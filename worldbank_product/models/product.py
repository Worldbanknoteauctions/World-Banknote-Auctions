from odoo import models, fields, api


class ProductProduct(models.Model):
    _inherit = "product.product"
    
    full_id_number = fields.Many2one("notenumber.report", string="Full ID Number")
    country_code_from_id = fields.Many2one("country.codes", string="Country Code from ID")
    country = fields.Many2one("res.country", string="Country")
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
            parsed_barcode = self.env['product.template'].parse_barcode(values['name'])
            values.update({
                'full_id_number': parsed_barcode['full_id_number'],
                'country_code_from_id': parsed_barcode['country_code_from_id'],
                'grade_condition': parsed_barcode['grade_condition'],
                'unique_certification_number': parsed_barcode['unique_certification_number'],
                'g': parsed_barcode['g'],
                'full_code': parsed_barcode['full_code'],
            })
        return super(ProductProduct, self).write(values)

    @api.model_create_multi
    def create(self, vals_list):
        res = super(ProductProduct, self).create(vals_list)
        if 'name' in res and res.grading_company == 'PMG':
            parsed_barcode = self.env['product.template'].parse_barcode(res['name'])
            res.update({
                'full_id_number': parsed_barcode['full_id_number'],
                'country_code_from_id': parsed_barcode['country_code_from_id'],
                'grade_condition': parsed_barcode['grade_condition'],
                'unique_certification_number': parsed_barcode['unique_certification_number'],
                'g': parsed_barcode['g'],
                'full_code': parsed_barcode['full_code'],
            })
        return res

