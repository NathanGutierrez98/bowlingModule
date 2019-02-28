# -*- coding: utf-8 -*-
{
    'name': "bowling_module",

    'summary': """
        Bowling Alley management""",

    'description': """
        Bowling-Module es un módulo de Odoo que nos permite gestionar las pistas de nuestra bolera
        mantenimiento de estas, registro de partidas, usuarios... 
    """,

    'author': "Nathan Gutiérrez Gil",
    'website': "nathangut98@gmail.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Marketplace',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/data.xml'


    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
