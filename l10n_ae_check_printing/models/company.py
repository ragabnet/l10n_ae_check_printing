# -*- coding: utf-8 -*-
# License ROOK FZ LLC Proprietary (https://www.rook.ae/license).
# Copyright 2022 ROOK.ae

from odoo import models, fields


class Company(models.Model):
    _inherit = "res.company"

    # here, key has to be full xmlID(including the module name) of all the
    # new report actions that you have defined for check layout
    account_check_printing_layout = fields.Selection(selection_add=[
        ('l10n_ae_check_printing.action_print_check_adib', 'Print Check - AE ADIB'),
    ], ondelete={
        'l10n_ae_check_printing.action_print_check_adib': 'set default',
    })
