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


    def insert_address_data(
        self, address, domain):
        self.cursor.execute(
            '''
            INSERT INTO emails (address, domain)
            VALUES (?, ?)
            ''', (address, domain)
        )


    def delete_address_data(self, address, id):
        self.cursor.execute(
            f'''
            DELETE from emails
            WHERE id = ?,
            DROP TABLE {address}
            ''', (id,)
        )
        
        self.connection.commit()



    def insert_email_data(
        self, address,
        from_, subject, date, content):

        self.cursor.execute(
            f'''
            INSERT INTO {address} (from, subject, date, content)
            VALUES (?, ?, ?, ?)
            ''', (from_, subject, date, content)
        )

        self.connection.commit()


    def delete_email_data(self, address, id):
        self.cursor.execute(
            f'''
            DELETE from {address}
            WHERE id = ?
            ''', (id,)
        )
