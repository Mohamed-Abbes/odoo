from odoo import api, fields, models, _
from odoo.exceptions import ValidationError, UserError


class HospitalDoctors(models.Model):
    _name = "hospital.doctors"
    _inherit = ['mail.thread']
    _description = "Doctors Records"
    _rec_name='dref'
    name = fields.Char(string='Name', required=True, tracking=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('others', 'Others')], string='Gender', tracking=True)
    dref = fields.Char(string='Reference', default=lambda self: _('New'))
    active = fields.Boolean(default="True")

    @api.model_create_multi
    # It makes several records from a list of dictionaries
    def create(self, vals_list):
        for vals in vals_list:
            vals['dref'] = self.env['ir.sequence'].next_by_code('hospital.doctors')
        return super(HospitalDoctors, self).create(vals_list)

    # Getting a value as a compialtion of two field
    def name_get(self):
        res = []
        for rec in self:
            res.append((rec.id, f'{rec.dref}-{rec.name}'))
        return res
