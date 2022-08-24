from contact import Contact


class CellPhone:
    def __init__(self, model):
        self.model = model
        self.phone_number = '123-456-7890'
        self.contacts = []
        self.messages = []
        self.vibrate_mode = False

    def incoming_message(self, text_message):
        print(f'New incoming message: {text_message}')
        self.messages.append(text_message)

    def toggle_vibrate_mode(self):
        self.vibrate_mode = not self.vibrate_mode
        print(f'Vibrate mode {"ON" if self.vibrate_mode else "OFF"}')

    def send_message_to_contact(self, contact_name, text_to_send):
        for contact in self.contacts:
            if contact.name == contact_name:
                contact.send_text(text_to_send)
                return

        print('Contact does not exist')

    def add_contact(self, name, phone_number):
        new_contact = Contact(name, phone_number)
        self.contacts.append(new_contact)

    def display_contacts(self):
        for contact in self.contacts:
            print(f'Contact: {contact.name} ({contact.phone_number})')
