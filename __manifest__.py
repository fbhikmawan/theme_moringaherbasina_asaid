# -*- coding: utf-8 -*-
# Copyright 2024 ASAid Group Investment - Fatchul Bari Hikmawan
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

{
    'name': 'Theme Moringa Herbasina',
    'summary': "Theme for Moringa Herbasina customer ",
    'description': """
      Moringa Herbasina. We produce, manage and deliver Moringa products for local and export markets. We are committed to deliver the best quality Moringa products to our customers.
    """,

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/17.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Theme',
    'version': '17.0.1.0.0',
    'live_test_url': 'https://www.moringaherbasina.com',

    'author': "ASAid Group Investment",
    'maintainer': 'ASAid Group Investment',
    'website': "https://www.asaidgroup.com",
    "license": "LGPL-3",

    'depends': ['website'],

    'data': [
      'data/ir_asset.xml',
      'views/footer_templates.xml',
      'views/header_templates.xml',
    ],

    'assets': {
      'web.assets_frontend': [
        'https://fonts.googleapis.com/css2?family=Poppins:wght@700&amp;display=swap',
        'https://fonts.googleapis.com/icon?family=Material+Icons',
        'https://use.fontawesome.com/releases/v5.7.0/css/all.css',
        '/theme_moringaherbasina_asaid/static/src/css/modern-normalize.css',
        'https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css',
        '/theme_moringaherbasina_asaid/static/src/css/mixins.scss',
        '/theme_moringaherbasina_asaid/static/src/css/layout.scss',
        'https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js',
        'https://ajax.googleapis.com/ajax/libs/jquery/1.12.0/jquery.min.js',
      ],
    },

    'images': [
      'static/description/banner.png',
      'static/description/theme_screenshot.jpg',
    ],
    
    'installable': True,
    'auto_install': False,
    'application': False,
}
