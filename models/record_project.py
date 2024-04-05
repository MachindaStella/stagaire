
from odoo import models, fields

class ProjectCreation(models.Model):
    _inherit = 'project.project'
    _order = 'name'
    
    def create_project(self):
            
        values = {
            'name': 'Stella',

        }
        
        project = self.env['project.project'].create(values)

        return{
            'name': ('Project'),
            'view_mode': 'list',
            'res_model': 'project.project',
            'type': 'ir.actions.act_window',
            'res_id': self.env['project.project'],
            'context': self.env.context,
        }
    
    