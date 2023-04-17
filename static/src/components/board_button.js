/** @odoo-module **/

const { Component } = owl;
import rpc from 'web.rpc';

export default class BoardButton extends Component{
    _onClickBet() {
        let state = this.props.state;
        let bet = state.tempBet;

        for(let key in state.tempBet) {
            if (!bet[key])continue
            rpc.query({
                model: 'x.bet.line',
                method: 'create',
                args: [{
                    'table_id': state.table.id,
                    'user_id': state.user.id,
                    'bet_result': key,
                    'bet_amount': bet[key]
                }],
            })
        }
        this._onClickCancel()
    }
    _onClickCancel () {
        let bet = this.props.state.tempBet;
        for(let item in bet)bet[item] = 0;
    }
}

BoardButton.template = "shrimp_crab_fish.board_button";