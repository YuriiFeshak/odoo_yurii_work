# -*- coding: utf-8 -*-
import string

from odoo import models, fields, api
from random import randint

class shop(models.Model):
    _name = 'shop.shop'
    _description = 'shop.shop'

    # генератор випадкових 13 значних чисел, правда незнаю чи унікальних
    def _generate_number(self):
        range_start = 10**(13-1)
        range_end = (10**13)-1
        return randint(range_start, range_end)
    # поля
    number = fields.Char(default=_generate_number,string = "Номер", required=True, readonly=True)
    # перевірка якщо не унікально згенероване число
    _sql_constraints = [('number_unique', 'unique(number)', 'Згенероване число не унікальне, повтори спробу!')]
    availability = fields.Selection([('availabe1','На складі'),
                               ('availabe2', 'Під замовлення')],
                                string = "Наявність")

class category_product(models.Model):
    _name = 'category.product'

    numb  = fields.Char(string="Назва")
    numb1 = fields.Char(string="Опис")