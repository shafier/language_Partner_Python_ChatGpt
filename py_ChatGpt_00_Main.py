
import py_ChatGpt_10_Beginner_Module

# PyAudio version 0.2.14, needed because using microphone. Part of SpeechRecognition´s requirement
# SpeechRecognition version 3.12.0
import speech_recognition as sr

r = sr.Recognizer()

while True:
    answer = ''
    query = ''

    with sr.Microphone() as source:
        print("Which Spanish level are you? Beginner, Intermediate, or Advance?")
        audio = r.listen(source)

    try:
      query = r.recognize_google(audio).lower()
      print(query)
    except sr.UnknownValueError:
      print("I do not understand")
    except sr.RequestError as e:
      print("Could not request results from Google Speech Recognition service; {0}".format(e))

    if 'beginner' in query:
        py_ChatGpt_10_Beginner_Module.beginner_Spanish_level()

    if "exit" in query:
        break