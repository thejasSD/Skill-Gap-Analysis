from . import db

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
