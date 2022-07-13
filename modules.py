import openai
import os

openai.api_key = os.getenv('API_KEY')

# basic structure of text
# bow = [1...n] where 1 to n represent different topics
# example bow (bag of words) vector -> ["sad", "crying", "mellow"] dimension of 1 with 3 elements

def gpt_prompt(text):
    response = openai.Completion.create(
    model="text-davinci-002",
    prompt=f"given that {text} is the primary topic, produce an image idea that correlates to the ",
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    print(response)