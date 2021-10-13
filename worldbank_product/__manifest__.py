# -*- coding: utf-8 -*-
{
    'name': "World Banknote Auctions : Product Information from Barcode",
    'summary': 'Update product information when barcode is scanned',
    'sequence': 100,
    'license': 'OEEL-1',
    'website': 'https://www.odoo.com',
    'version': '1.1',
    'author': 'Odoo Inc',
    'description': """
        Task ID: 2643330
        - Populate fields on product with information from a barcode when it is scanned.
    """,
    'category': 'Custom Development',

    # any module necessary for this one to work correctly
    'depends': ['product'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/product_template_views.xml',
        'views/notenumber_report_views.xml',
        'views/country_codes_views.xml',
        'views/product_product_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}