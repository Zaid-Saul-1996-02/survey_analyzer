from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import StateGraph, START
from langchain.schema import SystemMessage, HumanMessage, AIMessage # Esto es necesario para el eval del checkpointer
from langchain_core.messages import ToolMessage

from agent.utils_agent.state_agent import State
from agent.utils_agent.node_agent import iniciar, chat, tool_node_chat
from agent.utils_agent.edges_agent import get_state_init, get_state_chat

from agent.utils_agent.utils_db.db_mongo_utils import MongoDbAgent

def agent(user_id:str, mensaje:str, url_matriz:str, url_contexto:str) -> str:
    
    memory = MemorySaver()

    workflow = StateGraph(State) # Creo mi grafo con la clase Satate

    # Nodes
    workflow.add_node('iniciar', iniciar)

    workflow.add_node('chat', chat)
    workflow.add_node('tool_chat', tool_node_chat)

    # Edges
    workflow.add_conditional_edges(START, get_state_init)
    workflow.add_edge('iniciar', 'chat')
    workflow.add_conditional_edges('chat', get_state_chat)
    workflow.add_edge('tool_chat', 'chat')

    graph = workflow.compile(checkpointer=memory)
    
    conversation_id = f"{url_matriz}/user-{user_id}"

    try:
        state_values = MongoDbAgent().load_state(conversation_id) # aqui cargo el checkpointer de la DB
    except Exception as e:
        return 'Lo siento, se ha presentado un problema de conexion, espera unos segundos y vuelveremos a conversar'

    config = {"configurable": {"thread_id": conversation_id}}

    if state_values is not None:
        #print('if')

        state_values = eval(state_values)

        graph.update_state(config, state_values)
    else:
        #print('else')
        
        graph.update_state(config, {'url_contexto':str(url_contexto), 'nodo':'iniciar', 'url_matriz':str(url_matriz)})

    """
    mensaje_ia = ''
    for event in graph.stream({"messages": ("user", mensaje)}, config=config):
        for value in event.values():
            #print("Assistant:", value["messages"][-1].content)
            
            if "messages" in value:
                last_message = value["messages"][-1]
            else:
                continue

            if not(isinstance(last_message,ToolMessage)):
                mensaje_ia += last_message.content + '\n'
    """
    
    resp = graph.invoke({"messages": ("user", mensaje)}, config=config)
    mensaje_ia = resp['messages'][-1].content

    state_values = graph.get_state(config).values

    messages = state_values['messages']
    can_messages = 6

    if len(messages) >= can_messages:

        messages = messages[-1 * can_messages:]

        if isinstance(messages[0], ToolMessage): 
            messages = messages[1:]
        
        state_values['messages'] = messages

    try:
        MongoDbAgent().save_state(conversation_id, state_values)
    except Exception as e:
        pass
    
    return mensaje_ia