from requests import post, get

from shared.consts import INBOX, API

class MailManager:
    def __init__(
        self, mail_address):
        self.box = mail_address.split('@')

    
    def check_inbox(
        self):

        api_request = f'{API}?action=getMessage&login={self.box[0]}&domain={self.box[1]}'

        response = get(
            api_request
        ).json()

        if (len(response) == 0):
            return False
        
        else:
            return response
        

    def get_id(
        self, r, n):
        return r[n]['id']


    def read_message(
        self, id):
        
        read_mail = f'{API}?action=readMessage&login={self.box[0]}&domain={self.box[1]}&id={id}'

        response = get(
            read_mail
        ).json()

        return {
            'from': response.get('from'),
            'subject': response.get('subject'),
            'date': response.get('date'),
            'content': response.get('content'),
        }


    def delete_address(
        self):

        data = {
            "action": "deleteMailbox",
            "login": self.box[0],
            "domain": self.box[1]
        }

        request = post(
            INBOX,
            data=data
        )

        
        return True
