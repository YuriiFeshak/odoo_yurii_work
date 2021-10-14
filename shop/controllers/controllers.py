# -*- coding: utf-8 -*-
# from odoo import http


# class Shop(http.Controller):
#     @http.route('/shop/shop/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/shop/shop/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('shop.listing', {
#             'root': '/shop/shop',
#             'objects': http.request.env['shop.shop'].search([]),
#         })

#     @http.route('/shop/shop/objects/<model("shop.shop"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('shop.object', {
#             'object': obj
#         })
