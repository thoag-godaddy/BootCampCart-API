import falcon
from playhouse.shortcuts import model_to_dict
from cart_api.database import DatabaseCartItem


# Exercise 3:
# Using the database model you created in Exercise 1 create a cartitems route
# CartItems should have a responder for POST and GET - Do POST first
# CartItem should have responders for GET DELETE PATCH
# Your API response statuses and bodies should conform to your OpenAPI spec


class CartItems:
    def on_post(self, req, resp):
        new_product = req.get_media()
        new_model = DatabaseCartItem(
            name=new_product["name"],
            price=new_product["price"],
            quantity=new_product["quantity"],
            product_id=new_product["product_id"],
        )
        new_model.save()
        resp.media = model_to_dict(new_model)
        resp.status = falcon.HTTP_201

    def on_get(self, req, resp):
        pass


class CartItem:
    def on_get(self, req, resp):
        pass

    def on_delete(self, req, resp):
        pass

    def on_patch(self, req, resp):
        pass
