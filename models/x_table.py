# -*- coding: utf-8 -*-
from odoo import api, fields, models
from time import sleep
from collections import Counter
from .random_result import get_random_result

RUN_FLAG = False


class XTable(models.Model):
    _name = "x.table"
    _description = "X Table"

    name = fields.Char("Name")
    bet_line_ids = fields.One2many("x.bet.line", "table_id")
    time_per_round = fields.Integer("Time per round")
    current_time = fields.Integer("Current time")
    result_1 = fields.Selection([("s", "Shrimp"), ("c", "Crab"),
                                   ("f", "Fish"), ("d", "Deer"),
                                   ("g", "Gourd"), ("r", "Rooster")])
    result_2 = fields.Selection([("s", "Shrimp"), ("c", "Crab"),
                                   ("f", "Fish"), ("d", "Deer"),
                                   ("g", "Gourd"), ("r", "Rooster")])
    result_3 = fields.Selection([("s", "Shrimp"), ("c", "Crab"),
                                   ("f", "Fish"), ("d", "Deer"),
                                   ("g", "Gourd"), ("r", "Rooster")])
    message = fields.Text("Message")
    state = fields.Selection([("o", "Open"), ("c", "Close")])

    @api.model
    def fetch_table_data(self):
        table = self.sudo().env.ref("shrimp_crab_fish.x_table_1")
        return {'id': table.id, 'message': table.message}

    @api.model
    def generate_result(self):
        table = self.sudo().env.ref("shrimp_crab_fish.x_table_1")
        table.result_1, table.result_2, table.result_3 = get_random_result(3)

    @api.model
    def pay_bet_win(self):
        table = self.sudo().env.ref("shrimp_crab_fish.x_table_1")
        results = Counter([table.result_1, table.result_2, table.result_3])
        bet_line_ids = table.bet_line_ids.filtered(lambda l: l.bet_result in results.keys())
        for bet_line in bet_line_ids:
            bet_line.user_id.x_balance += bet_line.bet_amount * (results[bet_line.bet_result] + 1)

    @api.model
    def delete_bet_line(self):
        self.env.cr.execute("DELETE FROM x_bet_line ")

    def countdown(self, current_time):
        self.state = "o"
        while current_time > 0:
            current_time -= 1
            if current_time == 10:
                self.state = "c"
                self.generate_result()
            self.sudo().env.ref("shrimp_crab_fish.x_table_1").current_time = current_time
            sleep(1)
            self.env.cr.commit()
        sleep(4)
        self.pay_bet_win()
        sleep(2)
        self.delete_bet_line()

    def action_start_table(self):
        global RUN_FLAG
        RUN_FLAG = True
        current_time = self.sudo().env.ref("shrimp_crab_fish.x_table_1").time_per_round
        while RUN_FLAG:
            self.countdown(current_time)

    def action_stop_table(self):
        global RUN_FLAG
        RUN_FLAG = False

