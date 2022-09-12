from odoo import fields, models, api


class kasir(models.Model):
    _name = 'fikrishop.kasir'
    _inherit = 'fikrishop.manusia'
    _description = 'Description'

    id_pegawai = fields.Char(
        string='ID Pegawai')

    status_pegawai = fields.Selection([
        ('kontrak', 'Kontrak'),
        ('tetap', 'Pegawai Tetap'),
        ('magang', 'Pegawai Magang')],string='status_pegawai')