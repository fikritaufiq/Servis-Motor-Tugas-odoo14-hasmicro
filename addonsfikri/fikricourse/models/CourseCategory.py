from odoo import fields, models, api


class CourseCategory(models.Model):
    _name = 'fikricourse.coursecategory'
    _description = 'Nama Kategori Course'

    name = fields.Char(string='Kategori Kursus')
    kapasitas_kelas = fields.Integer(
        string='Kapasitas kelas',
        required=True)

    level_belajar = fields.Many2one(
        comodel_name='fikricourse.levelcategory',
        string='Level belajar',
        required=True)

    biaya = fields.Integer(compute='_compute_biaya',
        string='Biaya',
        required=False)

    @api.depends('level_belajar')
    def _compute_biaya(self):
        for a in self:
            a.biaya = a.level_belajar.biaya


class Pemograman(models.Model):
    _inherit = 'fikricourse.coursecategory'
    _name = 'fikricourse.pemograman'
    _description = 'ini kelas pemograman'

    name = fields.Char(string='Kategori Kursus')
    startup = fields.Char(
        string='Startup', 
        required=False)
    jml_siswa_prog = fields.Integer(
        string='Jml_siswa_prog',
        required=False)
    kapasitas_sisa = fields.Integer(compute='_compute_sisa',
                                    string='Sisa Kapasitas',
                                    required=False)

    @api.depends('jml_siswa_prog')
    def _compute_sisa(self):
        for record in self:
            record.kapasitas_sisa = record.kapasitas_kelas - record.jml_siswa_prog

class Bahasa(models.Model):
    _inherit = 'fikricourse.coursecategory'
    _name = 'fikricourse.bahasa'
    _description = 'ini kelas bahasa'
    negara_pendamping = fields.Char(
        string='Negara Pendamping',
        required=False)
    jml_siswa_bahasa = fields.Integer(
        string='Jml_siswa_prog',
        required=False)
    kapasitas_sisa = fields.Integer(string='Sisa Kapasitas',
                                    required=False)

    @api.depends('jml_siswa_bahasa')
    def _compute_sisa(self):
        for record in self:
            record.kapasitas_sisa = record.kapasitas_kelas - record.jml_siswa_bahasa

class Keterampilan(models.Model):
    _inherit = 'fikricourse.coursecategory'
    _name = 'fikricourse.keterampilan'
    _description = 'ini kelas keterampilan'
    jenis_keterampilan = fields.Char(
        string='Jenis Keterampilan',
        required=False)
    jml_siswa_ket = fields.Integer(
        string='Jml_siswa_ket',
        required=False)
    kapasitas_sisa = fields.Integer(string='Sisa Kapasitas',
                                    required=False)

    @api.depends('jml_siswa_ket')
    def _compute_sisa(self):
        for record in self:
            record.kapasitas_sisa = record.kapasitas_kelas - record.jml_siswa_ket
