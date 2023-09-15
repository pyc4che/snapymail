from pathlib import Path


class FileManager:
    def __init__(self, path):
        self.path = path

        self.obj = Path(
            self.path
        )


    def exists(self):
        return self.obj.exists()
    

    def is_file(self):
        return self.obj.is_file()
