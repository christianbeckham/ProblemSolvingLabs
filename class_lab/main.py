from alarm_clock import AlarmClock
from customer import Customer
from product import Product

# print('\nAlarm Clock Tasks')
# clock = AlarmClock('9:00am')

# print('Current time:', clock.current_time)
# clock.set_current_time('11:00am')
# clock.set_alarm_time('6:00am')
# clock.toggle_alarm_on_or_off()


print('\nCustomer Shopping Cart Tasks')

customer_one = Customer('Fred')
print('\nCustomer name:', customer_one.name)

candy = Product('Snickers', '1.50', 'candy')
drink = Product('Fiji water', '5.00', 'beverage')
shirt = Product('T-Shirt', '20', 'clothing')

customer_one.add_product(candy)
customer_one.add_product(drink)
customer_one.add_product(shirt)

print('\nProducts in cart:')
customer_one.view_products()
total_items_in_cart = customer_one.cart.get_total_products_in_cart()
print('\nTotal items in cart:', total_items_in_cart)

customer_one.cart.empty_cart()
total_items_in_cart = customer_one.cart.get_total_products_in_cart()
print('Total items in cart:', total_items_in_cart)
