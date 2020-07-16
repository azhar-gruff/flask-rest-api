# coding: utf-8
from sqlalchemy import Column, DateTime, Unicode
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



class CompanyCodeMapping(db.Model):
    __tablename__ = 'company_code_mapping'
    __table_args__ = {'schema': 'company'}

    company_code = db.Column(db.Unicode(15), primary_key=True)
    duns_no = db.Column(db.Unicode(15))
    company_unity_code = db.Column(db.Unicode(15))
    registration_date = db.Column(db.DateTime)
    update_date = db.Column(db.DateTime)
    registration_user_name = db.Column(db.Unicode(50))
    update_user_name = db.Column(db.Unicode(50))
