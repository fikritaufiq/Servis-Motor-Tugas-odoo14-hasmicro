from odoo import fields, models, api


class manusia(models.Model):
    _name = 'fikrishop.manusia'
    _description = 'Description'

    name = fields.Char(
        string='Nama', 
        required='True')
    
    gender = fields.Selection([('male', 'Male'),
                ('female', 'Female')], 
                string='Gender',
                required='True')

    alamat = fields.Char(string='Alamat')

    no_telepon = fields.Char(               #np_tlpn
        string='No telepon',                #np_tlpn
        required=False)