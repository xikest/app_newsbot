class Sender:
    def __init__(self):
        self.profiles = {'token':'5753698180:AAHlOqMGw_Pec-lYW6riVWDsCNiDBaybJ8I'}
    def get_token(self)->str:
        return self.profiles.get('token')

