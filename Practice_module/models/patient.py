from odoo import api, fields, models

class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital Patient'

    name = fields.Char(string='Name', required=True)
    ref = fields.Char(string='Reference')
    age = fields.Integer(string='Age', compute='age_compute')
    gender = fields.Selection([('male','Male'),
                               ('female','Female'),
                               ], string='Gender')
    date_of_birth = fields.Date(string='Date of Birth')
    image = fields.Image(string='image')
