from odoo import api, fields, models
from datetime import date

class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital Patient'

    name = fields.Char(string='Name', required=True)
    ref = fields.Char(string='Reference', default='New')
    age = fields.Integer(string='Age', compute='age_compute')
    gender = fields.Selection([('male','Male'),
                               ('female','Female'),
                               ], string='Gender')
    date_of_birth = fields.Date(string='Date of Birth')
    image = fields.Image(string='image')
    appointment_id = fields.Many2one('hospital.appointment', string='Appointments')
    tag_id = fields.Many2many('patient.tag', string='Tags')


    @api.onchange('date_of_birth')
    def age_compute(self):
        today = date.today()
        for rec in self:
            if rec.date_of_birth:
                rec.age = today.year - rec.date_of_birth.year
            else:
                rec.age = 0
