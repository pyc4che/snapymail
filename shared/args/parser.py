from argparse import ArgumentParser


class Arguments:
    def __init__(self):
        self.parser = ArgumentParser(
            prog='',
            description=''
        )



    def add_arguments(self):

        self.parser.add_argument(
            '',
            action=''
        )

        return self.parser.parse_args()
