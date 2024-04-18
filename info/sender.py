class Sender:
    def __init__(self):
        self.profiles = {'token':'5753698180:AAEgXUBlwPeDmRGRGGmt9NpcE3JqyLYrMbU'}
    def get_token(self)->str:
        return self.profiles.get('token')

