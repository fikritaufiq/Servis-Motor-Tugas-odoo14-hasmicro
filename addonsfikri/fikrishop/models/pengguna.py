from odoo import fields, models, api


class pengguna(models.Model):
    _name = 'fikrishop.pengguna'
    _description = 'Description'

    userid_ids = fields.One2many(
        comodel_name='fikrishop.pembelian',
        inverse_name='user_id',
        string='UserID Ids',
        required=False)

    id = fields.Char(
        string='Id', 
        required=False)

    passid = fields.Integer(
        string='Passid',
        required=False)

    nama = fields.Char(
        string='Nama',
        required=False)
        
    level = fields.Integer(
        string='Level',
        required=False)