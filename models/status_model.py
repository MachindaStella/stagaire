from odoo import models, fields

class Status(models.Model):
    _name = 'status'
    _description = "status model"


    status = fields.Char(string="status:", required=True)
