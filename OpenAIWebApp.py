import os
import openai
from flask import Flask
app = Flask(__name__)
@app.route('/')

def trial():
    os.environ['my_secret'] = "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"#API key saved as an environment variable 
    #print(os.getenv('my_secret'))
    openai.organization = "org-lw44KI9m0uVxbXSFSFkSuMvv"#OpenAI org ID
    # Load your API key from an environment variable or secret management service
    openai.api_key = os.getenv('my_secret')
    input = input("Enter what you'd like the AI to do: ")
    response = openai.Completion.create(model="text-davinci-003", prompt=input, temperature=0, max_tokens=100)
    choices = response['choices']
    ai_reply = choices[0].text

    return (print(ai_reply))

