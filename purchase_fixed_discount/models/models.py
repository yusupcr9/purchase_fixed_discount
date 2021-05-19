# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class purchase_fixed_discount(models.Model):
#     _name = 'purchase_fixed_discount.purchase_fixed_discount'
#     _description = 'purchase_fixed_discount.purchase_fixed_discount'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
