# Import libraries
import datetime
import pyttsx3
import speech_recognition as sr
import webbrowser
import wikipedia


class Baymax:
    def __init__(self, voice_engine, speech_recognizer):
        self.voice_engine = voice_engine
        self.speech_recognizer = speech_recognizer

    
    def speak(self, text_to_speech):
        self.voice_engine.say(text_to_speech)
        self.voice_engine.runAndWait()

    
    def listen(self):
        query = None
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1.0
            audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio)
            print(f'Human said: "{query}"\n')
        except Exception as err:
            self.speak("Sorry, I did not catch what you said, please speak again")
            print(err)
        return query

    
    def activate(self):
        self.speak('Hello, I am Baymax, your personal healthcare companion. \
            I was alerted to the need for medical attention when you said..."Ow!"... \
            On the scale of 1 to 10, how would you rate your pain?')
        return True

    
    def deactivate(self):
        self.speak('I am glad you are satisfied. Good bye!')
        return False

    
    def greet(self):
        # TODO
        pass