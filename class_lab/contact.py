class Contact:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

    def send_text(self, text_message):
        print(f'Sending text to: {self.name} at {self.phone_number}')
        print(f'\tMessage: {text_message}')
