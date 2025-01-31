from openai import OpenAI
import logging
import aiohttp
import asyncio 

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
        max_retries = 2

        for attempt in range(max_retries):
            try:
                async with aiohttp.ClientSession(timeout=timeout) as session:
                    async with session.post(ydown_download_url, json=data) as response:
                        response_text = await response.text()  # 원본 응답 확인
                        logging.debug(f"[get_mp3_url] Attempt {attempt + 1}: Response status {response.status}")
                        logging.debug(f"[get_mp3_url] Attempt {attempt + 1}: Raw response {response_text}")

                        if response.status == 200:
                            try:
                                response_json = await response.json()
                                logging.debug(f"[get_mp3_url] Attempt {attempt + 1}: Parsed JSON {response_json}")

                                label = response_json.get('label')
                                url = response_json.get('url')

                                if label and url:
                                    return label, url
                                else:
                                    logging.error(f"[get_mp3_url] Attempt {attempt + 1}: Missing 'label' or 'url' in response JSON")
                            except ValueError as e:
                                logging.error(f"[get_mp3_url] Attempt {attempt + 1}: Failed to parse JSON response: {str(e)}")
                        
                        else:
                            logging.error(f"[get_mp3_url] Attempt {attempt + 1}: Failed to get URL - {response.status}")

            except TimeoutError as e:
                logging.error(f"[get_mp3_url] Attempt {attempt + 1}: Timeout error: {str(e)}")

            except aiohttp.ClientError as e:
                logging.error(f"[get_mp3_url] Attempt {attempt + 1}: AIOHTTP Client error: {str(e)}")

            except Exception as e:
                logging.error(f"[get_mp3_url] Attempt {attempt + 1}: Unexpected error: {str(e)}")

            # 재시도 전 1초 대기
            if attempt < max_retries - 1:
                logging.info(f"[get_mp3_url] Retrying in 1 second...")
                await asyncio.sleep(1)

        # 모든 시도가 실패했을 경우 최종적으로 None 반환
        logging.error(f"[get_mp3_url] All {max_retries} attempts failed.")
        return None