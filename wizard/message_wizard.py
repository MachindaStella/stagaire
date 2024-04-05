from odoo import api, exceptions, fields, models

from odoo.exceptions import ValidationError

class InterviewCheck(models.TransientModel):
    _name = "interview.check"
    _description = "check interview day"
    interview_ids = fields.Many2many("internship.registration", string="Interviews")
    message_subject = fields.Char()
    message_body = fields.Char()

    def send_email(self):
        # Retrieve the selected interns
        interns = self.interview_ids

        # Retrieve the email addresses of the selected interns
        email_addresses = interns.mapped('email')

        # Check if any interns have been selected
        if not email_addresses:
            raise UserError("No interns selected.")

        # Compose the email
        subject = self.message_subject
        body = self.message_body

        # Send the email
        self.env['mail.mail'].create({
            'subject': subject,
            'body_html': body,
            'email_to': ','.join(email_addresses),
        }).send()