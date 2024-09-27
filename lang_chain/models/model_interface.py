from langchain_core.messages import HumanMessage, SystemMessage
from typing import List

class ModelInterface:
    def generate_text(self, messages) -> str:
        raise NotImplementedError("This method should be overridden in subclasses")
