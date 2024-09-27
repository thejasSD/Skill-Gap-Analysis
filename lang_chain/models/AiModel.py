import os
# from langchain_openai import ChatOpenAI
# from langchain_core.messages import HumanMessage, SystemMessage
# from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq

from dotenv import load_dotenv
from langchain_community.chat_models import ChatOllama
from .model_interface import ModelInterface
from langchain_core.messages import HumanMessage
from typing import List

# Load environment variables from .env file
load_dotenv()
class ModelAI(ModelInterface):
    def __init__(self, api_key: str):
        self.model = ChatGroq(model="llama3-8b-8192")

    def generate_text(self, messages: List[HumanMessage]) -> str:
        result = self.model.invoke(messages)
        return result.content