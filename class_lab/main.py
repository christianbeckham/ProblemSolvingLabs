from alarm_clock import AlarmClock
from customer import Customer
from product import Product
from cell_phone import CellPhone

print('\nAlarm Clock Tasks')
clock = AlarmClock('9:00am')

print('Current time:', clock.current_time)
clock.set_current_time('11:00am')
clock.set_alarm_time('6:00am')
clock.toggle_alarm_on_or_off()


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

print('\nCell Phone Tasks')
phone = CellPhone('iPhone')

print('Model:', phone.model)

contact_one = phone.add_contact('Ross', '111-222-3333')
contact_two = phone.add_contact('Joey', '111-222-3334')
contact_three = phone.add_contact('Rachel', '111-222-3335')
contact_four = phone.add_contact('Chandler', '111-222-3336')
contact_five = phone.add_contact('Gunther', '111-222-3337')

phone.display_contacts()
phone.incoming_message('Hey, how\'s it going?')
phone.incoming_message('Are you there?')

print('All messages:', phone.messages)
phone.toggle_vibrate_mode()
print(
    f'Current ringer/vibrate setting: {"VIBRATE ON" if phone.vibrate_mode else "RINGER ON"}')

phone.send_message_to_contact('Ross', 'Yo Ross')
