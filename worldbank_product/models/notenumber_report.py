# -*- coding: utf-8 -*-

from odoo import api, fields, models


class NoteNumberReport(models.Model):
    _name = "notenumber.report"
    _description = "Note Number Report"
    _order = "sequence asc, id asc"

    name = fields.Char(string="Name", store=True)
    active = fields.Boolean(default=True)
    category = fields.Char(string="Category", store=True )
    country = fields.Many2one("res.country", string="Country", store=True, readonly=True)
    country_code = fields.Many2one("country.codes", string="Country Code", store=True)
    denomination = fields.Char(string="Denomination", store=True)
    label_description = fields.Char(string="Label Description", store=True)
    note_type = fields.Char(string="Note Type", store=True)
    sequence = fields.Integer(string='Sequence', store=True)
    series_1 = fields.Char(string="Series1", store=True)
    series_2 = fields.Char(string="Series2", store=True)
    signature_1 = fields.Char(string="Signature1", store=True)
    signature_2 = fields.Char(string="Signature2", store=True)
    signature_3 = fields.Char(string="Signature3", store=True)
    signature_4 = fields.Char(string="Signature4", store=True)
    variety_1 = fields.Char(string="Variety", store=True)
    variety_2 = fields.Char(string="Variety2", store=True)
    variety_3 = fields.Char(string="Variety3", store=True)
    variety_4 = fields.Char(string="Variety4", store=True)
    variety_5 = fields.Char(string="Variety5", store=True)
    variety_6 = fields.Char(string="Variety6", store=True)
    variety_7 = fields.Char(string="Variety7", store=True)
