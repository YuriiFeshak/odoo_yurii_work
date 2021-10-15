# -*- coding: utf-8 -*-

from odoo import models, fields, api
import random

class shop(models.Model):
    _name = 'shop.shop'
    _description = 'shop.shop'

    def _generate_number(self):
        return str(random.randint(0000000000000,9999999999999))
    number = fields.Char(default=_generate_number,string = "Номер", required=True, readonly=True)
    _sql_constraints = [('number_unique', 'unique(number)', 'Згенероване число не унікальне, повтори спробу!')]
    availability = fields.Selection([('availabe1','На складі'),
                               ('availabe2', 'Під замовлення')],
                                string = "Наявність")

