from openai import OpenAI
import logging
import requests
import re
import os

class Assistant:
    def __init__(self, api_key:str, gpt_model:str, ydown_apiurl:str,
                 storage_name:str ):
        if api_key is None: raise ValueError
        else: self.api_key = api_key
        self.client = OpenAI(api_key=api_key,
                            #  base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
                             )
        self.gpt_model=gpt_model
        self.messages_prompt = []
        self.ydown_apiurl=ydown_apiurl
        self.storage_name = storage_name
        
        
    def add_message(self, role, content):
        self.messages_prompt.append({"role": role, "content": content})

    def reset_message(self):
        self.messages_prompt =[]

    def translate_tokr(self, sentence:str) -> str:
        try:
            self.add_message("assistant", "Translate the input language into Korean. Provide only the result.")
            self.add_message("user", f"{sentence}")
            bot_response = self.get_text_from_gpt(self.messages_prompt)
        except Exception as e:
            logging.error("Analysis error occurred: Returning default value.")
            bot_response = sentence
        self.reset_message()  # 리셋
        return bot_response

    def get_text_from_gpt(self, prompt):
        response = self.client.chat.completions.create(model=self.gpt_model, temperature=0.1,messages=prompt, timeout=60)
        answer = response.choices[0].message.content
        return answer


    def get_mp3_url(self, url) -> set:
        data = {
            "url": f"{url}",
            "file_type": 'mp3',
            "storage_name" : self.storage_name,
            "options": {
                    'format': 'bestaudio/best',  # 최고 품질의 오디오 다운로드
                    'outtmpl': '%(title)s.%(ext)s',  # 다운로드 파일 이름 포맷
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',  # 오디오 추출 및 변환
                        'preferredcodec': 'mp3',  # mp3로 변환
                        'preferredquality': '128',  # 128kbps로 설정
                    }],
                    'postprocessor_args': [
                        '-ar', '44100',  # 오디오 샘플링 주파수 44.1kHz
                        '-ac', '2',      # 스테레오 설정
                        '-ab', '128k',   # 비트레이트 128kbps
                    ],
                    'noplaylist': True,  # 재생목록 다운로드를 방지
                }
        }
        response = requests.post(self.ydown_apiurl, json=data)
        if response.status_code == 200:
            response_json = response.json()
            # label = response_json['label']
            url = response_json['url']
            return url
        else:
            return None  

       
       

