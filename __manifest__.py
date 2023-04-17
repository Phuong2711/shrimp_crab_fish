# -*- coding: utf-8 -*-
{
    'name': 'Shrimp Crab Fish',
    'website': 'https://www.facebook.com/dev.Phuong2711/',
    'summary': 'Vietnamese Traditional Game',
    'author': 'Phuong2711',
    'version': '16.0.1.2',
    'license': 'LGPL-3',
    'support ': 'Dev.Phuong2711@gmail.com',
    'depends': ['base'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/x_table_data.xml',
        'views/res_users_view.xml',
        'views/x_cashmove_views.xml',
        'views/x_table_views.xml',
        'views/dashboard_views.xml',
        'views/menu.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'shrimp_crab_fish/static/src/components/*.xml',
            'shrimp_crab_fish/static/src/components/*.js',
            'shrimp_crab_fish/static/src/scss/*.scss',
        ],
    },
    'installable': True,
    'application': True,
}
