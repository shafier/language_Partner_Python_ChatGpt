import os

# gTTS version 2.5.4
from gtts import gTTS

# for gTTS()
language = 'es'
tld_value = 'es'

def playResponse(answerFromOpenAI):
    try:
        myobj = gTTS(text=answerFromOpenAI, lang=language, slow=False, tld=tld_value)
# the Text to Speech audio is saved under the same directory where the python file is stored
        myobj.save("Test03_response.mp3")
# afplay is the audio software built in for MacBook Pro (MacOS)
        os.system("afplay Test03_response.mp3")
    except:
        pass