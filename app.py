from flask import Flask, request, jsonify, session, render_template, url_for
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from Services.questiongenerator_service import QuestionGeneratorService
from Services.skillAnaliser_service import SkillAnaliserService
from utility.json_data_handler import JsonExtractor
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')

# Update the SQLALCHEMY_DATABASE_URI with your MySQL connection details
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Configure session to use filesystem (can also use Redis or other options)
app.config['SESSION_TYPE'] = os.getenv('SESSION_TYPE')
Session(app)

# Import the models and initialize the database
from models import db
from models.models import MsRole, MsDomain, MsExperience, DomainRoleLink

db.init_app(app)

@app.route('/')
def home():
    return render_template('homepage.html')

@app.route('/details')
def details_page():
    return render_template('Details.html')

@app.route('/get_data', methods=['GET'])
def get_data():
    # Fetch all domains
    domains = MsDomain.query.all()
    domain_list = [{'id': domain.domain_id, 'name': domain.domain_name} for domain in domains]

    # Fetch all roles
    roles = MsRole.query.all()
    role_list = [{'id': role.role_id, 'name': role.role_name} for role in roles]

    # Fetch all experience levels
    experiences = MsExperience.query.all()
    experience_list = [{'id': exp.experience_id, 'name': exp.experience_level} for exp in experiences]

    return jsonify({'domains': domain_list, 'roles': role_list, 'experiences': experience_list})

@app.route('/get_roles_by_domain', methods=['POST'])
def get_roles_by_domain():
    domain_id = request.json['domain_id']
    roles = DomainRoleLink.query.filter_by(domain_id=domain_id).all()
    role_list = [{'id': role_link.role.role_id, 'name': role_link.role.role_name} for role_link in roles]

    return jsonify({'roles': role_list})

@app.route('/questionsPage')
def questions_page():
    # Retrieve parameters from the URL
    domain_id = request.args.get('domain_id')
    role_id = request.args.get('role_id')
    experience_id = request.args.get('experience_id')

    # Here you could call the question generation function again if needed
    objQuestionGenerator = QuestionGeneratorService()
    question_data = objQuestionGenerator.generate_questions(domain_id, role_id, experience_id)
    data = JsonExtractor().extract_json_from_response(question_data)

    return render_template('questionsPage.html', data=data)

@app.route('/skillanaliser', methods=['POST'])
def skill_pages():
    data = request.get_json()
    # Here you could call the question generation function again if needed
    objSkillAnaliser = SkillAnaliserService()
    question_data = objSkillAnaliser.skill_analis(data)
    formatted_data = format_ai_response(question_data)

    # Store the result in session or a global variable
    session['analysis_result'] = formatted_data  # Use session to store the analysis result
    return jsonify(success=True, redirect_url=url_for('show_result'))

@app.route('/result')
def show_result():
    analysis_result = session.get('analysis_result', "No result available.")
    return render_template('result.html', analysis_result=analysis_result)

# Function to clean and format the AI response
def format_ai_response(response_text):
    # Remove unnecessary characters like ** and extra spaces/newlines
    clean_text = response_text.replace("**", "").strip()

    # Split text by new lines and clean up any unwanted blank lines
    formatted_lines = []
    for line in clean_text.split("\n"):
        line = line.strip()  # Remove leading/trailing spaces
        if line:  # Skip empty lines
            # Add double line breaks after section titles for better separation
            if line.endswith(":"):
                formatted_lines.append(f"{line}\n\n")  # Double line break after section title
            # Add a single line break for bullet points
            elif line.startswith("* "):
                formatted_lines.append(f"{line}\n")  # Single line break for bullet points
            else:
                formatted_lines.append(line)

    # Join lines back with a newline separator
    formatted_text = "\n".join(formatted_lines).strip()
    return formatted_text

if __name__ == '__main__':
    app.run()
