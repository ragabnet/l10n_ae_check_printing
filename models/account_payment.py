# -*- coding: utf-8 -*-
# License ROOK FZ LLC Proprietary (https://www.rook.ae/license).
# Copyright 2022 ROOK.ae

from odoo import fields, models, api


class AccountPayment(models.Model):
    _inherit = 'account.payment'

    def _check_fill_line(self, amount_str):
        # TODO: add a check to make sure that the check is printed on ADIB paper
        # add a leading asterisk and ending asterisk to the amount_str
        return ''.ljust(2, '*') + amount_str + ''.rjust(2, '*')

    def _check_build_page_info(self, i, p):
        res = super(AccountPayment, self)._check_build_page_info(i, p)
        # TODO: add a check to make sure that the check is printed on ADIB paper
        res['amount'] = self._check_fill_line('{:,.2f}'.format(float(''.join(filter(str.isdigit, res['amount']))))) if i == 0 else 'VOID'
        return res
