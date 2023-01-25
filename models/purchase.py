import logging
from odoo import fields, models, api

_logger = logging.getLogger(__name__)

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    alt_dest_address_id = fields.Many2one('res.partner', compute='_compute_alt_dest_address_id', string='Picking type destination address')
    
    @api.depends('picking_type_id')
    def _compute_alt_dest_address_id(self):
        for po in self:
            _logger.info("setting alt_dest_address_id")
            if po.picking_type_id.destination_location_partner_id:
                po.alt_dest_address_id = po.picking_type_id.destination_location_partner_id
            else:
                po.alt_dest_address_id = False
