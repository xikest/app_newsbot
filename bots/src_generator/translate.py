import requests

class KakaoTranslate:
    @staticmethod    
    def eng2kor(query):
        url = "https://translate.kakao.com/translator/translate.json"

        headers = {
            "Referer": "https://translate.kakao.com/",
            "User-Agent": "Mozilla/5.0"
        }

        data = {
            "queryLanguage": "en",
            "resultLanguage": "kr",
            "q": query
        }

        resp = requests.post(url, headers=headers, data=data)
        data = resp.json()
        output = data['result']['output'][0][0]
        return output
