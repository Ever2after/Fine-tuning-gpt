import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def ft_gpt(chat_history):
    max_tokens = 500
    temperature = 0.1
    response = openai.Completion.create(
        model="davinci:ft-seoul-nat-l-univ:gptjusang-2023-03-20-17-48-09",
        prompt=chat_history,
        temperature=temperature, 
        max_tokens=max_tokens
    )
    answer = response.choices[0]['text']
    return answer

def gpt3(chat_history):
    engine = "text-davinci-003"
    max_tokens = 500
    temperature = 0.1
    response = openai.Completion.create(
        engine=engine, 
        prompt=chat_history,
        temperature=temperature, 
        max_tokens=max_tokens
    )

    answer = response.choices[0]['text']
    return answer