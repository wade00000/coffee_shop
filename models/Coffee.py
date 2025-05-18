class Coffee:
    all = []
    def __init__(self, name: str):
        self.name = name
        Coffee.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,value):
        if isinstance(value, str) and len(value) >= 3:
            self._name = value
        else:
            raise ValueError("Coffee name must be a string with at least 3 characters.")
        

    def orders(self):
        from .Order import Order 
        return [order for order in Order.all if order.coffee == self]

    def customers(self):
         """Return a list of unique customers who ordered this coffee."""
         return list({order.customer for order in self.orders()})
    
    def num_orders(self):
        return len(self.orders())
    
    def average_price(self):
        orders = [order.price for order in self.orders()]
        if not orders:  
            return 0.0
        return sum(orders) / len(orders)

