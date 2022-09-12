from odoo import fields, models, api


class barang(models.Model):
    _name = 'fikrishop.barang'
    _description = 'Description'

    name = fields.Char(
        string='Nama_Barang')

    kode_spec = fields.Char(
        string='Kode Spec')

    kode_barang = fields.Char(
        string='Kode Barang')
    
    produk_id = fields.Many2one(
        comodel_name='fikrishop.produk',
        string='Kode_Produk',
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
    
    jenis = fields.Selection(string='jenis', selection=[('makanan', 'Makanan'), ('minuman', 'Minuman')])
    supplier_ids = fields.Many2many(comodel_name='fikrishop.pemasok', string='Daftar Supplier')

    @api.onchange('produk_id', 'kode_spec')
    def _onchange_produk(self):
        self.kode_barang = str(self.produk_id.kode_produk)+' '+str(self.kode_spec)