from odoo import fields, models, api


class pembelian(models.Model):
    _name = 'fikrishop.pembelian'
    _description = 'Description'
    _rec_name = 'kode_pemasok'

    no_masuk_ids = fields.One2many(
        comodel_name='fikrishop.pembeliandetail',
        inverse_name='no_pembelian',
        string='No Masuk Ids',
        required=False)

    tgl_masuk = fields.Datetime(
        string='Tanggal Masuk',
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

    user_id = fields.Many2one(
        comodel_name='fikrishop.pengguna',
        string='User Id',
        required=False)

    @api.depends('total')
    def _compute_total(self):
        for record in self:
            a = sum(self.env['fikrishop.pembeliandetail'].search(
                [('no_pembelian', '=', record.id)]).mapped('subtotal'))
            record.total = a