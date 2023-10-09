class Bot_Profiles:

    def __init__(self):
        self.profiles = {'token':'telegram token'} #텔레그램 토큰 작성

    def get_token(self)->str:
        return self.profiles.get('token')

