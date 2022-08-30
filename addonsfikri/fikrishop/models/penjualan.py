from odoo import fields, models, api


class penjualan(models.Model):
    _name = 'fikrishop.penjualan'
    _description = 'New Description'

    membership = fields.Boolean(string='Apakah member')
    name = fields.Char(string='No. Nota')
    nama_nonmember = fields.Char(string='Nama')
    id_member = fields.Char(
        compute='_compute_id_member', 
        string='ID Member')
#    no_nota_ids = fields.One2many(
#        comodel_name='fikrishop.penjualandetail',
#        inverse_name='no_nota',
#        string='No Penjualan ids',
#        required=False)

    tgl_nota = fields.Datetime(
        string='Tanggal Nota',
        required=True,
        default=fields.Datetime.now())

    total_bayar = fields.Integer(
        compute="_compute_totalbayar",
        string='Total_bayar')

    detailpenjualan_ids = fields.One2many(
        comodel_name='fikrishop.penjualandetail', 
        inverse_name='penjualan_id', 
        string='List Barang')
    
    pelanggan_id = fields.Many2one(
        comodel_name='fikrishop.pelanggan',
        string='Kode Pelanggan')
    
    @api.depends('pelanggan_id')
    def _compute_id_member(self):
        for record in self:
            record.id_member = record.pelanggan_id.kode_pelanggan
    
    gender = fields.Selection([('male', 'Male'),
                ('female', 'Female')], 
                string='Gender',
                required='True')

    @api.depends('detailpenjualan_ids')
    def _compute_totalbayar(self):
        for record in self:
            a = sum(self.env['fikrishop.penjualandetail'].search(
                [('penjualan_id', '=', record.id)]).mapped('subtotal'))
            record.total_bayar = a

class penjualandetail(models.Model):
    _name = 'fikrishop.penjualandetail'
    _description = 'Description'

    name = fields.Char(string='No Nota')

    barang_id = fields.Many2one(
        comodel_name='fikrishop.barang',
        string='Barang',
        required=False)

#    nama_barang_penjualan = fields.Char(
#        compute="_compute_namabarangpenjualan",
#        string='Nama_Barang',
#        required=False)
    harga_satuan = fields.Integer(
        compute="_compute_hargasatuan",
        string='Harga_satuan',
        required=False)

    jumlah = fields.Integer(
        string='Jumlah',
        required=False)

    subtotal = fields.Integer(
        compute="_compute_subtotal",
        string='subtotal',
        required=False)

    penjualan_id = fields.Many2one(
        comodel_name='fikrishop.penjualan',
        string='Penjualan',
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
        record = super(penjualandetail, self).create(vals)
        if record.jumlah:
            self.env['fikrishop.barang'].search([('id','=',record.barang_id.id)]).write({
                'stok':record.barang_id.id.stok-record.jumlah})
            return record


    @api.depends('barang_id')
    def _compute_hargasatuan(self):
        for a in self:
            a.harga_satuan = a.barang_id.harga_jual

    @api.depends('jumlah','harga_satuan')
    def _compute_subtotal(self):
        for record in self:
            record.subtotal = record.jumlah * record.harga_satuan

