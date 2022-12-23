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
        self.voice_engine.say('Hi, I am BayMax, your personal healthcare companion')
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
    engine.setProperty('rate', 175)

    # Set up speech recognizer
    # TODO


    # Set up BayMax
    baymax = BayMax(voice_engine=engine, speech_recognizer=None)
    baymax.greet()


if __name__ == "__main__":
    main()