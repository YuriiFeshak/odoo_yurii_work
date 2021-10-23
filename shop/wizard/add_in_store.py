
# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AddInStore(models.TransientModel):
    _name = "add.in.store"
    _description = "add.in.store"

    up_stock_in = fields.Integer(string='Stock in')
    up_stock_out = fields.Integer(string='Stock Out')
    up_left_field = fields.Integer(string='Left')

    # добавлення даних в поля по кнопці add in store
    def update_fields(self):
        self.env['products.store'].browse(self._context.get('active_ids', [])).create({'stock_in': self.up_stock_in})
        return True
         # vals = {
         #     'stock_in': self.up_stock_in,
         #     'stock_out': self.up_stock_out
         # }
         # self.env['products.store'].create(vals)

