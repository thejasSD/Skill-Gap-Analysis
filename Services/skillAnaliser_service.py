from lang_chain.models.language_model_selector import LanguageModelSelector
from prompts.prompt_template import PromptTemplate
from utility.constants import Constants
from utility.json_data_handler import JsonExtractor
from utility.logger import logger



class SkillAnaliserService:

    def skill_analis(self,json=None):
        """
        Entry point to generate questions based on given parameters.
        """
        try:

            prompt = PromptTemplate().build_skill_analyser_prompt(json)
            selector = LanguageModelSelector()
            response, chat_history = selector.invoke_model("ModelAI", "llama3-8b-8192", prompt)
            # response,chat_history = selector.invoke_model("cohere", "command-r", prompt)
            logger.info(f'Response received from API: {response}')
            # obj_format_json = JsonExtractor()
            # response = obj_format_json.extract_json_from_string(response)
            # return response
            return response
        except Exception as e:
            logger.exception(f"Error occurred during the question generation: {e}")

        except Exception as e:
            logger.exception(f"Error occurred during the question generation as {e}")

    def generate_question_data(self,domain,role,experience_level):
        """
        Generates questions based on the type, number, level, and categories provided.
        """
        try:
            prompt = PromptTemplate().build_mcq_prompt_quetion(domain,role,experience_level)

            # prompt = PromptTemplate().prompt_template(template)
            selector = LanguageModelSelector()
            response,chat_history = selector.invoke_model("ModelAI", "llama3-8b-8192", prompt)
            # response,chat_history = selector.invoke_model("cohere", "command-r", prompt)
            logger.info(f'Response received from API: {response}')
            obj_format_json = JsonExtractor()
            response = obj_format_json.extract_json_from_string(response)
            # return response
            return response
        except Exception as e:
            logger.exception(f"Error occurred during the question generation: {e}")


