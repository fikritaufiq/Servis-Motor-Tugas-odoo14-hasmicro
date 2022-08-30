from odoo import fields, models, api

class PesertaDidik(models.Model):
    _inherit = 'res.partner'
    _description = 'Form peserta didik fikri course'
    jenis_kursus = fields.Selection(selection=[('pemograman', 'Pemograman'), ('bahasa', 'Bahasa'), ('keterampilan', 'Keterampilan')],
        string='Jenis_kursus',
        required=False)
    is_peserta = fields.Boolean(
        string='Peserta',
        required=False)