from odoo import models, fields


class daftarpenjualanexcel(models.AbstractModel):
    _name = 'report.fikrishop.report_penjualan_xlsx'
    _inherit = 'report.report_xlsx.abstract'
    

    def generate_xlsx_report(self, workbook, data, penjualan):
        sheet =  workbook.add_worksheet('laporan Penjualan')
        col = 0
        row = 1
        for obj in penjualan:
            sheet.write(row, col, obj.name)
            sheet.write(row, col, obj.membership)
            row += 1