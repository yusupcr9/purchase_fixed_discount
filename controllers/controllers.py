# -*- coding: utf-8 -*-
# from odoo import http


# class PurchaseFixedDiscount(http.Controller):
#     @http.route('/purchase_fixed_discount/purchase_fixed_discount/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/purchase_fixed_discount/purchase_fixed_discount/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('purchase_fixed_discount.listing', {
#             'root': '/purchase_fixed_discount/purchase_fixed_discount',
#             'objects': http.request.env['purchase_fixed_discount.purchase_fixed_discount'].search([]),
#         })

#     @http.route('/purchase_fixed_discount/purchase_fixed_discount/objects/<model("purchase_fixed_discount.purchase_fixed_discount"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('purchase_fixed_discount.object', {
#             'object': obj
#         })
