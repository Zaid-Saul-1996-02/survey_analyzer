from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph.message import add_messages


class State(TypedDict):
    url_contexto:str
    url_matriz:str
    text_contexto: str
    nodo: str
    messages: Annotated[list, add_messages]