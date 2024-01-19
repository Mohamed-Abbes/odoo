from odoo import api, fields, models, _
# Underscore _ above is for translation purpose
from odoo.exceptions import ValidationError, UserError

class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = ['mail.thread']
    _description = "Patient Records"

    name = fields.Char(string='Name', required=True, tracking=True)
    age = fields.Integer(string='Age', tracking=True)
    is_child = fields.Boolean(string="Is child", tracking=True)
    notes = fields.Text(string="Notes")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('others', 'Others')], string='Gender', tracking=True)

    # We add store to store variable in the db
    capitalized_name = fields.Char(string='Capitalized Name', compute='_compute_capitalized_name', store=True)
    ref = fields.Char(string='Reference', default=lambda self: _('New'))
    doctor_id = fields.Many2one('hospital.doctors', string='Doctor')
    tag_ids= fields.Many2many('res.partner.category','hospital_patient_tag_rel','patient_id','tag_id',string="Tags")
    @api.model_create_multi
    # It makes several records from a list of dictionaries
    def create(self, vals_list):
        for vals in vals_list:
            vals['ref'] = self.env['ir.sequence'].next_by_code('hospital.patient')
        return super(HospitalPatient, self).create(vals_list)

    @api.constrains('is_child' , 'age')
    def _check_child_age(self):
        for rec in self:
            if (rec.is_child and rec.age == 0) or rec.age <0:
            # Note that: if rec.is_child is sam as if is_child==True
                raise ValidationError(_("Age has to be valid !"))

    @api.depends('name')
    def _compute_capitalized_name(self):
        # Iterate through self because it has many values
        for rec in self:
            if rec.name:
                rec.capitalized_name = rec.name.upper()
            else:
                rec.capitalized_name = ""


    # Decorator triggered when age change you can specify many fields
    # @api.onchange('age','gender',...)
    @api.onchange('age')
    def _onchange_age(self):
        if self.age <= 10:
            self.is_child = True
        else:
            self.is_child = False

