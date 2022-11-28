import requests

class Kakao:
    
    def __init__(self, lang:str='en'):
        self._lang=lang
        
    """
    Kakao('text').translate()
    
    """
 
    async def translate(self,text:str): 
                # en to ko 만 지원
                self._text = text
                url = "https://translate.kakao.com/translator/translate.json"

                headers = {
                    "Referer": "https://translate.kakao.com/",
                    "User-Agent": "Mozilla/5.0"
                }

                data = {
                    "queryLanguage": "en",
                    "resultLanguage": "kr",
                    "q": self._text
                }

                resp = requests.post(url, headers=headers, data=data)
                data = resp.json()
                output = data['result']['output'][0][0]
                return output
