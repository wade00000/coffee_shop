from models.Customer import Customer
from models.Coffee import Coffee

if __name__ == "__main__":
    coffee = Coffee("Mocha")
    customer = Customer("Wade")

    order = customer.create_order(coffee, 3.5)

    print(f"Customer {customer.name} ordered {order.coffee.name} for ${order.price}")
    print(f"Total orders for {coffee.name}: {coffee.num_orders()}")

# Create some customers and coffees
c1 = Customer("Wade")
c2 = Customer("Neo")

latte = Coffee("Latte")
drip = Coffee("Drip")

# Create some orders
c1.create_order(latte, 5.5)
c2.create_order(drip, 4.0)
c1.create_order(drip, 4.5)

# See how many orders Wade made
print(f"{c1.name} made {len(c1.orders())} orders")

# What’s the average price for drip coffee?
print(f"Average price for {drip.name}: ${drip.average_price():.2f}")