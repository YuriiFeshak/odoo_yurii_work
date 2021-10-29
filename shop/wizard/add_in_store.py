
# -*- coding: utf-8 -*-

from odoo import models, fields, api

class AddInStore(models.Model): # не може бути TransientModel тоді не працює many2one
    _name = "add.in.store"
    _description = "add in store"

    # stock_id = fields.Many2one('products.store', string='Product Name')
    up_stock_in = fields.Integer(string='Stock in')
    # up_stock_out = fields.Integer(string='Stock Out', related='name_id.stock_in')
    # up_left_field = fields.Integer(string='Left(Not edited)')

    # добавлення даних в поля по кнопці add in store
    @api.model
    def action_add_value(self, value):
        res = super(AddInStore, self).create(value)
        product = self.env['products.store'].search([('id', '=', self.env.context.get('default_id'))])
        if product:
            product.update({
                'stock_id': self.id
            })
        return res

    # def update_fields(self):
    #     # self.env['products.store'].search(self.context.get('default_id'))\
    #     self.env['products.store'].search([('id', '=', self.env.context.get('default_id'))]).update({
    #         'stock_in': self.up_stock_in,
    #         # 'stock_out': self.up_stock_out,
    #     })
    #     return True

    # @api.model
    # def default_get(self, fields):
    #     res = super(AddInStore, self).default_get(fields)
    #     res['stock_id'] = self.env.context['default_id']
    #     return res