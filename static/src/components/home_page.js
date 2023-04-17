/** @odoo-module **/


const { Component, useState, onWillStart, onWillUnmount } = owl;
import rpc from 'web.rpc';
import ajax from "web.ajax";
import { registry } from "@web/core/registry";
import PlayerDetail from "./player_detail";
import MessageMarquee from "./message_marquee";
import CircleCountdown from "./circle_countdown";
import GameBoard from "./game_board";
import BoardButton from "./board_button";
import AllBetPopup from "./all_bet_popup";
export default class HomePage extends Component{
    setup () {
        super.setup();
        this.state = useState({
            user: {id: -1, userName: "", balance: ""},
            table: {
                id: false,
                message: "",
                currentTime: -1,
                r1: 'u',
                r2: 'u',
                r3: 'u'

            },
            tempBet: {s:0, c:0, f:0, d:0, g:0, r:0},
            allBet: []

        });
        onWillStart( async ()=>{
            return Promise.all([this._fetch_table_data(), this._fetch_user_data(), this._fetch_table_result()])
        });
        this.refreshTableData = setInterval(this._fetch_table_current_time.bind(this), 800);
        this.refreshResultData = setInterval(this._fetch_table_result.bind(this), 7000);
        onWillUnmount(()=>{
            clearInterval(this.refreshTableData);
            clearInterval(this.refreshResultData);
        })
    }
    async _fetch_table_data () {
        let table = this.state.table;
        let result = await rpc.query({
            model: 'x.table',
            method: 'fetch_table_data',
            args: []});
        table.id = result['id'];
        table.message = result['message'];
    }
    async _fetch_user_data () {
        let user = this.state.user;
        let result = await rpc.query({
            model: 'res.users',
            method: 'fetch_user_data',
            args: []});

        user.id = result['id'];
        user.userName = result['name'];
        user.balance = result['balance'];
    }
    async _fetch_table_current_time () {
        let state = this.state;
        let result = await ajax.jsonRpc('/shrimp_crab_fish/get_table_public_data', 'call', {});
        state.table.currentTime = result['time'];
        state.allBet = result['all_bet'];
        state.user.balance = result['balance']
    }
    async _fetch_table_result () {
        let table = this.state.table;
        let result = await ajax.jsonRpc('/shrimp_crab_fish/get_table_result', 'call', {});
        table.r1 = result['r1'];
        table.r2 = result['r2'];
        table.r3 = result['r3'];
    }
}

HomePage.template = "shrimp_crab_fish.home_page";
HomePage.components = { PlayerDetail, MessageMarquee, CircleCountdown, GameBoard, BoardButton, AllBetPopup};

registry.category("actions").add("shrimp_crab_fish", HomePage);