from odoo import http, models, fields
from odoo.http import request
import json

class Fikrishop(http.Controller):
    @http.route('/fikrishop/getbarang', auth='public', method=['GET'])
    def getBarang(self, **kw):
        barang = self.env['fikrishop.barang'].search([])
        isi = []
        for b in barang:
            isi.append({
                'nama_barang' : b.name,
                'hrg_jual' : b.hrg_jual,
                'stok' : b.stok
            })
        return json.dumps(isi)
    
    @http.route('/fikrishop/getpemasok', auth='public', method=['GET'])
    def getPemasok(self, **kw):
        pemasok = request.env['fikrishop.produk'].search([])
        pem = []
        for p in pemasok:
            pem.append({
                'nama_perusahaan' : p.name,
                'alamat' : p.alamat,
                'no_telepon' : p.no_pic,
                'barang' : p.barang_id[0].name
            })
        return json.dumps(pem)