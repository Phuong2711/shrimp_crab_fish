# -*- coding: utf-8 -*-
from odoo.http import Controller, route, request
from odoo.tools import config
from .xml_rpc import XmlRPC
import time


class XTableController(Controller):
    @route('/shrimp_crab_fish/get_table_public_data', auth='public', type='json', methods=['GET', 'POST'])
    def get_table_public_info(self, **kwargs):
        result = {'all_bet': [], 'balance': 0,'time': 0}
        bet_line_ids = request.env['x.bet.line'].search_read([], ['user_id', 'bet_result', 'bet_amount'])
        result['all_bet'] = bet_line_ids
        result['time'] = request.env.ref('shrimp_crab_fish.x_table_1').current_time
        result['balance'] = request.env.user.x_balance
        return result

    @route('/shrimp_crab_fish/get_table_result', auth='public', type='json', methods=['GET', 'POST'])
    def get_table_result(self, **kwargs):
        table = request.env.ref("shrimp_crab_fish.x_table_1")
        return {'r1': table.result_1, 'r2': table.result_2, 'r3': table.result_3}



