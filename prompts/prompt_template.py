from langchain.prompts import ChatPromptTemplate


class PromptTemplate:

    def build_mcq_prompt_quetion(self,domain,role,experience_level):
        """Builds the prompt for generating MCQ questions."""
         # Experience level, e.g., 3 for intermediate, can also be dynamic.

        input_data = {
            "experience_level":experience_level,
            "role":role,
            "domain":domain
        }

        messages = [
            ("system",
             f"You are a trivia master who generates 30 multiple-choice for {domain} questions across various topics. These questions should evaluate a candidate's skills, with some focused on {role} at {experience_level}  of experience and others covering general aptitude, logical reasoning, simple math, general knowledge, and grammar. Each question should include:"),
            ("system",
             f"- `category`: Set this based on the topic (e.g., {role}, aptitude, general knowledge, math, logical reasoning, grammar)."),
            ("system",
             f"- `sub_category`: Set this based on the specific sub-topic (e.g., {role}, basic math, English grammar, world history, etc.)."),
            ("system", "- `question_name`: A short title for the question."),
            ("system", "- `question_description`: The actual question text."),
            ("system", "- `options`: A dictionary containing four options labeled '1' to '4'."),
            ("system", "- `correct_option`: The key corresponding to the correct answer in the options."),
            ("system", f"- `level_id`: Set this to {experience_level} for intermediate-level questions."),
            ("system",
             f"The {role} questions should focus on topics relevant to the role, such as basic syntax, OOP, libraries, optimization, and concurrency. The aptitude, general knowledge, logical reasoning, and grammar questions should challenge the candidate's reasoning, math skills, general awareness, and language abilities. The output should be a JSON array containing all 30 questions."),
            ("human", "Generate the questions.")
        ]

        prompt_template = ChatPromptTemplate.from_messages(messages)
        return prompt_template.invoke(input_data)

