# -*- coding: utf-8 -*-

from odoo import api, fields, models


class CountryCodes(models.Model):
    _name = "country.codes"
    _description = "Country Code"
    _order = "sequence asc, id asc"

    name = fields.Char(string="Name", store=True)
    active = fields.Boolean(default=True)
    country = fields.Many2one("res.country", string="Country", store=True)
    sequence = fields.Integer(string='Sequence', store=True)
    