# -*- coding: utf-8 -*-
{
    'name': "jt_stock_subcontracting",

    'summary': "",

    'description': "",

    'author': "jaco tech",
    'website': "https://jaco.tech",
    "license": "AGPL-3",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'stock',
    'version': '0.18',

    # any module necessary for this one to work correctly
    'depends': ['purchase_stock','mrp_subcontracting_dropshipping'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'report/purchase_report_templates.xml',
        'report/report_deliveryslip.xml',
        'views/purchase_order_views.xml',
        'views/stock_picking_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [

    ],
}
