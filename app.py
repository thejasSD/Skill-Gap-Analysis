from flask import Flask, render_template, request, jsonify

from Services.questiongenerator_service import QuestionGeneratorService

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    # Example: Get data from the frontend (like skill sets) and process it.
    skill_data = request.json
    # Dummy response for demonstration
    response = {"message": "Skill analysis complete", "gaps": ["Python", "Data Analysis"]}
    return jsonify(response)


from flask import request, jsonify


@app.route('/mcq', methods=['POST'])
def mcq_question():
    # Get parameters from the POST request's JSON body
    params = request.form.to_dict()  # Expecting JSON data in the POST body
    questions_type = str(params.get('questions_type'))
    number_of_questions = int(params.get('number_of_questions'))
    level_id = int(params.get('level_id'))
    category = str(params.get('category'))
    sub_category = str(params.get('sub_category'))
    # Call the generate_questions method with the unpacked dictionary
    if params:
        objQuestionGenerator = QuestionGeneratorService()
        question_data = objQuestionGenerator.generate_questions(questions_type, number_of_questions, level_id, category,
                                                        sub_category)
        return jsonify(question_data)  # Returning the generated questions as JSON
    else:
        return jsonify({"error": "No data provided"}), 400

if __name__ == '__main__':
    app.run()
