from openai import OpenAI
import logging
import aiohttp

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

    async def get_mp3_url(self, url) -> set:
        yt_type = 'mp3'
        data = {
            "url": f"{url}",
            "file_type": f"{yt_type}",
            "storage_name" : self.storage_name 
        }
        
        ydown_download_url = self.ydown_apiurl+"/download/"
        
        timeout = aiohttp.ClientTimeout(total=None)  
        try:
            async with aiohttp.ClientSession(timeout=timeout) as session:
                async with session.post(ydown_download_url, json=data) as response:
                    if response.status == 200:
                        response_json = await response.json()
                        return response_json.get('label'), response_json.get('url')
                    else:
                        print(f"Error: Received status code {response.status}")
                        return None
        except aiohttp.ClientError as e:
            print(f"Request failed: {e}")
            return None
        
