from .state_agent import State
from langgraph.graph import END
from typing import Literal

def get_state_init(state: State)->Literal["iniciar", "chat", '__end__']:
    
    nodo = state["nodo"]
    
    if nodo in {'iniciar', 'chat'}:
        return nodo
    
    return END

def get_state_chat(state: State) -> Literal['tool_chat', '__end__']:

    last_messages = state['messages'][-1]

    if last_messages.tool_calls:
        return 'tool_chat'
    
    return END