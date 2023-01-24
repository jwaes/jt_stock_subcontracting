import logging
from odoo import fields, models, api

_logger = logging.getLogger(__name__)

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    @api.onchange('picking_type_id')
    def _onchange_picking_type_id(self):
        if self.picking_type_id.default_location_dest_id.usage != 'customer':
            self.dest_address_id = False
        if self.picking_type_id.destination_location_partner_id:
            self.dest_address_id = self.picking_type_id.destination_location_partner_id

    def _get_destination_location(self):
        self.ensure_one()
        if self.picking_type_id.default_location_dest_id.usage != 'customer':
            self.dest_address_id = False
        if self.picking_type_id.destination_location_partner_id:
            self.dest_address_id = self.picking_type_id.destination_location_partner_id        
        _logger.info("For %s dest_address_id is %s", self.name, self.dest_address_id)
        _logger.info("default_location_dest_id_usage is %s", self.default_location_dest_id_usage)
        return super()._get_destination_location()

    # def _get_destination_location(self):
    #     self.ensure_one()
    #     if self.dest_address_id:
    #         return self.dest_address_id.property_stock_customer.id
    #     if self.picking_type_id.destination_location_partner_id:
    #         return self.picking_type_id.destination_location_partner_id.id
    #     return self.picking_type_id.default_location_dest_id.id            