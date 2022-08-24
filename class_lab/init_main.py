from alarm_clock import AlarmClock
from customer import Customer
from product import Product
from cell_phone import CellPhone


class InitMain:
    def __init__(self):
        self.clock = AlarmClock('9:00am')
        self.customer = Customer('Fred')
        self.phone = CellPhone('iPhone')

    def run_all_methods(self):
        print('\nAlarm Clock Tasks')
        print('Current time:', self.clock.current_time)
        self.clock.set_current_time('11:00am')
        self.clock.set_alarm_time('6:00am')
        self.clock.toggle_alarm_on_or_off()

        print('\nCustomer Shopping Cart Tasks')
        print('\nCustomer name:', self.customer.name)

        candy = Product('Snickers', '1.50', 'candy')
        drink = Product('Fiji water', '5.00', 'beverage')
        shirt = Product('T-Shirt', '20', 'clothing')

        self.customer.add_product(candy)
        self.customer.add_product(drink)
        self.customer.add_product(shirt)

        print('\nProducts in cart:')
        self.customer.view_products()
        total_items_in_cart = self.customer.cart.get_total_products_in_cart()
        print('\nTotal items in cart:', total_items_in_cart)

        self.customer.cart.empty_cart()
        total_items_in_cart = self.customer.cart.get_total_products_in_cart()
        print('Total items in cart:', total_items_in_cart)

        print('\nCell Phone Tasks')
        print('Model:', self.phone.model)

        self.phone.add_contact('Ross', '111-222-3333')
        self.phone.add_contact('Joey', '111-222-3334')
        self.phone.add_contact('Rachel', '111-222-3335')
        self.phone.add_contact('Chandler', '111-222-3336')
        self.phone.add_contact('Gunther', '111-222-3337')

        self.phone.display_contacts()
        self.phone.incoming_message('Hey, how\'s it going?')
        self.phone.incoming_message('Are you there?')

        print('All messages:', self.phone.messages)
        self.phone.toggle_vibrate_mode()
        print(
            f'Current ringer/vibrate setting: {"VIBRATE ON" if self.phone.vibrate_mode else "RINGER ON"}')

        self.phone.send_message_to_contact('Ross', 'Yo Ross')
