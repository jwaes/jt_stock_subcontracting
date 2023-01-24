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



        in_bom_products = False
        not_in_bom_products = False
        for order_line in self.order_line:
            _logger.info("Order line  %s", order_line)

            _logger.info("Bom line ids: %s", order_line.product_id.bom_line_ids)

            for bom_line in order_line.product_id.bom_line_ids.filtered(lambda line: line.company_id == self.company_id):
                _logger.info("Bom line %s for %s and contractors %s", bom_line, bom_line.bom_id, bom_line.bom_id.subcontractor_ids)

            if any(bom_line.bom_id.type == 'subcontract' and self.dest_address_id in bom_line.bom_id.subcontractor_ids for bom_line in order_line.product_id.bom_line_ids.filtered(lambda line: line.company_id == self.company_id)):
                in_bom_products = True
                _logger.info("in bom prouct")
            else:
                not_in_bom_products = True
                _logger.info("not in bom prouct")



        dest = super()._get_destination_location()
        _logger.info("after super dest: %s", dest)


        return dest

    # def _get_destination_location(self):
    #     self.ensure_one()
    #     if self.dest_address_id:
    #         return self.dest_address_id.property_stock_customer.id
    #     if self.picking_type_id.destination_location_partner_id:
    #         return self.picking_type_id.destination_location_partner_id.id
    #     return self.picking_type_id.default_location_dest_id.id            