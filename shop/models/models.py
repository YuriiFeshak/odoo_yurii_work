# -*- coding: utf-8 -*-
import string

from odoo import models, fields, api
from random import randint

class Shop(models.Model):
    _name = 'shop.shop'
    _description = 'shop.shop'

    # генератор випадкових 13 значних чисел, правда не унікальних
    def _generate_number(self):
        range_start = 10**(13-1)
        range_end = (10**13)-1
        return randint(range_start, range_end)
    # поля
    number = fields.Char(default=_generate_number, string="Number", required=True, readonly=True)
    # перевірка якщо не унікально згенероване число
    _sql_constraints = [('number_unique', 'unique(number)', 'The generate number must be unique, try again!')]
    availability = fields.Selection([('availabe_1','In stock'),
                               ('availabe_2', 'Under the order')],
                                string="Availability")

class CategoryProducts(models.Model):
    _name = 'category.products'

    name = fields.Char(string="Сategory products", )
    products_description = fields.Char(string="Description")

    # def default_get(self, fields):
        # res = super(CategoryProducts, self).default_get(fields)
        # res['name'] = 'Automotive products'
        # return res

class ProductsStore(models.Model):
    _name = 'products.store'
    # _inherit = 'category.products'

    products_category_id = fields.Many2one('category.products',  string="Name products")
    name = fields.Char(string="Product name")
    availability_products = fields.Selection([('availabe_1','In stock'),
                               ('availabe_2', 'Under the order')],
                                string="Availability")

    description_text_id = fields.Text(string="Product descriptions")
    stock_in = fields.Integer(string='Stock in', readonly=True)
    stock_out = fields.Integer(string='Stock Out', readonly=True)
    left_field = fields.Integer(string='Left', readonly=True, compute='_compute_left')

    # Розрахунок поля Left
    @api.depends('stock_in', 'stock_out')
    def _compute_left(self):
        if self.stock_in > self.stock_out:
            self.left_field = self.stock_in - self.stock_out
        else:
            self.left_field = False
