# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class XCashMove(models.Model):
    _name = "x.cashmove"
    _order = "create_date desc"

    user_id = fields.Many2one("res.users", required=True, default=lambda self: self.env.user, readonly=True)
    amount = fields.Float("Amount", states={'wait': [('readonly', True)], 'approved': [('readonly', True)], 'rejected': [('readonly', True)]})
    image = fields.Binary("Image", states={'wait': [('readonly', True)], 'approved': [('readonly', True)], 'rejected': [('readonly', True)]})
    reason = fields.Text("Reason")
    state = fields.Selection([("draft", "Draft"), ("wait", "Wait auditing"), ("approved", "approved"), ("rejected", "Rejected")], default="draft", readonly=True, string="State")

    def unlink(self):
        for record in self:
            if record.state != "draft":
                raise ValidationError(_("You only can delete record in draft state!"))
        super().unlink()

    def name_get(self):
        return [(self.id, f'{self.user_id.name} [{self.amount:,}]')]

    def action_send_request(self):
        for rec in self:
            if rec.state != "draft":
                return
            rec.state = "wait"

    def action_approve(self):
        for rec in self:
            if rec.state != "wait":
                return
            rec.user_id.x_balance += rec.amount
            rec.state = "approved"

    def action_reject(self):
        for rec in self:
            if rec.state != "wait":
                return
            rec.state = "rejected"

    def action_back_to_draft(self):
        for rec in self:
            if rec.state != "rejected":
                return
            rec.reason = False
            rec.state = "draft"

    def open_reject_popup(self):
        for rec in self:
            if rec.state != "wait":
                return

            return {
                'type': 'ir.actions.act_window',
                'name': _('Reject request'),
                'res_model': 'x.cashmove',
                'views': [(self.env.ref('shrimp_crab_fish.x_cashmove_reject_view_form').id, 'form')],
                'res_id': rec.id,
                'target': 'new'
            }

