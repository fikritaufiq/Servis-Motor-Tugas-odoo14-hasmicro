from odoo import fields, models, api

class barangdatang(models.TransientModel):
    _name = 'fikrishop.barangdatang'

    barang_id = fields.Many2one(
        comodel_name='fikrishop.barang',
        string='Nama Barang',
        required=True)
    
    jumlah = fields.Integer(
        string='Jumlah',
        required=False)
    
    def barang_datang(self):
        for rec in self:
            self.env['fikrishop.barang'].search([('id', '=', rec.barang_id.id)]).write({'stok': rec.barang_id.stok + rec.jumlah})