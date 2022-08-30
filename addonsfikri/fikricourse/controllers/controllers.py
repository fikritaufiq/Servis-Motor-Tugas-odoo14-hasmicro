# -*- coding: utf-8 -*-
# from odoo import http


# class Fikricourse(http.Controller):
#     @http.route('/fikricourse/fikricourse/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fikricourse/fikricourse/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('fikricourse.listing', {
#             'root': '/fikricourse/fikricourse',
#             'objects': http.request.env['fikricourse.fikricourse'].search([]),
#         })

#     @http.route('/fikricourse/fikricourse/objects/<model("fikricourse.fikricourse"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fikricourse.object', {
#             'object': obj
#         })
