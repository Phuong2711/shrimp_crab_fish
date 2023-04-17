# -*- coding: utf-8 -*-
from odoo import api, fields, models


class XBetLine(models.Model):
    _name = "x.bet.line"
    _description = "X Bet Line"

    table_id = fields.Many2one("x.table")
    user_id = fields.Many2one("res.users")
    bet_result = fields.Selection([("s", "Shrimp"), ("c", "Crab"),
                                   ("f", "Fish"), ("d", "Deer"),
                                   ("g", "Gourd"), ("r", "Rooster")])
    bet_amount = fields.Float("Bet amount")

    @api.model_create_multi
    def create(self, vals_list):
        if self.sudo().env.ref("shrimp_crab_fish.x_table_1").state == "c":
            return 0
        for val in vals_list:
            self.sudo().env['res.users'].browse(val.get('user_id')).x_balance -= val.get('bet_amount')
        return super(XBetLine, self).create(vals_list)
