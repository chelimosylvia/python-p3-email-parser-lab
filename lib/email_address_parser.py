# your code goes here!
import re

class EmailAddressParser:
    def __init__(self, email_addresses):
        self.email_addresses = email_addresses

    def parse(self):
        parts = re.split(r'[,\s]+', self.email_addresses)
        parsed_emails = []
        for part in parts:
            if '@' in part:
                parsed_emails.append(part)
        return sorted(parsed_emails)