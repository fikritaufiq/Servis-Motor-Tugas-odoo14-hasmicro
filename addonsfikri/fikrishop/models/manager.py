from odoo import fields, models, api


class manager(models.Model):
    _inherit = 'res.partner'
    _description = 'Description'

    jabatan = fields.Selection([
        ('manop', 'Manager Operasional'), 
        ('manmar', 'Manager Marketing'),
        ('manak', 'Manager Akuntansi'),
    ], string='Jabatan')