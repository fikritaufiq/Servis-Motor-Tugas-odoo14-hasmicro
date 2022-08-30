from odoo import fields, models, api


class SessionPemograman(models.Model):
    _name = 'fikricourse.sessionpemograman'
    _description = 'Description'
    name = fields.Char(string='Nama')
    nama_kursus = fields.Many2one(
        comodel_name='fikricourse.pemograman',
        string='Nama kursus',
        required=False)
    nama_tutor = fields.Many2one(
        comodel_name='res.partner',
        string='Nama_tutor',
        required=False,
        domain=[('function', '=', 'Tutor Pemograman')])
    tgl_mulai = fields.Datetime(
        string='Tgl Mulai',
        required=False,
        default=fields.Datetime.now())
    peserta_pemograman_ids = fields.One2many(
        comodel_name='fikricourse.pesertapemograman',
        inverse_name='session_id',
        string='Peserta',
        required=False)
    jml_siswa = fields.Integer(
        compute='_compute_peserta',
        string='Jml Siswa',
        required=False)

    @api.model
    def _compute_peserta(self):
        for record in self:
            a = self.env['fikricourse.pesertapemograman'].search([('session_id', '=', record.id)]).mapped(
                'display_name')
            b = len(a)
            record.jml_siswa = b
            record.nama_kursus.jml_siswa_prog = b


class PesertaPemograman(models.Model):
    _name = 'fikricourse.pesertapemograman'
    _description = 'PesertaPemograman'

    name = fields.Char()
    peserta_ids = fields.Many2one(
        comodel_name='res.partner',
        string='Peserta Pemograman',
        required=False,
        domain=[('is_peserta', '=', True), ('jenis_kursus', '=', 'pemograman')])
    session_id = fields.Many2one(
        comodel_name='fikricourse.sessionpemograman',
        string='Session_id',
        required=False)