    activity_task = fields.Many2one('project.task', string="Activity")
    intern_ids = fields.Many2one('internship.registration', 'activity_task', string='intern')
    intern_ids = fields.Many2one('internship.registration', string="intern", required =True)


