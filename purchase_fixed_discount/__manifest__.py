# -*- coding: utf-8 -*-
{
    'name': "Purchase Fixed Discount",

    'summary': """
        Fixed Discount on Purchase""",

    'description': """
        Fixed Discount on Purchase. To use this module, you must install Purchase order lines with discounts and Account Fixed Discount by OCA.
        click this link to download require module for dependences : 
        https://apps.odoo.com/apps/modules/13.0/purchase_discount/
        https://apps.odoo.com/apps/modules/13.0/account_invoice_fixed_discount/
    """,

    'author': "Yusup Firmansyah",
    'website': "http://www.jidokasystem.co.id",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['purchase', 'account', 'account_invoice_fixed_discount', 'purchase_discount'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'reports/po_template.xml',
        'views/purchase.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
