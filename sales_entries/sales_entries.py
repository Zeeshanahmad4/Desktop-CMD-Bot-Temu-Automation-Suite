import imaplib
import email
from email.parser import BytesParser
import json
import logging
from .common_utils import load_configuration

class SalesEntryProcessor:
    def __init__(self, config_path):
        self.config = load_configuration(config_path)
        self.mail = self.setup_email_client()

    def setup_email_client(self):
        """Set up and return an IMAP client connected and logged in to the email server."""
        mail = imaplib.IMAP4_SSL(self.config['email_server'], self.config['email_port'])
        mail.login(self.config['email_username'], self.config['email_password'])
        return mail

    def fetch_emails(self):
        """Fetch new order emails from the specified mailbox."""
        self.mail.select(self.config['email_folder'])  # Connect to the inbox
        status, message_ids = self.mail.search(None, 'UNSEEN')
        messages = []
        for num in message_ids[0].split():
            typ, data = self.mail.fetch(num, '(RFC822)')
            for response_part in data:
                if isinstance(response_part, tuple):
                    msg = BytesParser().parsebytes(response_part[1])
                    messages.append(msg)
        return messages

    def extract_order_details(self, email_message):
        """Extract order details from email messages."""
        # Here, you would implement your specific logic to extract and parse order data
        # This is an example assuming the order data is in the email body as JSON
        email_body = email_message.get_payload(decode=True)
        order_data = json.loads(email_body)
        return order_data

    def create_accounting_entry(self, order_data):
        """Create accounting entries based on extracted order data."""
        # Implement integration with accounting software API here
        logging.info(f"Creating accounting entry for order ID: {order_data['order_id']}")

    def process_new_orders(self):
        """Process all new order emails."""
        logging.info("Checking for new order emails...")
        messages = self.fetch_emails()
        for msg in messages:
            order_data = self.extract_order_details(msg)
            self.create_accounting_entry(order_data)

# Example usage
config_path = 'path_to/email_config.json'  # Adjust the path as necessary
sales_processor = SalesEntryProcessor(config_path)
sales_processor.process_new_orders()
