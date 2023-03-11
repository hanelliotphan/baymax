# Import libraries
from baymax import Baymax
import pyttsx3


def main():
    # Set up voice engine
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[14].id)
    engine.setProperty('rate', 180)

    # Set up BayMax
    baymax = Baymax(voice_engine=engine, speech_recognizer=None)
    is_activated = False

    # Baymax listens and responds
    while True:
        what_human_said = baymax.listen()
        if "ow" or "ouch" in what_human_said.lower():
            is_activated = baymax.activate()
            continue
        elif "satisfied with my care" in what_human_said.lower():
            is_activated = baymax.deactivate()
            break
        if is_activated:
            baymax.simple_chat(what_human_said)


if __name__ == "__main__":
    main()