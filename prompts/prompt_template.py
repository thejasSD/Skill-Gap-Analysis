from langchain.prompts import ChatPromptTemplate


class PromptTemplate:

    def build_mcq_prompt_quetion(self):
        """Builds the prompt for generating MCQ questions."""
        experience_level = "beginner to intermediate" if 2 <= 1 else "advanced"
        input_data = {
            "experience_level":experience_level
        }

        messages = [
            ("system",
             f"You are a trivia master who generates 10 multiple-choice questions related to softwere developer in python. These questions should assess a Python developer's skills at a(n) intermediate level with 3 years of experience. Each question should include:"),
            ("system", f"- `category`: Set this to Python development (Python development)."),
            ("system", f"- `sub_category`: Set this to Python programming (Python programming)."),
            ("system", "- `question_name`: A short title for the question."),
            ("system", "- `question_description`: The actual question text."),
            ("system", "- `options`: A dictionary containing four options labeled '1' to '4'."),
            ("system", "- `correct_option`: The key corresponding to the correct answer in the options."),
            ("system", f"- `level_id`: Set this to 3 (corresponding to the developer's experience)."),
            ("system",
             f"The questions should cover topics relevant to 3 Python developers, such as basic syntax, OOP, libraries, optimization, and concurrency, based on their experience. The output should be a JSON array containing all the questions."),
            ("human", "Generate the questions.")
        ]
        prompt_template = ChatPromptTemplate.from_messages(messages)
        return prompt_template.invoke(input_data)

