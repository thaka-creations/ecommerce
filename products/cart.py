from products.models import Product

class Cart:
    #class constructor
    def __init__(self, request, id, quantity, format=None):
        self.session = request.session
        self.cart = self.session.get('cart', False)
        self.id = id
        self.quantity = quantity
        self.product = Product.objects.get(id=self.id)

    #method add-to-cart
    def add_to_cart(self):
        if not self.cart:
            #empty cart
            if int(self.quantity) > self.product.quantity:
                #can't order more than stock
                res = {"message":"You can't order more than what is in stock"}
                return res
            else:
                #items being added to cart
                added_items = { self.id:{"quantity":self.quantity, "price":float(self.product.price)} }
                self.session['cart'] = added_items
                res = {"cart":self.session.get('cart', False), "message":"Item(s) added to cart"}
                return res
        else:
            #not empty cart
            items =  self.session.get('cart', False)
            if self.id in items.keys():
                #if product in cart
                quantity = int(self.quantity) + int(items[self.id]['quantity'])

                if quantity > self.product.quantity:
                    #can't order more than in stock
                    res = {"cart":items, "message":"You can't order more than what is in stock"}
                    return res

                else:
                    items[self.id]["quantity"] = quantity
                    self.session['cart'] = items
                    res = {"cart":self.session.get('cart', False), "message":"Item(s) added to cart"}
                    return res
               
            else:
                #product not in cart
                items = self.session.get('cart',False)
                added_items = {self.id:{"quantity":int(self.quantity), "price":float(self.product.price)}}
                items.update(added_items) #add items to dictionary/updating dict
                self.session['cart'] = items
                res = {"cart":self.session.get('cart',False), "message":"Item(s) added to cart"}
                return res

