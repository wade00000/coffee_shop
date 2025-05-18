class Customer:
   all = []

   def __init__(self, name: str):
     self.name = name
     Customer.all.append(self)

   @property
   def name(self):
    return self._name
   
   @name.setter
   def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        if not (1 <= len(value) <= 15):
            raise ValueError("Name must be between 1 and 15 characters")
        self._name = value
   
   def orders(self):
    from .Order import Order
    return [order for order in Order.all if order.customer == self]
   
   def coffees(self):
    return list({order.coffee for order in self.orders()})
   
   def create_order(self, coffee, price):
        from .Order import Order
        new_order = Order(self, coffee, price)
        return new_order
   
   @classmethod
   def most_aficionado(cls,coffee):
       from .Order import Order
       from collections import Counter

       customers = [order.customer for order in Order.all if order.coffee == coffee]
       if not customers:
         return None
      
       return Counter(customers).most_common(1)[0][0]

      

