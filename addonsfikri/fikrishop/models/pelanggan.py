from odoo import fields, models, api


class pelanggan(models.Model):
    _name = 'fikrishop.pelanggan'
    _inherit = 'fikrishop.manusia'
    _description = 'Description'

    nama_pelanggan = fields.Char(string='ID Member')
    id_member = fields.Char(
        string='Kode Pelanggan', 
        required=False)
    level = fields.Char(string='Level')
    