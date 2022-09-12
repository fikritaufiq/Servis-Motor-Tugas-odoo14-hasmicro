from tarfile import RECORDSIZE
from odoo import fields, models, api
from odoo.exceptions import ValidationError


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
        string='Nama Pelanggan')
    
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

    @api.depends('pelanggan_id')
    def _compute_id_member(self):
        for record in self:
            record.id_member = record.pelanggan_id.nama_pelanggan

    @api.onchange('pelanggan_id')
    def onchange_pelanggan(self):
        if self.pelanggan_id.gender:
            self.gender = self.pelanggan_id.gender
        else:
            self.gender = ""
        
#    @api.ondelete(at_uninstall=False)
#    def _ondelete_penjualandetail(self):
#        if self.detailpenjualan_ids:
#            for rec in self:
#                a = self.env['fikrishop.penjualandetail'].search([('penjualan_id','=',rec.id)])
#                print(a)

    def unlink(self):
        if self.detailpenjualan_ids:
            a=[]
            for rec in self:
                a = self.env['fikrishop.penjualandetail'].search([('penjualan_id','=', rec.id)])
                print(a)
            for i in self:
                print(str(i.barang_id.name) + ' ' + str(i.jumah))
                i.barang_id.stok += i.jumlah
        record = super(penjualan,self).unlink()
        return record

    def write(self, vals):
        for rec in self:
            a = self.env['fikrishop.penjualandetail'].search([('penjualan_id', '=', rec.id)])
            for data in a:
                print(str(data.barang_id.name)+" "+str(data.jumlah)+" "+str(data.barang_id.stok))
                data.barang_id.stok += data.barang_id.stok + data.jumlah
        record = super(penjualan,self).write(vals)
        for rec in self:
            b = self.env['fikrishop.penjualandetail'].search([('penjualan_id', '=', rec.id)])
            print(a)
            print(b)
            for databaru in b:
                if databaru in a:
                    print(str(databaru.barang_id.name)+" "+str(databaru.jumlah))
                    databaru.barang_id.stok += databaru.barang_id.stok - databaru.jumlah
                else:
                    pass
        return record

    _sql_constraints =[
        ('no_nota_unik', 'unique(name)', 'No. Nota harus unik')
    ]

class penjualandetail(models.Model):
    _name = 'fikrishop.penjualandetail'
    _description = 'Description'

    name = fields.Char(string='Nama')

    barang_id = fields.Many2one(
        comodel_name='fikrishop.barang',
        string='Barang',
        required=False)

#    nama_barang_penjualan = fields.Char(
#        compute="_compute_namabarangpenjualan",
#        string='Nama_Barang',
#        required=False)

    harga_satuan = fields.Integer(
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
        string='Penjualan Id',
        required=False)

    satuan = fields.Char(
        compute='_compute_satuan', 
        string='satuan')
    
    @api.onchange('barang_id')
    def _onchange_satuan(self):
        if (self.barang_id.harga_jual):
            self.harga_satuan = self.barang_id.harga_jual
        else:
            self.harga_satuan = ''

    @api.onchange('barang_id')
    def _compute_satuan(self):
        self.satuan = self.barang_id.satuan

    @api.depends('jumlah','harga_satuan')
    def _compute_subtotal(self):
        for record in self:
            record.subtotal = record.jumlah * record.harga_satuan
    
    @api.model
    def create(self, vals):
        record = super(penjualandetail, self).create(vals)
        if record.jumlah:
            self.env['fikrishop.barang'].search([('id','=',record.barang_id.id)]).write({
                'stok':record.barang_id.stok - record.jumlah})
            return record

    @api.constrains('qty')
    def _checkJumlah(self):
        for rec in self:
            if rec.jumlah < 1 :
                raise ValidationError('Mau belanja {} berapa buah...'.format(rec.barang_id.name))
            elif (rec.jumlah > rec.barang_id.stok):
                raise ValidationError('Stok {} tidak cukup, hanya tersedia {} {}'.format(rec.barang_id.name))
