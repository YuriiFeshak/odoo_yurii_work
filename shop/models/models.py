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
    _description = 'category products'

    name = fields.Char(string="Сategory products")
    products_description = fields.Char(string="Description")

    stock_in = fields.Integer(string='Stock in')
    # def default_get(self, fields):
        # res = super(CategoryProducts, self).default_get(fields)
        # res['name'] = 'Automotive products'
        # return res

class ProductsStore(models.Model):
    _name = 'products.store'
    _description = 'products store'



    products_category_id = fields.Many2one('category.products', string="Products category")
    name = fields.Char(string="Product name")
    model_product = fields.Char(string="Model")
    description_category = fields.Char(related="products_category_id.products_description")
    availability_products = fields.Selection([('availabe_1','In stock'),
                               ('availabe_2', 'Under the order')],
                                string="Availability")
    active = fields.Boolean(string='Active', default=True) #для архівації запису

    description_text_id = fields.Text(string="Product descriptions")
    stock_id = fields.Many2one('add.in.store')
    stock_in = fields.Integer(string='Stock in', related='stock_id.up_stock_in')
    stock_out = fields.Integer(string='Stock Out', related='stock_id.up_stock_out')
    stock_left = fields.Integer(string='Left', related='stock_id.up_stock_left')
    state = fields.Selection([('draft', 'Draft'),
                                ('confirm', 'Confirm'),
                                ('done', 'Done'),
                                ('cancel', 'Cancel')], string='Status', default='draft', readonly=True)
    total_stock = fields.Integer('Total')

    def action_confirm(self):
        self.state ='confirm'


    def test_cron(self):
        value = self.env['products.store'].search([]) #взяти всі занчення
        for rec in value:
            rec.total_stock = rec.stock_in + rec.stock_out

    @api.model
    def add_in_stock_action(self):
        return {
                'type': 'ir.actions.act_window',
                'res_model': 'add.in.store',
                'view_mode': 'form',
                'context': {'default_id': self.id, # потрібно щоб працювала можливість добавляти нові значення в полі
                            'default_up_stock_in': self.stock_in,  #підзавантаження значення в полі
                            'default_up_stock_out': self.stock_out,
                            'default_up_stock_left': self.stock_left,
                            },
                'target': 'new'
        }

    def create_notification(self):
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': 'warning',
                'message': 'Please select only one product',
                'sticky': True,
            }
        }
