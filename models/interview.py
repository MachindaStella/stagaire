import string
from datetime import date
from odoo import models, fields

class InterviewPassage(models.Model):
    _name = 'interview'
    _description = "Interview Model"

    intern = fields.Many2one('internship.registration', string="intern:")
    intern_name = fields.Char(string="intern Name:",required =True)
    starting_date = fields.Date(string="Starting Date:", required =True)
    ending_date = fields.Date(string="Ending Date:", required =True)
    intern_marks = fields.Integer(string ="intern marks:", required =True)
    technical_skills = fields.Char(string ="Technical skills:", required =True)
    relevant_experience = fields.Char(string ="Relevant experience:", required =True)
    interpersonal_skills = fields.Char(string ="Interpersonal skills:", required =True)
    motivation_passion = fields.Char(string ="Motivation and passion:", required =True)
    adaptability_flexibility = fields.Char(string ="Adaptability and flexibility:", required =True)
    problem_solving_abilities = fields.Char(string ="Problem-solving abilities:", required =True)
    cultural_fit = fields.Char(string ="Cultural fit:", required =True)

    def accept(self):
        print('accept button')

    def refuse(self):
        print('accept button')

    def end_update(self):
        records = self.env['internship.registration'].browse(self._context.get('active_id'))
        data = self.env['interview'].browse(self._context.get('active_ids'))        
        if records.exists():
            for a in data:
                if records == a.intern:
            
                    if records.status == 'end':
                        a.write({'ending_date': date.today()}) 
                        self.env.cr.commit()
          

    def create_project(self):
        for record in self:
            values = {
                'project_id': record.project_id

            }
   


    def create_interview(self):
        record = self.env['internship.registration'].browse(self._context.get('active_id'))
        print("active id", record.name)
        values = {
            'intern_name': record.name,
            'starting_date': '2024-05-10',
            'ending_date': '2024-05-12',
            'intern_marks':10,
            'technical_skills': '50',
            'relevant_experience': '50',
            'interpersonal_skills': '50',
            'motivation_passion': '50',
            'adaptability_flexibility': '50',
            'problem_solving_abilities': '50',
            'cultural_fit': '50',

        }
        interview = self.env['interview'].create(values)

        return{
            'name': ('Interview'),
            'view_mode': 'form',
            'res_model': 'interview',
            'type': 'ir.actions.act_window',
            'res_id': self.env['interview'],
            'context': self.env.context,
        }


        @api.model
        def default_get(self, fields):
            res = super(EndWizard, self).default_get(fields)
            intern_id = self._context.get('active_id')
            intern = self.env['internship.registration'].browse(intern_id)
            if intern.status == 'end' and interview:
                res.update({'ending_date': date.today()})
            print("interview inside interview")

            return res

        
    

