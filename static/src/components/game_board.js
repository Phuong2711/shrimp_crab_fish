/** @odoo-module **/

const { Component } = owl;

export default class GameBoard extends Component{
    _onClickDeer() {
        this.props.state.tempBet.d += 1000;
    }
    _onClickShrimp() {
        this.props.state.tempBet.s += 1000;
    }
    _onClickCrab() {
        this.props.state.tempBet.c += 1000;
    }
    _onClickFish() {
        this.props.state.tempBet.f += 1000;
    }
    _onClickGourd() {
        this.props.state.tempBet.g += 1000;
    }
    _onClickRooster() {
        this.props.state.tempBet.r += 1000;
    }
}

GameBoard.template = "shrimp_crab_fish.GameBoard";