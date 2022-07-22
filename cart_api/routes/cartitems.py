import falcon
from playhouse.shortcuts import model_to_dict
from cart_api.database import DatabaseCartItem

# Exercise 3:
# Using the database model you created in Exercise 1 create a cartitems route
# CartItems should have a responder for POST and GET
# CartItem should have responders for GET DELETE PATCH
# Your API response statuses and bodies should conform to your OpenAPI spec


class CartItem:
    def on_get(self, req, resp, cart_item_id):
        cart_item = DatabaseCartItem.get(id=cart_item_id)
        resp.media = model_to_dict(cart_item)
        resp.status = falcon.HTTP_200

    def on_delete(self, req, resp, cart_item_id):
        DatabaseCartItem.delete_by_id(cart_item_id)
        resp.status = falcon.HTTP_204

    def on_patch(self, req, resp, cart_item_id):
        obj = req.get_media()
        cart_item = DatabaseCartItem.update(quantity=obj.get('quantity')).where(DatabaseCartItem.id == cart_item_id)
        cart_item.execute()
        resp.status = falcon.HTTP_204


class CartItems:
    def on_get(self, req, resp):
        return_data = []
        cart_items = DatabaseCartItem.select()
        for cart_item in cart_items:
            return_data.append(model_to_dict(cart_item))

        resp.media = return_data
        resp.status = falcon.HTTP_200

    def on_post(self, req, resp):
        obj = req.get_media()
        new_cart_item = DatabaseCartItem(
            name=obj.get('name'),
            image_url=obj.get('image_url'),
            price=obj.get('price'),
            is_on_sale=obj.get('is_on_sale'),
            sale_price=obj.get('sale_price'),
            quantity=obj.get('quantity')
        )
        new_cart_item.save()
        resp.media = model_to_dict(new_cart_item)
        resp.status = falcon.HTTP_201
