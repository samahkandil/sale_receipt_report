{
    "name": "Sale Receipt Report",

    'version': "16.0",
    'license': 'LGPL-3',
    'category': 'Sales',

    "summary": "Sales Receipt Report",

    'author': "Samah Knadil",
    
    'website': 'https://www.linkedin.com/in/samah-kandil-odoo',
    'support': 'samahqandeel22@gmail.com',

    "depends": [
        'base',
        'sale',
    ],

    "data": [
        "views/sale_receipt_report.xml",
        # "views/report.xml",

    ],

    'images': ['static/description/banner.png'],
    'installable': True,
    'application': True,
    'auto_install': False,

}
