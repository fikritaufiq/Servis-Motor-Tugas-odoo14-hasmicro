from odoo import fields, models, api


class produk(models.Model):
    _name = 'fikrishop.produk'
    _description = 'Description produk'
    _rec_name = 'grup_id'


    barang_ids = fields.One2many(
        comodel_name='fikrishop.barang',
        inverse_name='kode_produk',
        string='Kode_Produk_Ids',
        required=False)

    grup_id = fields.Many2one(
        comodel_name='fikrishop.grup',
        string='Kode_Grup',
        required=False)

    nama_produk = fields.Char(
        string='Nama_Produk', 
        required=False)