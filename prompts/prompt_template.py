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

    def build_skill_analyser_prompt(self, json_data=None):
        """Builds the prompt for analyzing skills based on the provided JSON data."""
        json_data =[
        {
            "question_name": "Python Basics",
            "question_description": "What is the output of the following Python code: print(10 // 3)?",
            "chosed_option": "1"
        },
        {
            "question_name": "Logical Reasoning",
            "question_description": "Five switches are connected to five light bulbs. Each switch corresponds to one light bulb. You can turn the switches on and off as many times as you want. How can you ensure that you can identify which switch corresponds to which light bulb?",
            "chosed_option": "1"
        },
        {
            "question_name": "World History",
            "question_description": "Which ancient civilization built the city of Petra?",
            "chosed_option": "4"
        },
        {
            "question_name": "Basic Math",
            "question_description": "What is the value of x in the equation 2x + 5 = 11?",
            "chosed_option": "2"
        },
        {
            "question_name": "English Grammar",
            "question_description": "Which of the following sentences is in the passive voice?",
            "chosed_option": "2"
        },
        {
            "question_name": "Python Syntax",
            "question_description": "What is the output of the following Python code: print('Hello' + ' ' + 'World')?",
            "chosed_option": "1"
        },
        {
            "question_name": "Logical Reasoning",
            "question_description": "A bat and a ball together cost $1.10. The bat costs $1.00 more than the ball. How much does the ball cost?",
            "chosed_option": "2"
        },
        {
            "question_name": "Science",
            "question_description": "What is the largest planet in our solar system?",
            "chosed_option": "3"
        },
        {
            "question_name": "Basic Math",
            "question_description": "What is the value of y in the equation x + 2y = 7 and x = 3?",
            "chosed_option": "2"
        },
        {
            "question_name": "English Grammar",
            "question_description": "Which of the following sentences is in the active voice?",
            "chosed_option": "3"
        },
        {
            "question_name": "Python Basics",
            "question_description": "What is the output of the following Python code: print(10 % 3)?",
            "chosed_option": "1"
        },
        {
            "question_name": "Logical Reasoning",
            "question_description": "A snail is at the bottom of a 20-foot well. Each day, it climbs up 3 feet, but at night, it slips back 2 feet. How many days will it take for the snail to reach the top of the well?",
            "chosed_option": "18"
        },
        {
            "question_name": "History",
            "question_description": "Who was the leader of the Soviet Union during World War II?",
            "chosed_option": "2"
        },
        {
            "question_name": "Basic Math",
            "question_description": "What is the value of x in the equation 5x = 25?",
            "chosed_option": "2"
        },
        {
            "question_name": "English Grammar",
            "question_description": "Which of the following sentences is in the present perfect tense?",
            "chosed_option": "1"
        },
        {
            "question_name": "Python Syntax",
            "question_description": "What is the output of the following Python code: print('Hello' * 3)?",
            "chosed_option": "1"
        },
        {
            "question_name": "Logical Reasoning",
            "question_description": "A farmer has 100 feet of fencing and wants to enclose a rectangular area with an existing barn as one side. What is the maximum area the farmer can enclose?",
            "chosed_option": "2"
        },
        {
            "question_name": "Science",
            "question_description": "What is the process by which water moves through a plant, from the roots to the leaves, and is then released into the air as water vapor?",
            "chosed_option": "3"
        },
        {
            "question_name": "Basic Math",
            "question_description": "What is the value of y in the equation 2x + y = 5 and x = 2?",
            "chosed_option": "3"
        },
        {
            "question_name": "English Grammar",
            "question_description": "Which of the following sentences is in the passive voice?",
            "chosed_option": "1"
        },
        {
            "question_name": "Python Syntax",
            "question_description": "What is the output of the following Python code: print(10 / 3)?",
            "chosed_option": "3"
        },
        {
            "question_name": "Logical Reasoning",
            "question_description": "A man is looking at a photograph of someone. His friend asks him, 'Who is in the photograph?' The man replies, 'Brother of my husband.' Who is in the photograph?",
            "chosed_option": "2"
        },
        {
            "question_name": "History",
            "question_description": "Which ancient civilization built the city of Babylon?",
            "chosed_option": "4"
        },
        {
            "question_name": "Basic Math",
            "question_description": "What is the value of x in the equation x - 3 = 7?",
            "chosed_option": "4"
        },
        {
            "question_name": "English Grammar",
            "question_description": "Which of the following sentences is in the future tense?",
            "chosed_option": "1"
        },
        {
            "question_name": "Python Basics",
            "question_description": "What is the output of the following Python code: print(10 ** 2)?",
            "chosed_option": "2"
        },
        {
            "question_name": "Logical Reasoning",
            "question_description": "A bat and a ball together cost $1.10. The bat costs $1.00 more than the ball. How much does the bat cost?",
            "chosed_option": "3"
        },
        {
            "question_name": "Science",
            "question_description": "What is the process by which plants convert sunlight into energy?",
            "chosed_option": "1"
        },
        {
            "question_name": "Basic Math",
            "question_description": "What is the value of y in the equation 2y = 10?",
            "chosed_option": "2"
        },
        {
            "question_name": "English Grammar",
            "question_description": "Which of the following sentences is in the present perfect tense?",
            "chosed_option": "1"
        },
        {
            "question_name": "Python Syntax",
            "question_description": "What is the output of the following Python code: print(10 // 2)?",
            "chosed_option": "1"
        },
        {
            "question_name": "Logical Reasoning",
            "question_description": "A snail is at the bottom of a 20-foot well. Each day, it climbs up 3 feet, but at night, it slips back 2 feet. How many days will it take for the snail to reach the top of the well?",
            "chosed_option": "18"
        },
        {
            "question_name": "History",
            "question_description": "Who was the leader of the Soviet Union during World War II?",
            "chosed_option": "2"
        },
        {
            "question_name": "Basic Math",
            "question_description": "What is the value of x in the equation x + 5 = 10?",
            "chosed_option": "3"
        },
        {
            "question_name": "English Grammar",
            "question_description": "Which of the following sentences is in the passive voice?",
            "chosed_option": "1"
        },
        {
            "question_name": "Python Basics",
            "question_description": "What is the output of the following Python code: print(10 % 3)?",
            "chosed_option": "1"
        }]
        # json_data = self.apply_escape_to_all(json_data)
        content = self.format_questions(json_data)

        messages = [
            ("system", f"Analyze the following JSON data containing a series of questions and answers: {content}."),
            ("system",
             "For each question, identify the user's skills based on their responses. Specifically, consider the following:"),
            ("system", "1. **Categories and Performance:**"),
            ("system", "- Count how many questions were answered correctly versus incorrectly in each category."),
            ("system",
             "- Identify the categories where the user has a high success rate and those where they struggled."),
            ("system", "2. **Skill Assessment:**"),
            ("system",
             "- For each category, determine if the user demonstrates proficiency, basic understanding, or significant gaps in knowledge."),
            ("system", "- Provide a summary of the user’s strengths and weaknesses across the categories."),
            ("system", "3. **Personalized Improvement Areas:**"),
            ("system",
             "- Highlight specific areas where the user is lacking based on the questions answered incorrectly."),
            ("system", "- Suggest targeted improvement areas for the user to focus on."),
            ("system", "4. **Recommendations:**"),
            ("system", "- Offer actionable recommendations for improvement, such as:"),
            ("system",
             "  - Resources (books, online courses, tutorials) to enhance knowledge in the identified weak areas."),
            ("system", "  - Practice strategies, like solving more problems in those categories."),
            ("system", "  - Setting specific learning goals to track progress over time."),
            ("system", "5. **Example Analysis:**"),
            ("system", "- **Categories:**"),
            ("system", "  - Logical Reasoning: 2 correct, 2 incorrect"),
            ("system", "  - General Knowledge: 4 correct, 1 incorrect"),
            ("system", "  - Math: 3 correct, 2 incorrect"),
            ("system", "  - English Grammar: 3 correct, 1 incorrect"),
            ("system", "- **Strengths:**"),
            ("system", "  - Proficient in General Knowledge and Python Basics."),
            ("system", "- **Weaknesses:**"),
            ("system", "  - Struggling with Logical Reasoning and Math, particularly problem-solving and equations."),
            ("system", "- **Personalized Improvement Areas:**"),
            ("system", "  - Improve understanding of logical reasoning concepts and mathematical equations."),
            ("system", "- **Recommendations:**"),
            ("system", "  - Enroll in a basic math course or a logical reasoning workshop."),
            ("system", "  - Regularly practice problems from those categories using online resources or textbooks."),
            ("system",
             "  - Set a goal to complete at least 10 logical reasoning problems each week to build confidence."),
            ("human", "Provide the analysis based on the given data.")
        ]

        prompt_template = ChatPromptTemplate.from_messages(messages)
        return prompt_template.invoke({"content": content})

    def apply_escape_to_all(self,fields):
        """Applies escape_curly_braces to all fields in a dictionary."""
        return {key: self.escape_curly_braces(value) for key, value in fields.items()}

    def escape_curly_braces(self,text):
        """Escapes curly braces in the given text."""
        if isinstance(text, str):
            return text.replace("{", "{{").replace("}", "}}")
        return text

    def format_questions(self,questions):
        formatted_string = ""

        for question in questions:
            formatted_string += f"Question Name: {question['question_name']}\n"
            formatted_string += f"Description: {question['question_description']}\n"
            formatted_string += f"Chosen Option: {question['chosed_option']}\n\n"

        return formatted_string.strip()


