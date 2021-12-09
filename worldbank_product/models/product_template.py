from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = "product.template"
    
    full_id_number = fields.Many2one("notenumber.report", string="Full ID Number")
    country = fields.Many2one("res.country", string="Country")
    country_code_from_id = fields.Many2one("country.codes", string="Country Code from ID")
    grade_condition = fields.Char(string="Grade Condition")
    full_code = fields.Char(string="Full Code")
    g = fields.Char(string="G")
    unique_certification_number = fields.Char(string="Unique Certification Number")
    grading_company = fields.Selection(
        [("PMG", "PMG"), ("Other", "Other")],
        store=True,
        default='PMG'
    )       

    def write(self, values):
        if 'name' in values and self.grading_company == 'PMG':
            parsed_barcode = self.parse_barcode(values['name'])
            country_name = self.env['country.codes'].search([('name', '=', parsed_barcode['country_code_from_id'].name)]).country_name
            values.update({
                'full_id_number': parsed_barcode['full_id_number'],
                'country_code_from_id': parsed_barcode['country_code_from_id'],
                'country': country_name,
                'grade_condition': parsed_barcode['grade_condition'],
                'unique_certification_number': parsed_barcode['unique_certification_number'],
                'g': parsed_barcode['g'],
                'full_code': parsed_barcode['full_code'],
            })
        return super(ProductTemplate, self).write(values)

    @api.model_create_multi
    def create(self, vals_list):
        res = super(ProductTemplate, self).create(vals_list)
        if 'name' in res and res.grading_company == 'PMG':
            parsed_barcode = self.parse_barcode(res['name'])
            country_name = self.env['country.codes'].search([('name', '=', parsed_barcode['country_code_from_id'].name)]).country_name
            res.update({
                'full_id_number': parsed_barcode['full_id_number'],
                'country_code_from_id': parsed_barcode['country_code_from_id'],
                'country': country_name,
                'grade_condition': parsed_barcode['grade_condition'],
                'unique_certification_number': parsed_barcode['unique_certification_number'],
                'g': parsed_barcode['g'],
                'full_code': parsed_barcode['full_code'],
            })
        return res

    def parse_barcode(self, barcode):
        parsed_barcode = {}
        full_id = self.env['notenumber.report'].search(
            [('name', '=', barcode[:-14])], 
            limit=1
        )
        if not full_id:
            full_id = self.env['notenumber.report'].create(
                {'name': barcode[:-14]}
            )
        country_code = self.env['country.codes'].search(
            [('name', '=', barcode[:-17])], 
            limit=1
        )
        if not country_code:
            country_code = self.env['country.codes'].create(
                {'name': barcode[:-17]}
            )
        parsed_barcode.update({
            'full_id_number': full_id,
            'country_code_from_id': country_code,
            'grade_condition': barcode[-14:-11],
            'unique_certification_number': barcode[-11:-4] + '-' + barcode[-4:-1],
            'g': barcode[-1],
            'full_code': barcode[:-1],
        })
        return parsed_barcode
