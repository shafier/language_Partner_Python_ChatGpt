# PyAudio version 0.2.14, needed because using microphone. Part of SpeechRecognition´s requirement
# SpeechRecognition version 3.12.0
import speech_recognition as sr

r = sr.Recognizer()

answer = ''
query = ''

def speakToOpenAI():
    with sr.Microphone() as source:
        #print("Your response?: ")
        audio = r.listen(source)

    try:
        query = r.recognize_google(audio).lower()
        print(f'user said: {query} ')
    except sr.UnknownValueError:
        print("I do not understand")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    # debugging
    #print(f" return query, what is query: {query}")
    return query
