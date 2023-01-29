# Import libraries
import datetime
import speech_recognition as sr
import webbrowser
import wikipedia

from translate import Translate


class Baymax:
    def __init__(self, voice_engine, speech_recognizer):
        self.voice_engine = voice_engine
        self.speech_recognizer = speech_recognizer
        self.translator = Translate()


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
        current_hour = int(datetime.datetime.now().hour)
        if 0 <= current_hour < 12:
            self.speak('Good morning!')
        elif 12 <= current_hour < 18:
            self.speak('Good afternoon!')
        else:
            self.speak('Good evening!')
        self.speak('I hope you are doing well at the moment. You are the best!')


    def translate_sentence(self):
        from_lang = "english"
        self.speak('What sentence do you want to translate?')
        sentence_to_translate = self.listen()
        self.speak('What language do you want to translate to?')
        to_lang = self.listen()
        is_language_undetected = False
        # Chinese Simplified or Traditional
        if to_lang.lower() in ["chinese", "simplified chinese", "traditional chinese", "chinese simplified", "chinese traditional"]:
            to_lang, is_language_undetected = self.translator.translate_chinese(to_lang, is_language_undetected)
        # Native French or Canadian French
        elif to_lang.lower() in ["french", "canadian french", "native french"]:
            to_lang, is_language_undetected = self.translator.translate_french(to_lang, is_language_undetected)
        # Indian Punjabi or Pakistani Punjabi
        elif to_lang.lower() in ["punjabi", "indian", "pakistani"]:
            # TODO
            pass
        # TODO: Continue to translate language here
        else:
            is_language_undetected = True
        if is_language_undetected:
            self.speak('Sorry, that language is not in our database yet. Please try again later!')
        return self.translator.translate_with_ibm_watson(sentence_to_translate, from_lang, to_lang)


    def read_text_from_image(self):
        # TODO
        pass


    def surf_webbrowser(self):
        # TODO
        pass


    def search_wikipedia(self):
        # TODO
        pass