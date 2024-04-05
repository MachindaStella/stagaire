from odoo import api, exceptions, fields, models
from datetime import date
class EndWizard(models.TransientModel):
        _name = "choice.selection"
        _description = 'selection wizard'
        msg = fields.Text(string="Option", default="Choose an option",readonly=True)
       
        def create_attestation(self):
            return True

        # @api.model
        # def default_get(self, fields):
        #     res = super(EndWizard, self).default_get(fields)
        #     intern_id = self._context.get('active_id')
        #     intern = self.env['internship.registration'].browse(intern_id)
        #     interview_id = self._context.get('active_id')
        #     interview = self.env['interview'].browse(interview_id)
        #     if intern.status == 'end' and interview:
        #         res.update({interview.ending_date: date.today()})
        #     print("interview", interview)
        #     return res

        def call_create_project(self):
            self.env['project.project'].create_project()

        def ending_date_update(self):
            self.env['interview'].end_update()
