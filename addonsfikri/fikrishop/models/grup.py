from odoo import fields, models, api


class grup(models.Model):
    _name = 'fikrishop.grup'
    _description = 'Description'
  
    name = fields.Selection([
        ('makanan', 'Makanan'),
        ('minuman', 'Minuman'),
    ], string='Nama Grup', ondelete='cascade')

#    name = fields.Char(string='Nama Grup')
    kode_grup = fields.Char(string='Kode Grup')

    @api.onchange('name')
    def _onchange_namagrup(self):
        if (self.name == 'makanan'):
            self.kode_grup = 'mak0123'
        elif (self.name == 'minuman'):
            self.kode_grup = 'min0123'

    produk_ids = fields.One2many(
        comodel_name='fikrishop.produk',
        inverse_name='grup_id',
        string='Produk-produk',
        required=False)
    

    