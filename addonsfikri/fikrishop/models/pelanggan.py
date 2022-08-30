from odoo import fields, models, api


class pelanggan(models.Model):
    _name = 'fikrishop.pelanggan'
    _inherit = 'fikrishop.manusia'
    _description = 'Description'

    name = fields.Char(string='nama pelanggan')
    kode_pelanggan = fields.Char(
        string='Kode_pelanggan', 
        required=False)

    pelanggan = fields.One2many(            #pelanggan_ids
        comodel_name='fikrishop.penjualan',
        inverse_name='pelanggan_id',
        string='Kode_Ids',
        required=False)

    alamat = fields.Char(
        string='Alamat',
        required=False)

    no_telepon = fields.Char(               #np_tlpn
        string='No telepon',                #np_tlpn
        required=False)

    
