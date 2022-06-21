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
                     