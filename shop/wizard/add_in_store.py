
# -*- coding: utf-8 -*-

from odoo import models, fields, api



class AddInStore(models.Model): # не може бути TransientModel тоді не працює many2one
    _name = "add.in.store"
    _description = "add in store"

    up_stock_in = fields.Integer(string='Stock in')
    up_stock_out = fields.Integer(string='Stock Out')
    up_stock_left = fields.Integer(string='Left', compute='_compute_up_stock_left', inverse='_inverse_up_stock_left')



    # Розрахунок поля Left
    @api.depends('up_stock_in', 'up_stock_out')
    def _compute_up_stock_left(self):
        if self.up_stock_in > self.up_stock_out:
            self.up_stock_left = self.up_stock_in - self.up_stock_out
        else:
            self.up_stock_left = False

    def _inverse_up_stock_left(self):
        if self.up_stock_left > 0:
            self.up_stock_in = self.up_stock_out + self.up_stock_left
        else:
            self.up_stock_in = False


    # добавлення даних в поля по кнопці add in store
    @api.model
    def create(self, value):
        res = super(AddInStore, self).create(value)
        product = self.env['products.store'].search([('id', '=', self.env.context.get('default_id'))])
        if product:
            product.update({
                'stock_id': res.id
            })
        return res

    # вaріант 2 через кнопку action_add_value( якщо кнопка то тільки може бути один параметр self,без декоратора)
    # def action_add_value(self):
    #     values = {'up_stock_in': self.up_stock_in}
    #
    #     res = self.create(values)
    #     product = self.env['products.store'].search([('id', '=', self.env.context.get('default_id'))])
    #     if product:
    #         product.update({
    #             'stock_id': res.id
    #         })
    #     return res

    # примітивне добавлення даних по кнопці add
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