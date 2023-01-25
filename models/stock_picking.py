import logging
from odoo import fields, models, api

_logger = logging.getLogger(__name__)


class PickingType(models.Model):
    _inherit = "stock.picking.type"

    destination_location_partner_id = fields.Many2one(
        'res.partner', 'Default destination partner',
        check_company=True,)

class Picking(models.Model):
    _inherit = "stock.picking"

    destination_location_partner_id = fields.Many2one(
        'res.partner', 'Destination partner',
        check_company=True,)

    source_location_partner_id = fields.Many2one(
        'res.partner', 'Source partner',
        check_company=True,)
