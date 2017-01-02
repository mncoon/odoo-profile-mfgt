# -*- coding: utf-8 -*-
# This file is part of Odoo. The COPYRIGHT file at the top level of
# this module contains the full copyright notices and license terms.
{
    'name': 'Profile MFGT Online Team',
    'version': '9.0.0.1.0',
    'author': 'Hucke Media GmbH & Co. KG/IFE GmbH',
    'category': 'Custom',
    'website': 'https://www.hucke-media.de/',
    'licence': 'AGPL-3',
    'summary': 'Customizations for MFGT',
    'depends': [
        'report',
        'sale',
        'purchase',
    ],
    'data': [
        'report/layouts.xml',
        'report/report_saleorder.xml',
        'report/report_purchasequotation.xml',
        'views/res_partner_views.xml',
    ],
    'installable': True,
    'application': False,
}
