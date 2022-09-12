from odoo import fields, models, api


class produk(models.Model):
    _name = 'fikrishop.produk'
    _description = 'Description produk'


    name = fields.Char(
        string='Nama_Produk', 
        required=False)
    
    kode_spec = fields.Char(string='Kode Spec')

    kode_produk = fields.Char(
        string='Kode Produk',
        onchange='_onchange_grup')

    barang_ids = fields.One2many(
        comodel_name='fikrishop.barang',
        inverse_name='produk_id',
        string='ID Barang',
        required=False)

    grup_id = fields.Many2one(
        comodel_name='fikrishop.grup',
        string='Grup')

    pelanggan_id = fields.Many2one(
        comodel_name='fikrishop.pelanggan', 
        string='Pelanggannya')

    @api.onchange('grup_id','kode_spec')
    def _onchange_grup(self):
        if (self.grup_id.kode_grup):
            self.kode_produk = str(self.grup_id.kode_grup) +' '+ str(self.kode_spec)
        else:
            self.kode_produk = ""
