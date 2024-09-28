from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from Services.questiongenerator_service import QuestionGeneratorService
import json

from Services.skillAnaliser_service import SkillAnaliserService
from utility.json_data_handler import JsonExtractor

app = Flask(__name__)

# Update the SQLALCHEMY_DATABASE_URI with your MySQL connection details
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Suma%402000@localhost/skill_based_analysis'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define your models (if not already defined)
class MsRole(db.Model):
    __tablename__ = 'ms_role'
    role_id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(255), nullable=False)

    # Define the relationship to DomainRoleLink
    domain_links = db.relationship('DomainRoleLink', back_populates='role')

class MsDomain(db.Model):
    __tablename__ = 'ms_domain'
    domain_id = db.Column(db.Integer, primary_key=True)
    domain_name = db.Column(db.String(255), nullable=False)

    # Define the relationship to DomainRoleLink
    domain_links = db.relationship('DomainRoleLink', back_populates='domain')

class MsExperience(db.Model):
    experience_id = db.Column(db.Integer, primary_key=True)
    experience_level = db.Column(db.String(255), nullable=False)

class DomainRoleLink(db.Model):
    __tablename__ = 'domain_role'
    id = db.Column(db.Integer, primary_key=True)
    domain_id = db.Column(db.Integer, db.ForeignKey('ms_domain.domain_id'), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('ms_role.role_id'), nullable=False)

    domain = db.relationship('MsDomain', back_populates='domain_links')
    role = db.relationship('MsRole', back_populates='domain_links')

@app.route('/')
def home():
    return render_template('homepage.html')
@app.route('/details')
def details_page():
    return render_template('Details.html')
@app.route('/result')
def results_page():
    # Get the question_data from the session
    question_data = session.get('question_data')
    return render_template('result.html', data=question_data)

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

@app.route('/analyze', methods=['POST'])
def analyze():
    domain_id = request.json.get('domain_id')
    role_id = request.json.get('role_id')
    experience_id = request.json.get('experience_id')


    # Perform your analysis logic here based on the domain_id and role_id
    # This is just a placeholder response
    return render_template('questionsPage.html')



@app.route('/mcq', methods=['POST'])
def mcq_question():
    # Get parameters from the POST request's JSON body
    domain = request.json.get('domain_id')
    role= request.json.get('role_id')
    experience_level = request.json.get('experience_id')

    # Call the generate_questions method with the unpacked dictionary
    objQuestionGenerator = QuestionGeneratorService()
    question_data = objQuestionGenerator.generate_questions(domain,role,experience_level)
    data = JsonExtractor().extract_json_from_response(question_data)

    # Respond with success and the data needed for the redirection
    return jsonify(success=True, data=data)


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
    question_data = format_ai_response(question_data)
    return question_data


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

