from lang_chain.models.language_model_selector import LanguageModelSelector
from prompts.prompt_template import PromptTemplate
from utility.constants import Constants
from utility.json_data_handler import JsonExtractor
from utility.logger import logger



class QuestionGeneratorService:

    def generate_questions(self, questions_type, number_of_questions, level_id, category,
                                                        sub_category):
        """
        Entry point to generate questions based on given parameters.
        """
        try:

            question_data = self.generate_question_data()
            # evaluator = Evaluator()
            # responce = evaluator.evaluate_questions(question_data)
            return question_data
            # self.save_questions_to_database(question_data, questions_type)

        except Exception as e:
            logger.exception(f"Error occurred during the question generation as {e}")

    def generate_question_data(self):
        """
        Generates questions based on the type, number, level, and categories provided.
        """
        try:
            prompt = PromptTemplate().build_mcq_prompt_quetion()

            # prompt = PromptTemplate().prompt_template(template)
            selector = LanguageModelSelector()
            response,chat_history = selector.invoke_model("cohere", "command-r", prompt)
            logger.info(f'Response received from API: {response}')
            # return response
            return response
        except Exception as e:
            logger.exception(f"Error occurred during the question generation: {e}")

    def convert_level_id(self, level_id):
        """Converts level_id from 'easy', 'medium', 'hard' to 1, 2, 3 respectively."""
        if isinstance(level_id, str):
            return Constants.DIFFICULTY_LEVEL.get(level_id.lower(), level_id)
        return level_id


