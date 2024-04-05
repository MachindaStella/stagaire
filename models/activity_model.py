
from odoo import models, fields

class ProjectTaskCopy(models.Model):
    _inherit = 'project.task'
    _order = 'name'
    
    intern_ids = fields.Many2many('internship.registration', 'activity_task', string='intern(s):')
    