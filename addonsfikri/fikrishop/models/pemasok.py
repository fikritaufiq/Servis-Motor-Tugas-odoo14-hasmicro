from odoo import fields, models, api


class pemasok(models.Model):
    _name = 'fikrishop.pemasok'
    _description = 'Description'
    _rec_name = 'kode_pemasok'

    kode_pemasok = fields.Char(
        string='Kode_Pemasok',
        required=False)

    kode_pembelian_ids = fields.One2many(
        comodel_name='fikrishop.pembelian',
        inverse_name='kode_pemasok',
        string='Kode_Pembelian_ids',
        required=False)

    nama_pemasok = fields.Char(
        string='Nama_pemasok',
        required=False)

    alamat = fields.Char(
        string='Alamat',
        required=False)

    kota = fields.Char(
        string='Kota',
        required=False)

    provinsi = fields.Char(
        string='Provinsi',
        required=False)

    no_telepon = fields.Char(
        string='No_telepon',
        required=False)

    no_fax = fields.Char(
        string='No_fax',
        required=False)

    contact_person = fields.Char(
        string='Contact_person',
        required=False)