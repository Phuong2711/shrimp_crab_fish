# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class ResUsers(models.Model):
    _inherit = 'res.users'
    _sql_constraints = [
        ('check_x_balance_not_negative', 'CHECK(x_balance >= 0.0)', _("The balance cannot be negative."))
    ]

    x_balance = fields.Float("Balance", readonly=True)

    @api.model
    def fetch_user_data(self):
        user = self.env.user
        return {'id': user.id, 'name': user.name, 'balance': user.x_balance}
