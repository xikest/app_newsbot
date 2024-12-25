from openai import OpenAI
import logging

class Summerizer:
    def __init__(self, api_key=None, gpt_model="gemini-1.5-flash"):
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

    def get_text_from_gpt(self, prompt):
        response = self.client.chat.completions.create(model=self.gpt_model, temperature=0.1,messages=prompt, timeout=60)
        answer = response.choices[0].message.content
        return answer

