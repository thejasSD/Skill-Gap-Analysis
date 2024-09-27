# from dotenv import load_dotenv
from dotenv import load_dotenv
from langchain_cohere import ChatCohere
from .model_interface import ModelInterface
from langchain_core.messages import HumanMessage
from typing import List
load_dotenv()

# Load environment variables from .env file
# load_dotenv()

class CohereModel(ModelInterface):
    def __init__(self, api_key: str):
        self.model = ChatCohere(model="command-r")

    def generate_text(self, messages) -> str:
        result = self.model.invoke(messages)
        return result.content

