from odoo.tests.common import TransactionCase

class TestInternship(TransactionCase):
    def test_create_intern(self):
        intern = self.env['internship.registration'].create({
            'name': 'New Intern',
            'supervisor': 'Madam FRANCA',
        })
        self.assertTrue(intern, "Intern creation failed")

    def test_modify_intern(self):
        intern = self.env['internship.registration'].create({
            'name': 'New Intern',
            'supervisor': 'Madam FRANCA',

        })
        intern.name = 'John Smite'
        self.assertEqual(intern.name, 'John Smite', "Intern modification failed")

    def test_delete_intern(self):
        intern = self.env['internship.registration'].create({
            'name': 'New Intern',
            'supervisor': 'Madam FRANCA',

        })
        intern.unlink()
        self.assertFalse(intern.exists(), "Intern deletion failed")