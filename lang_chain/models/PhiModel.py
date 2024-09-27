# from dotenv import load_dotenv
# from langchain_community.chat_models import ChatOllama
# from .model_interface import ModelInterface
# from langchain_core.messages import HumanMessage
# from typing import List
#
# # Load environment variables from .env file
# load_dotenv()
#
# class PhiModel(ModelInterface):
#     def __init__(self, api_key: str):
#         self.model = ChatOllama(model="phi3:mini", base_url="http://192.168.68.118:11434")
#
#     def generate_text(self, messages: List[HumanMessage]) -> str:
#         result = self.model.invoke(messages)
#         return result.content
#
