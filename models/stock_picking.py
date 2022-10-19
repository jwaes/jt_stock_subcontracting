import logging
from odoo import fields, models, api

_logger = logging.getLogger(__name__)


class PickingType(models.Model):
    _inherit = "stock.picking.type"

    destination_location_partner_id = fields.Many2one(
        'res.partner', 'Default destination partner',
        check_company=True,)

# t-if="o.picking_type_id.code != 'internal' 
#         and (not o.move_ids_without_package or not o.move_ids_without_package[0].partner_id) 
#         and o.picking_type_id.warehouse_id.partner_id">

class Picking(models.Model):
    _inherit = "stock.picking"

    destination_location_partner_id = fields.Many2one(
        'res.partner', 'Destination partner',
        check_company=True,)

    source_location_partner_id = fields.Many2one(
        'res.partner', 'Source partner',
        check_company=True,)

#     @api.model
#     def create(self, vals):
#         res = super(Picking, self).create(vals)
#         if res.picking_type_id.destination_location_partner_id and not res.partner_id:
#             _logger.info("partner_id was not set, found one in the PickingType, setting.")
#             # res.partner_id = res.picking_type_id.destination_location_partner_id
#         return res

#     def write(self, vals):
#         res = super(Picking, self).write(vals)
#         return res