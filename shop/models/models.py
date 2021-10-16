# -*- coding: utf-8 -*-
import string

from odoo import models, fields, api
from random import randint

class shop(models.Model):
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

class category_products(models.Model):
    _name = 'category.products'


    name_products = fields.Char(string="Name")
    products_description = fields.Char(string="Description")
