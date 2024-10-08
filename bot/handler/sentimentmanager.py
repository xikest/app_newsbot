import pandas as pd
from openai import OpenAI

class SentimentManager:
    def __init__(self, api_key=None, gpt_model="gpt-3.5-turbo-1106"):
        self.api_key = api_key
        self.aim = AIManager(self.api_key, gpt_model=gpt_model)
        self.messages_prompt = []

    def add_message(self, role, content):
        self.messages_prompt.append({"role": role, "content": content})

    def reset_message(self):
        self.messages_prompt =[]

    def translate_tokr(self, sentence:str) -> str:
        try:
            self.add_message("assistant", "You are a professional journalist, and translate the input language into Korean.")
            self.add_message("user", f"{sentence}")
            bot_response = self.aim.get_text_from_gpt(self.messages_prompt)
        except Exception as e:
            print("Analysis error occurred: Returning default value.")
            bot_response = sentence
        self.reset_message()  # 리셋
        return bot_response





class AIManager:
    def __init__(self, api_key, gpt_model="gpt-3.5-turbo-1106"):
        if api_key is None:
            raise ValueError
        self.client = OpenAI(api_key=api_key)
        self.messages_prompt = []
        self.gpt_model=gpt_model

    def add_message_to_prompt(self, role, content):
        self.messages_prompt.append({"role": role, "content": content})

    def get_text_from_gpt(self, prompt):
        # "gpt-3.5-turbo"
        response = self.client.chat.completions.create(model=self.gpt_model, temperature=0.1,messages=prompt, timeout=60)
        answer = response.choices[0].message.content
        return answer
    def getImageURLFromDALLE(self, user_input):
        response = self.client.images.generate(model="dall-e-3", prompt=user_input,n=1, size="1024x1024", quality="standard")
        image_url = response.data[0].url
        return image_url


    def dataframe_to_text(self,df:pd.DataFrame):
        text = df.to_markdown()
        return text

