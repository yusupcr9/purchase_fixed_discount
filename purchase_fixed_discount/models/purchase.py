# Copyright 2017-20 ForgeFlow S.L.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class PurchaseOrderLineInherit(models.Model):
    _inherit = "purchase.order.line"

    discount_fixed = fields.Float(
        string="Discount (Fixed)",
        digits="Product Price",
        help="Fixed amount discount.",
    )

    @api.onchange("discount")
    def _onchange_discount_percent(self):
        # _onchange_discount method already exists in core,
        # but discount is not in the onchange definition
        if self.discount:
            self.discount_fixed = 0.0

    @api.onchange("discount_fixed")
    def _onchange_discount_fixed(self):
        if self.discount_fixed:
            self.discount = 0.0

    @api.constrains("discount", "discount_fixed")
    def _check_only_one_discount(self):
        for line in self:
            if line.discount and line.discount_fixed:
                raise ValidationError(
                    _("You can only set one type of discount per line.")
                )

    @api.depends(
        "product_qty", "discount", "price_unit", "taxes_id", "discount_fixed"
    )
    def _compute_amount(self):
        # vals = {}
        res = super(PurchaseOrderLineInherit, self)._compute_amount()
        for line in self.filtered(
            lambda l: l.discount_fixed and l.order_id.state not in [
                "done", "cancel"]
        ):
            subtot = line.price_unit*line.product_qty
            line.price_subtotal = subtot-line.discount_fixed
        return res

    def _prepare_account_move_line(self, move):
        vals = super(PurchaseOrderLineInherit,
                     self)._prepare_account_move_line(move)
        vals["discount_fixed"] = self.discount_fixed
        return vals


class PurchaseOrderInherit(models.Model):
    _inherit = "purchase.order"

    amount_diskon = fields.Integer(
        string='Total Diskon', compute="_compute_amount_diskon")

    @api.depends('amount_untaxed', 'amount_tax')
    def _compute_amount_diskon(self):
        for i in self:
            subtot = tot_disk = 0
            for line in i.order_line:
                subtot += (line.product_qty*line.price_unit)
            tot_disk = subtot-(i.amount_untaxed+i.amount_tax)
            i.amount_diskon = tot_disk
