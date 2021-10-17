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

    name = fields.Char(string="Name category products")
    products_description = fields.Char(string="Description")
    # products_id = fields.Many2one('products', string ="product store")

class Products(models.Model):
    _name = 'products.store'
    # _inherit = 'category.products'
    # products_id = fields.Many2one('category.products', string="product store")
    products_category_id = fields.Many2one('category.products',  string="Category")
    name = fields.Char(string="Product name")
    availability_products = fields.Selection([('availabe_1','In stock'),
                               ('availabe_2', 'Under the order')],
                                string="Availability")

    description_text_id = fields.Text(string="Product descriptions")

