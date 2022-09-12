from odoo import fields, models, api


class pemasok(models.Model):
    _name = 'fikrishop.pemasok'
    _inherit = 'fikrishop.manusia'
    _description = 'Description'

    name = fields.Char(
        string='Nama Perusahaan',
        required=False)
#    kode_pemasok = fields.Char(
#        string='Kode_Pemasok',
#        required=False)

#    kode_pembelian_ids = fields.One2many(
#        comodel_name='fikrishop.pembelian',
#        inverse_name='kode_pemasok',
#        string='Kode_Pembelian_ids',
#        required=False)

    alamat = fields.Char(
        string='Alamat',
        required=False)

#    kota = fields.Char(
#        string='Kota',
#        required=False)

#    provinsi = fields.Char(
#        string='Provinsi',
#        required=False)

    pic = fields.Char(
        string='Contact_person',
        required=False)

    no_pic = fields.Char(
        string='No.Telepon',
        required=False)
    
    barang_ids = fields.Many2many(
        comodel_name='fikrishop.barang', 
        string='Supply Barang')
    
    
    

#    no_fax = fields.Char(
#        string='No_fax',
#        required=False)
