import json


class ProductsMongoDBModel:

    _id = None
    product_name = None
    product_quantity = None
    data_inregistrare = None

    def __init__(self, **fields):
        self._id = fields.get("id_produs", None)
        self.product_name = fields["product_name"]
        self.product_quantity = fields["product_quantity"]
        self.data_inregistrare = fields.get("data_inregistrare", None)
