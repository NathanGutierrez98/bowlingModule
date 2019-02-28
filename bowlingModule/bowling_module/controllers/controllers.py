# -*- coding: utf-8 -*-
from odoo import http

# class BowlingModule(http.Controller):
#     @http.route('/bowling_module/bowling_module/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bowling_module/bowling_module/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('bowling_module.listing', {
#             'root': '/bowling_module/bowling_module',
#             'objects': http.request.env['bowling_module.bowling_module'].search([]),
#         })

#     @http.route('/bowling_module/bowling_module/objects/<model("bowling_module.bowling_module"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bowling_module.object', {
#             'object': obj
#         })