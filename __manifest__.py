
#############################################################################
{
    'name': 'Internship',
    'version': '17.0.1.0.0',
    'category': 'Employers',
    'summary': 'Employer follows interns',
    'description': 'This module will help employers to follow up interns from thier registration'
                   'to the end of thier internship',
    'live_test_url': '',
    'author': 'Third',
    'company': 'Third Sarl',
    'maintainer': 'Third',
    'website': 'https://third.cm',
    'depends': ['base','project'],
    'data': [
        'security/group.xml',
        'security/ir.model.access.csv',
        'views/registration_view.xml',
        'data/question.xml',
        'wizard/message_check_view.xml',
        'wizard/confirm_view.xml',
        'wizard/interview_date_change_view.xml',
        'wizard/end_wizard_view.xml',
        'reports/intern_report_template.xml',
        'reports/intern_report.xml',
        
    ],
     "qweb": [ 
        'static/src/xml/qweb_template.xml',
    ],
    'images': ['static/description/odoo.png'],
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'application': True,
}
