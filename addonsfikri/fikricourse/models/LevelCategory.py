from odoo import fields, models, api


class LevelCategory(models.Model):
    _name = 'fikricourse.levelcategory'
    _description = 'Kategori Level Kursus Fikri'

    name = fields.Selection(string='Nama Level',
                       selection=[('beginner', 'Beginner'), ('intermediate', 'Intermediate'),('advanced', 'Advanced')])
    keterangan = fields.Char(string='Keterangan')
    biaya = fields.Integer(
        string='Biaya', 
        required=False)
    course_ids = fields.One2many(
        comodel_name='fikricourse.coursecategory',
        inverse_name='level_belajar',
        string='Daftar Kursus',
        required=False)