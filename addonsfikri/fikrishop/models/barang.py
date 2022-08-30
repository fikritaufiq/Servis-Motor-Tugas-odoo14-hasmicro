from odoo import fields, models, api


class barang(models.Model):
    _name = 'fikrishop.barang'
    _description = 'Description'

    
    kode_barang = fields.Char(
        string='Kode_Barang',
        required=False)

    kode_produk = fields.Many2one(
        comodel_name='fikrishop.produk',
        string='Kode_Produk',
        required=False)

    keterangan_produk = fields.Char(
        string='Nama Produk',
        compute="_compute_produk",
        required=False)

    name = fields.Char(
        string='Nama_Barang',
        required=False)

    satuan = fields.Selection(
        string='Satuan',
        selection=[('pcs', 'Pcs'),
                ('unit', 'Unit'),
                ('lot', 'LOT'), ],
        required=False, )

    harga_beli = fields.Integer(
        string='Harga_beli', 
        required=False)

    harga_jual = fields.Integer(
        string='Harga_jual', 
        required=False)

    stok = fields.Integer(
        string='Stok',
        required=False)



    @api.depends('kode_produk')
    def _compute_produk(self):
           for a in self:
            a.keterangan_produk = a.kode_produk.nama_produk



