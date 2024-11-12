from openai import OpenAI

class Summerizer:
    def __init__(self, api_key=None, gpt_model="gpt-3.5-turbo-1106"):
        if api_key is None: raise ValueError
        else: self.api_key = api_key
        self.client = OpenAI(api_key=api_key)
        self.gpt_model=gpt_model
        self.messages_prompt = []

    def add_message(self, role, content):
        self.messages_prompt.append({"role": role, "content": content})

    def reset_message(self):
        self.messages_prompt =[]

    def translate_tokr(self, sentence:str) -> str:
        try:
            self.add_message("assistant", "You are a professional journalist, and translate the input language into Korean.")
            self.add_message("user", f"{sentence}")
            bot_response = self.get_text_from_gpt(self.messages_prompt)
        except Exception as e:
            print("Analysis error occurred: Returning default value.")
            bot_response = sentence
        self.reset_message()  # 리셋
        return bot_response

    def get_text_from_gpt(self, prompt):
        response = self.client.chat.completions.create(model=self.gpt_model, temperature=0.1,messages=prompt, timeout=60)
        answer = response.choices[0].message.content
        return answer

