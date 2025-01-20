from openai import OpenAI
import whisper
import os
import logging
import json
import yt_dlp

class Assistant:
    def __init__(self, api_key=None, gpt_model="gemini-2.0-flash-exp"):
        if api_key is None: raise ValueError
        else: self.api_key = api_key
        self.client = OpenAI(api_key=api_key,
                             base_url="https://generativelanguage.googleapis.com/v1beta/openai/")
        self.gpt_model=gpt_model
        self.messages_prompt = []

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

    def translate_summary(self, sentence:str) -> str:
        try:
            self.add_message("assistant", "Make a summary considering the main topic in Korean. Provide only the result.")
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


    def get_text_from_video_yt(self, url):     
        model = whisper.load_model("large")
        file_type = "mp4"
        json_path = "./json/yt_options.json"  # 옵션 파일 경로
        
        with open(json_path, 'r', encoding='utf-8') as file:
            options = json.load(file)
            
        with yt_dlp.YoutubeDL(options.get(file_type)) as ydl:
            result = ydl.extract_info(url, download=True)
            file_name = ydl.prepare_filename(result)
            file_name = file_name.replace(".webm", f".{file_type}")
        print(f"File exists: {os.path.exists(file_name)}")
        try:
            if file_name:
                result = model.transcribe(file_name) 
                os.remove(file_name)
                script = result["text"]  
                script = self.translate_summary(script)
                return script
            else:
                return None
        except Exception as e:
            return None


