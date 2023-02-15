# -*- coding: utf-8 -*-
#################################################################################
# Author      : ROOK FZ LLC (<https://rook.ae/>)
# Copyright(c): 2020-Present ROOK.ae
# All Rights Reserved.
#
# This program is copyright property of the author mentioned above.
# You can`t redistribute it and/or modify it.
#
# You should have received a copy of the License along with this program.
# If not, see <https://rook.ae/license/>
#################################################################################
{
    'name': 'UAE Account Check',
    'description':
        """
        This module allows to print your payments on pre-printed check paper for banks in the UAE.
        You can configure the output (layout, stubs information, etc.) in company settings, and manage the
        checks numbering (if you use pre-printed checks without numbers) in journal settings.
        """,
    'summary': 'ADIB Check Printing',
    'category': 'Accounting/Localizations/Check',
    'version': '16.0.1.0.0',
    'author': 'Nabil Mohamed Ali Ragab',
    'company': 'ROOK FZ LLC',
    'maintainer': 'ROOK FZ LLC',
    'website': 'https://www.rook.ae',
    'depends': [
        'l10n_ae',
        'account',
        'account_accountant',
        'account_check_printing',
    ],
    'data': [
        'data/ae_check_printing.xml',
        'report/print_check_adib.xml',
    ],
    'assets':
        {
            'web.report_assets_common': [
                'l10n_ae_check_printing/static/src/scss/report_check_commons.scss',
                'l10n_ae_check_printing/static/src/scss/report_check_adib.scss',
             ],
        },
    'installable': True,
    'application': False,
    'auto_install': ['l10n_ae'],
    'license': 'Other proprietary',
    'images': [
        'static/description/banner.jpg'
    ],
    'currency': 'USD',
    'price': 0.00,
    'support': 'i@rook.ae',

}
