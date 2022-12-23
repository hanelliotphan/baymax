# Import libraries
import datetime
import os
import pyttsx3
import speech_recognition as sr
import webbrowser
import wikipedia


class BayMax:
    def __init__(self, voice_engine, speech_recognizer):
        self.voice_engine = voice_engine
        self.speech_recognizer = speech_recognizer

    def greet(self):
        self.voice_engine.say('Hello, I am Baymax, your personal healthcare companion. \
            I was alerted to the need for medical attention when you said "Ow!" \
            One the scale of 1 to 10, how would you rate your pain?')
        self.voice_engine.runAndWait()

    def speak(self, text_to_speech):
        self.voice_engine.say(text_to_speech)
        self.voice_engine.runAndWait()

    def listen(self):
        # TODO
        pass 


def main():
    # Set up voice engine
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[14].id)
    engine.setProperty('rate', 180)

    # Set up speech recognizer
    # TODO


    # Set up BayMax
    baymax = BayMax(voice_engine=engine, speech_recognizer=None)
    baymax.greet()


if __name__ == "__main__":
    main()