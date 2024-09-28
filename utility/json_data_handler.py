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


    def extract_json_from_response(self,response):
        try:
            # Check if response is a string
            if isinstance(response, str):
                json_string = response  # It's already a string

            # Check if response is bytes
            elif isinstance(response, bytes):
                json_string = response.decode('utf-8')  # Decode bytes to string

            # Check if response is a dictionary
            elif isinstance(response, dict):
                json_string = json.dumps(response)  # Convert dict to JSON string

            elif isinstance(response, list):
                results = []
                # Iterate over each item in the list
                for item in response:
                    if isinstance(item, dict):
                        # Accessing specific fields
                        category = item.get("category")
                        question_name = item.get("question_name")
                        question_description = item.get("question_description")
                        options = item.get("options")
                        correct_option = item.get("correct_option")

                        # Create a dictionary for the current question
                        question_data = {
                            "category": category,
                            "question_name": question_name,
                            "options": options,
                            "correct_option": correct_option,
                            "question_description":question_description
                        }

                        # Append the question data to results
                        results.append(question_data)
                    else:
                        print("Item is not a dictionary.")

                # Return the results as a JSON string
                return json.dumps(results, indent=4)
            else:
                raise ValueError("Unsupported response type.")

            # Load the string as JSON
            extracted_json = json.loads(json_string)
            return extracted_json

        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            return None
        except Exception as e:
            print(f"Error processing response: {e}")
            return None
