# -*- coding: utf-8 -*-
# from odoo import http


# class Fikrishop(http.Controller):
#     @http.route('/fikrishop/fikrishop/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fikrishop/fikrishop/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('fikrishop.listing', {
#             'root': '/fikrishop/fikrishop',
#             'objects': http.request.env['fikrishop.fikrishop'].search([]),
#         })

#     @http.route('/fikrishop/fikrishop/objects/<model("fikrishop.fikrishop"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fikrishop.object', {
#             'object': obj
#         })
