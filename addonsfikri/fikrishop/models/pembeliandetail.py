from odoo import fields, models, api


class pembeliandetail(models.Model):
    _name = 'fikrishop.pembeliandetail'
    _description = 'Description'
    #_rec_name = 'kode_pemasok'

    no_masuk = fields.Char(
        string='No_masuk',
        required=False)

    kode_barang_ids = fields.Many2one(
        comodel_name='fikrishop.barang',
        string='Kode_Barang_Ids',
        required=False)

    harga_beli = fields.Integer(
        compute="_compute_hargabeli",
        string='Harga_Beli',
        required=False)

    jumlah = fields.Integer(
        string='Jumlah',
        required=False)

    subtotal = fields.Integer(
        compute="_compute_subtotal",
        string='SubTotal',
        required=False)

    no_pembelian = fields.Many2one(
        comodel_name='fikrishop.pembelian',
        string='No_pembelian',
        required=False)

    nama_barang_pembelian = fields.Char(
        compute="_compute_namabarangpembelian",
        string='Nama_barang',
        required=False)

    @api.model
    def create(self, vals):
        record = super(pembeliandetail, self).create(vals)
        if record.jumlah:
            self.env['fikrishop.barang'].search([('id', '=', record.kode_barang_ids.id)]).write({
                'stok': record.kode_barang_ids.stok+record.jumlah})
            return record

    @api.depends('harga_beli')
    def _compute_hargabeli(self):
        for a in self:
            a.harga_beli = a.kode_barang_ids.harga_beli

    @api.depends('nama_barang_pembelian')
    def _compute_namabarangpembelian(self):
        for a in self:
            a.nama_barang_pembelian = a.kode_barang_ids.nama_barang

    @api.depends('subtotal')
    def _compute_subtotal(self):
        for record in self:
            record.subtotal = record.jumlah * record.harga_beli


