from json import loads

from shared.file import FileManager
from shared.err import FILE_NOT_FOUND


class ConfigManager:
    def __init__(self, path):
        self.config = path

        self.manager = FileManager(
            self.config
        )


    def get_data(self):
        if (self.manager.exists()
            and self.manager.is_file()):

            with open(self.config, 'r') as config_file:
                return loads(config_file.read())

        else:
            raise FILE_NOT_FOUND
