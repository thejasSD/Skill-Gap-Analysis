import json
import re

from utility.logger import logger


class JsonExtractor:
    def __init__(self):
        self.pattern = r'\{[^{}]*\}'

    def extract_json_from_string(self,input_string):
        # Clean the input string by removing unwanted text
        start_idx = input_string.find('[')
        end_idx = input_string.rfind(']')
        json_string = input_string[start_idx:end_idx + 1]

        # Try to parse the JSON
        try:
            questions = json.loads(json_string)
            return questions
        except json.JSONDecodeError as e:
            print(f"Error parsing JSON: {e}")
            return None

