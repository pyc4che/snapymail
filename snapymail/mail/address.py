from random import choice
from string import ascii_letters, digits

from shared.config.manager import ConfigManager


class Address:
    def __init__(
        self, config):
        
        self.config = ConfigManager(
            config
        )
        self.domains = self.config.get_data()
        
        self.alhabet = ascii_letters + digits


    def generate_mail(
        self):

        return ''.join(
            choice(self.alhabet) for symbol in range(12)
        ) + '@' + choice(self.domains['list'])
