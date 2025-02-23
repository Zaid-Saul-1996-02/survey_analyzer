from pymongo import MongoClient
from os import getenv
from dotenv import load_dotenv
from typing import Optional, Any
from langchain.schema import (
    SystemMessage, 
    HumanMessage, 
    AIMessage
) # Esto es necesario para el eval del checkpointer

load_dotenv()

class MongoDbAgent(object):

    def __init__(self, uri: Optional[str] = None, data_base: Optional[str] = None) -> None:
        self.uri = uri if uri is not None else getenv('URI_MONGO')
        self.data_base = data_base if data_base is not None else getenv('NAME_DB_MONGO')

    def get_db_collection(self, collection: str) -> Any:
        client = MongoClient(self.uri)
        db = client[self.data_base]
        return db[collection]

        
    def load_state(self, id: str, collection_name: Optional[str] = None) -> Optional[str]:
        """Carga el checkpointer desde la base de datos."""
        
        collection_name = collection_name if collection_name is not None else getenv('NAME_STATE_COLLECTION_DB_MONGO')

        collection = self.get_db_collection(collection_name)

        document = collection.find_one({"ID": id})

        if document:
            state_values = document.get('state_values', '')
            state_values = eval(state_values)
            return state_values

        return None # Aqui no quiero manejar la excepcion, lo necesito hacer por logica donde uso el metodo
        

    def save_state(self, id: str, state_values:str, collection_name: Optional[str] = None) -> None:
        """Guarda el checkpointer en la base de datos."""
    
        collection_name = collection_name if collection_name is not None else getenv('NAME_STATE_COLLECTION_DB_MONGO')

        state_values = str(state_values)
        
        collection = self.get_db_collection(collection_name)

        collection.update_one(
            {"ID": id},
            {"$set": {
                "state_values": state_values
            }},
            upsert=True
        ) # Aqui no quiero manejar la excepcion, lo necesito hacer por logica donde uso el metodo

