import openai
import os

openai.api_key = os.environ["API_KEY"]

def create_openai_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.3,
        max_tokens=100,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    res_message = response['choices'][0]['text']
    return res_message
