# from dotenv import load_dotenv
# from langchain_community.chat_models import ChatOllama
# from .model_interface import ModelInterface
# from langchain_core.messages import HumanMessage
# from typing import List
#
# # Load environment variables from .env file
# load_dotenv()
#
# class Llama(ModelInterface):
#     def __init__(self, api_key: str):
#         self.model = ChatOllama(model="llama3.1", base_url="http://127.0.0.1:11434")
#
#     def generate_text(self, messages: List[HumanMessage]) -> str:
#         result = self.model.invoke(messages)
#         return result.content
#
