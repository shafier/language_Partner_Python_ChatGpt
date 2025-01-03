import py_ChatGpt_03_playReplyOpenAiToComputer

# openai version 1.58.1
from openai import OpenAI
client = OpenAI(api_key = 'Add your OpenAi API Key --> sk-proj-')

def send_receive_reply_OpenAi(phrase):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=
        [
            {"role": "system",
             "content": "you are a Spanish teacher for user who speaks English, and you are teaching Spanish CEFR A1 level"},
            {"role": "assistant",
             "content": "you reply to the user in Spanish in less than 10 words"},
            {"role": "assistant",
             "content": "you do not translate from English to Spanish"},
            {"role": "user",
             "content": phrase}
        ]
    )
    message = response.choices[0].message.content
    print(f'Play Response from OpenAI: ')
    py_ChatGpt_03_playReplyOpenAiToComputer.playResponse(message)
    print(f'Response from OpenAI:  {message}')

    return message
