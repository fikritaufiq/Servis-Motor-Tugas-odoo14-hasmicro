from odoo import fields, models, api


class grup(models.Model):
    _name = 'fikrishop.grup'
    _description = 'Description'
    _rec_name = 'nama_grup'

    kode_grup = fields.Char(string='kode Grup')
    
    nama_grup = fields.Char(
        string='Nama_Grup', 
        required=False)

    produk_ids = fields.One2many(
        comodel_name='fikrishop.produk',
        inverse_name='grup_id',
        string='Kode Grup Ids',
        required=False)

    