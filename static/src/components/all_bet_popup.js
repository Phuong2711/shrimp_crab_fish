/** @odoo-module **/

const { Component, useState } = owl;

export default class AllBetPopup extends Component{
    setup () {
        super.setup();
        this.state = useState({isShow: true});
    }
    toggle () {
        this.state.isShow = this.state.isShow ? false : true;
    }
}

AllBetPopup.template = "shrimp_crab_fish.all_bet_popup";