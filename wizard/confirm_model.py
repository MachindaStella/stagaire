from odoo import api, exceptions, fields, models

class GenTestWizard(models.TransientModel):
        _name = "confirm.change"
        _description = 'Testing of wizard'
        msg = fields.Text(string="Confirm", default="Do you want to change the interview date?",readonly=True)
       
        def yes(self):
            return True

        
        def no(self):
            return False 
