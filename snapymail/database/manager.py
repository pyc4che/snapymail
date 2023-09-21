from sqlite3 import connect

from shared.err import FILE_NOT_FOUND


class Database:
    def __init__(self, database):
        self.path = database
    
        try:
            self.connection = connect(
                self.path
            )

        except:
            print(FILE_NOT_FOUND)


    def create_cursor(self):
        self.cursor = self.connection.cursor()


    def create_address_table(self):
        self.connection.execute(
            f'''
            CREATE TABLE IF NOT EXISTS emails (
                id INTEGER PRIMARY KEY,
                address TEXT NOT NULL,
                domain TEXT NOT NULL
            )
            '''
        )

    def select_addresses(self):
        self.cursor.execute(
            '''
            SELECT * FROM emails
            '''
        )

        return self.cursor.fetchall()



    def create_email_table(self, address):
        self.connection.execute(
            f'''
            CREATE TABLE IF NOT EXISTS {address} (
                id INTEGER PRIMARY KEY,
                from TEXT NOT NULL,
                subject TEXT NOT NULL,
                date TEXT NOT NULL,
                content TEXT NOT NULL
            )
            '''
        )


    def select_data(self, address):
        self.connection.execute(
            f'''
            SELECT * FROM {address}
            '''
        )
