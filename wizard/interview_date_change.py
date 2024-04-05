from odoo import api, exceptions, fields, models

class InterviewChange(models.TransientModel):
    _name = "interview.date.change"
    _description = "check interview day"
    current_date = fields.Date(readonly=True)
    new_date = fields.Date()


    def open(self):
        intern_id = self._context.get('active_ids')
        intern = self.env['internship.registration'].browse(intern_id)
        self.current_date = intern.get_current_interview_date()
        
        return super(InterviewChange, self).open()
    

    
    def change_interview_date(self):
        intern_id = self._context.get('active_ids')
        intern = self.env['internship.registration'].browse(intern_id)
        self.current_date = intern.get_current_interview_date()
        intern.write({'interview_day': self.new_date})

    @api.model
    def default_get(self, list_fields):
        res = super(InterviewChange, self).default_get(list_fields)
        intern_id = self._context.get('active_id')
        list_fields = self.env['internship.registration'].browse(intern_id)
        if list_fields.exists():
             res.update({ 'current_date': list_fields.interview_day})
        return res


  