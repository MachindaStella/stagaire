import string
from odoo import models, fields

class InterviewQuestions(models.Model):
    _name = 'interview.questions'
    _description = "interview question Model"


    question = fields.Char(string="question:", required=True)