import openai
import os
import random
from dotenv import load_dotenv

# load environment variables
load_dotenv()

openai.api_key = os.getenv('API_KEY')

# basic structure of text
# bow = [1...n] where 1 to n represent different topics
# example bow (bag of words) vector -> ["sad", "crying", "mellow"] dimension of 1 with 3 elements

def gpt_prompt(text):
    index = random.randint(0, len(text))
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=f"what is an image idea that correlates to the following topic: {text[index]}",
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response
    