# -*- coding: utf-8 -*-
{
    'name': "reception",

    'summary': "Le systeme de gestion de la reception",

    'description': """
        Le systeme de gestion de la reception
    """,

    'application': True,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/reception_security.xml',
        'security/ir.model.access.csv',
        'views/client.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

