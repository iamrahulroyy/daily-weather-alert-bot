import json
from twilio.rest import Client

class WhatsAppMessenger:
    def __init__(self, account_sid, auth_token, from_number, to_number):
        self.client = Client(account_sid, auth_token)
        self.from_number = from_number
        self.to_number = to_number

    def send_template(self, content_sid: str, variables: dict):
        return self.client.messages.create(
            from_=self.from_number,
            content_sid=content_sid,
            content_variables=variables,
            to=self.to_number
        )

    def send_message(self, message: str):
        return self.client.messages.create(
            body=message,
            from_=self.from_number,
            to=self.to_number
        )
