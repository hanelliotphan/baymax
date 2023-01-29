from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


class Translate:
    def __init__(self):
        self.IBM_LANGULATOR_API_KEY = 'yNEC2Qu4VKlli_a1aJXE_TM639ExYHGwaIdcYTZzIenF'
        self.IBM_LANGULATOR_URL = 'https://api.us-east.language-translator.watson.cloud.ibm.com/instances/530b60b1-6d4b-4672-a7c3-11aa5a8cfb0a'
        self.api_authenticator = IAMAuthenticator(apikey=self.IBM_LANGULATOR_API_KEY)
        self.translator = LanguageTranslatorV3(version='2018-05-01', authenticator=self.api_authenticator)
        self.translator.set_service_url(self.IBM_LANGULATOR_URL)
        self.language_code_mapping = {
            'arabic': 'ar',
            'basque': 'eu', 'bengali': 'bn', 'bosnian': 'bs', 'bulgarian': 'bg',
            'catalan': 'ca', 'chinese (simplified)': 'zh', 'chinese (traditional)': 'zh-TW', 'croatian': 'hr', 'czech': 'cs',
            'danish': 'da', 'dutch': 'nl',
            'english': 'en', 'estonian': 'et',
            'finnish': 'fi', 'french': 'fr', 'french (canadian)': 'fr',
            'german': 'de', 'greek': 'el', 'gujarati': 'gu',
            'hebrew': 'he', 'hindi': 'hi', 'hungarian': 'hu',
            'irish': 'ga', 'indonesian': 'id', 'italian': 'it',
            'japanese': 'ja',
            'kannada': 'kn', 'korean': 'ko',
            'latvian': 'lv', 'lithuanian': 'lt',
            'malay': 'ms', 'malayalam': 'ml', 'maltese': 'mt', 'marathi': 'mr', 'montenegrin': 'cnr',
            'nepali': 'ne', 'norwegian': 'nb',
            'polish': 'pl', 'portuguese': 'pt', 'punjabi (indian)': 'pa', 'punjabi (pakistani)': 'pa-PK',
            'romanian': 'ro', 'russian': 'ru',
            'serbian': 'sr', 'sinhala': 'si', 'slovak': 'sk', 'slovenian': 'sl', 'spanish': 'es', 'swedish': 'sv',
            'tamil': 'ta', 'telugu': 'te', 'thai': 'th', 'turkish': 'tr',
            'ukrainian': 'uk', 'urdu': 'ur',
            'vietnamese': 'vi',
            'welsh': 'cy'
        }
        self.languages = self.language_code_mapping.keys()


    def speak(self, text_to_speech):
        self.voice_engine.say(text_to_speech)
        self.voice_engine.runAndWait()


    def translate_chinese(self, to_lang, is_language_undetected):
        if to_lang.lower() == "chinese":
            self.speak('There are Simplified Chinese and Traditional Chinese. What would you like to choose?')
            chinese_type = self.listen()
            if "simplified" in chinese_type.lower():
                to_lang = "chinese (simplified)"
            elif "traditional" in chinese_type.lower():
                to_lang = "chinese (traditional)"
            else:
                is_language_undetected = True
        elif to_lang.lower() in ["chinese simplified", "simplified chinese"]:
            to_lang = "chinese (simplified)"
        elif to_lang.lower() in ["chinese traditional", "traditional chinese"]:
            to_lang = "chinese (traditional)"
        else:
            is_language_undetected = True
        return to_lang, is_language_undetected
    

    def translate_french(self, to_lang, is_language_undetected):
        if to_lang.lower() == "french":
            self.speak('There are Native French and Canadian French. Which one would you choose?')
            french_type = self.listen()
            if "native" in french_type.lower():
                to_lang = "french"
            elif "canadian" in french_type.lower():
                to_lang = "french (canadian)"
            else:
                is_language_undetected
        elif to_lang.lower() in ["french canadian", "canadian french"]:
            to_lang = "french (canadian)"
        elif to_lang.lower() in ["french", "native french", "french native", "original french", "french original", "just french"]:
            to_lang = "french"
        else:
            is_language_undetected = True
        return to_lang, is_language_undetected
    

    def translate_punjabi(self, to_lang, is_language_undetected):
        pass # TODO
    

    def translate_with_ibm_watson(self, sentence, from_lang, to_lang):
        if from_lang not in self.languages:
            return 'The language you want to translate from is not in the database. Please choose another language'
        if to_lang not in self.languages:
            return 'The language you want to translate to is not in the database. Please choose another language'
        if from_lang == to_lang:
            return sentence
        else:
            try:
                translate_model = f'{self.language_code_mapping[from_lang]}-{self.language_code_mapping[to_lang]}'
                translation = self.translator.translate(text=self.translator, model_id=translate_model)
                translated_text = translation.get_result()['translations'][0]['translation']
                return translated_text
            except Exception as err:
                return f'Uh oh! Some errors have occurred. Here is the error: {err}'