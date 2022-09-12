from tokenize import Name
from odoo import fields, models, api


class pembelian(models.Model):
    _name = 'fikrishop.pembelian'
    _description = 'Description'

    name = fields.Char(string='No. Nota')

    tgl_nota = fields.Datetime(
        string='Tanggal Nota',
        required=False,
        default=fields.Datetime.now())

    kode_pemasok = fields.Many2one(
        comodel_name='fikrishop.pemasok',
        string='kode_Pemasok',
        required=False)

    total = fields.Integer(
        compute='_compute_total',
        string='Total',
        required=False)
    
    detailpembelian_ids = fields.One2many(
        comodel_name='fikrishop.pembeliandetail', 
        inverse_name='pembelian_id', 
        string='List Barang')

    user_id = fields.Many2one(
        comodel_name='fikrishop.pengguna',
        string='User Id',
        required=False)

    @api.depends('detailpembelian_ids')
    def _compute_total(self):
        for record in self:
            a = sum(self.env['fikrishop.pembeliandetail'].search(
                [('pembelian_id', '=', record.id)]).mapped('subtotal'))
            record.total = a

class pembeliandetail(models.Model):
    _name = 'fikrishop.pembeliandetail'
    _description = 'Description'
    #_rec_name = 'kode_pemasok'

    name = fields.Char(
        string='No_masuk')

    barang_id = fields.Many2one(
        comodel_name='fikrishop.barang',
        string='Kode_Barang_Ids',
        required=False)

    harga_satuan = fields.Integer(
        compute="_compute_hargasatuan",
        string='Harga_satuan',
        required=False)

    jumlah = fields.Integer(
        string='Jumlah',
        required=False)

    subtotal = fields.Integer(
        compute="_compute_subtotal",
        string='SubTotal',
        required=False)

    pembelian_id = fields.Many2one(
        comodel_name='fikrishop.pembelian',
        string='No_pembelian',
        required=False)
    
    satuan = fields.Char(
        compute='_compute_satuan', 
        string='satuan')

    @api.depends('barang_id')
    def _compute_satuan(self):
        for record in self:
            record.satuan = record.barang_id.satuan

    @api.model
    def create(self, vals):
        record = super(pembeliandetail, self).create(vals)
        if record.jumlah:
            self.env['fikrishop.barang'].search([('id', '=', record.barang_id.id)]).write({
                'stok': record.barang_id.stok+record.jumlah})
            return record

    @api.depends('barang_id')
    def _compute_hargabeli(self):
        for a in self:
            a.harga_satuan = a.barang_id.harga_satuan

    @api.depends('jumlah','harga_satuan')
    def _compute_subtotal(self):
        for record in self:
            record.subtotal = record.jumlah * record.harga_satuan