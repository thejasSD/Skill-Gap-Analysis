from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from Services.questiongenerator_service import QuestionGeneratorService

app = Flask(__name__)

# Update the SQLALCHEMY_DATABASE_URI with your MySQL connection details
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:12345678@localhost/skill_based_analysis'
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
    return render_template('index.html')

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
    analysis_result = {
        'analysis': f'This is the analysis result based on selected domain and role.'
    }
    return jsonify(analysis_result)


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

