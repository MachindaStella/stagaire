import string
from odoo import api,models, fields
from odoo.exceptions import ValidationError

class InternshipRegistration(models.Model):
    _name = 'internship.registration'
    _description = "Registration Model"


    id = fields.Integer(string= "Intern ID:")
    name = fields.Char(string="Intern Name:", required=True)
    dob = fields.Date(string="Date of Birth:")
    internship_duration = fields.Integer(string="Duration:")
    supervisor = fields.Char(string="Intern Supervisor:")
    interview_day = fields.Date(string="Interview Date:")
    intern_profile = fields.Char(string="Intern Profile:")
    email = fields.Char(string="Email")
    end_visibility = fields.Boolean(compute= "_compute_visibility_check", store=True)


    
    internship_type = fields.Selection(
        string='Internship Type:',
        selection=[('Professional', 'Professional'), ('Academic', 'Academic')],
        help='Help to determine the type of internship performed by the intern'
    )

    highlighted_id = fields.Reference(
                    [("stagaire.interview", "intern_marks"), ("stagaire.activity",
                    "intern_ids")],
                    "Reference Highlight",
                    )



    date_regis = fields.Datetime.now()
    status = fields.Selection(
        string="Status:",
        selection=[("pending", 'Pending'),
                   ("accept", 'Accept'), 
                   ("refuse", 'Refuse'), 
                   ("end", 'End')
                   ], 
        required=True,
        default = 'pending')
    

    @api.depends('status')
    def _compute_visibility_check(self):
       for record in self:
            if record.status in ['pending', 'end']:
                record.end_visibility = True

            else:
                record.end_visibility = False

    def check_visibility(self):
        record = self.env['internship.registration'].browse(self._context.get('active_id'))

        if record:
            record._compute_visibility_check()

    
    # intern_starting_date = fields.Many2one( "stagaire.interview", string="Intern Starting Date",
    #                                         compute="_compute_intern_starting_day",
    # )

    # def _compute_intern_starting_day(self):
    #     for intern in self:
    #         intern.intern_startingButton_date = intern.interview_day
    
    ########  ########  ########  ########  constraints  ########  ########  ########  ########  

    _sql_constraints = [('intern_name_check',
                         'UNIQUE (name)',
                         'Name must be unique'),
                         ('intern_dob_check', 'CHECK (dob >= date_regis - INTERVAL "15 years")',
                           'Date of birth must be at least 5 years before the registration date')]
    

    @api.constrains('dob')
    def intern_dob_check(self):
        for record in self:
            if record.dob >= fields.Date.today(): 
                raise models.ValidationError('Date of birth cannot be inferieur equal to the registring date')
            

                        
    def all_transition(self, old_status, new_status):
        alltrans = [('pending', 'accept'),
        ('pending', 'refuse'),
        ('accept', 'end'),
        ('pending', 'end')]
        return (old_status, new_status) in alltrans
    
    def change_status(self, new_status):
        for allstatus in self:
            if allstatus.all_transition(allstatus.status,new_status):
                allstatus.status = new_status
            else:
                continue


    def status_pending(self):
        self.change_status("pending")

    def status_accept(self):
        self.change_status("accept")

    def status_refuse(self):
        self.change_status("refuse")

    def status_end(self):
      
            
        self.change_status("end")
        return {
            'name': 'Selection Choice',
            'type': 'ir.actions.act_window',
            'res_model': 'choice.selection',
            'view_mode': 'form',
            'target': 'new',
            'context': {
            },
        }

       


    def log_all_interns(self):
        internship_interns = self.env['internship.registration']
        all_interns = internship_interns.search([])
        return True
    

    # def change_interview_day(self):
    #     self.ensure_one()
    #     self.interview_day = fields.Date.today()

    # def change_update(self):
    #     self.ensure_one()
    #     self.update({
    #         'interview_day': fields.Datetime.now(),
    #         'internship_duration':"5",
    #         'status':"pending"
            
    #     })

    def get_current_interview_date(self):
        

        return self.interview_day




    def open_wizard(self):

        return {
            'name': 'Change Interview Date',
            'type': 'ir.actions.act_window',
            'res_model': 'interview.date.change',
            'view_mode': 'form',
            'target': 'new',
            'context': {
            },
    }
      

    # def status_pending(self):
    #     self.self.write({'status': "pending"})

    # def status_accept(self):
    #     self.write({'status': "accept"})

    # def status_refuse(self):
    #     self.write({'status': "refuse"})

    # def status_end(self):
    #     self.write({'status': "end"})




    def name_get(self):
        result = []
        for record in self:
            rec_name = "%s (%s)" % (record.name, record.date_regis)
        result.append((record.id, rec_name))
        return result
    

    # INTERN REPORT

    def _get_report_base_filename(self):
        self.ensure_one()
        return 'Report of %s' % (self.name)


    
    def call_create_interview(self):
        self.env['interview'].create_interview()

   

    

