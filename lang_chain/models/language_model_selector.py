# from dotenv import load_dotenv
from langchain.schema import AIMessage, HumanMessage, SystemMessage
from .cohere_model import CohereModel
from .model_interface import ModelInterface
# from .llama_model import Llama

# Load environment variables from the .env file
# load_dotenv()

class LanguageModelSelector:
    """
    LanguageModelSelector class for selecting and interacting with various language models.
    """

    def __init__(self):
        """
        Initializes the LanguageModelSelector with available models.
        """
        self.models = {
            'cohere': CohereModel,
            # 'llama': Llama
        }

    def get_model(self, model_name: str, model_variant: str) -> ModelInterface:
        """
        Retrieves the model instance based on the model name and variant.

        :param model_name: The name of the model to retrieve.
        :param model_variant: The variant of the model to retrieve.
        :return: An instance of the selected model that implements ModelInterface.
        :raises ValueError: If the provided model name is not supported.
        """
        if model_name in self.models:
            return self.models[model_name](model_variant)
        else:
            raise ValueError(f"Unsupported model name: {model_name}")

    def format_chat_history(self, prompt, chat_history=None):
        """
        Formats the chat history based on the prompt type.

        :param prompt: The input prompt, which may contain messages.
        :param chat_history: The chat history to append to (optional).
        :return: The updated chat history.
        :raises ValueError: If an unsupported message type is encountered.
        """
        if chat_history is None:
            chat_history = []

        if hasattr(prompt, 'messages') and isinstance(prompt.messages, list):
            for message in prompt.messages:
                if isinstance(message, SystemMessage):
                    chat_history.append({"role": "system", "content": message.content})
                elif isinstance(message, HumanMessage):
                    chat_history.append({"role": "user", "content": message.content})
                else:
                    raise ValueError(f"Unsupported message type: {type(message)}")
        else:
            chat_history.append({"role": "user", "content": prompt})

        return chat_history

    def invoke_model(self, model_name: str, model_variant: str, prompt, chat_history=None):
        """
        Invokes the model with the provided chat history and prompt.

        :param model_name: The name of the model to invoke.
        :param model_variant: The variant of the model to invoke.
        :param prompt: The input prompt for the model.
        :param chat_history: The chat history to pass along with the prompt (optional).
        :return: The model's response and the updated chat history.
        """
        # Format the chat history based on the prompt
        chat_history = self.format_chat_history(prompt, chat_history)

        # Get the model instance
        model = self.get_model(model_name, model_variant)

        # Invoke the model with the formatted chat history
        response = model.generate_text(chat_history)

        # Add the model's response to the chat history
        chat_history.append(AIMessage(content=response))

        # Return both the response and the updated chat history
        return response, chat_history
