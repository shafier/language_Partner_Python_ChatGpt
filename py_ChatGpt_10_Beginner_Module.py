# Module for English speaker to learn Spanish at Low level

import py_ChatGpt_01_speakToComputerToOpenAI
import py_ChatGpt_02_receiveReplyOpenAiToComputer

converse = ''

def beginner_Spanish_level():
    print("What topic do you want to talk about?")
    while True:
        topic_beginner_Spanish = py_ChatGpt_01_speakToComputerToOpenAI.speakToOpenAI()
        py_ChatGpt_02_receiveReplyOpenAiToComputer.send_receive_reply_OpenAi(topic_beginner_Spanish)
        print("continue the conversation...talk about something")
        converse = py_ChatGpt_01_speakToComputerToOpenAI.speakToOpenAI()
        if 'stop' in converse:
            break
        else:
            py_ChatGpt_02_receiveReplyOpenAiToComputer.send_receive_reply_OpenAi(converse)
