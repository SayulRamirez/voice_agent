import os
import keyboard
from audio.audio import Audio
from dotenv import load_dotenv
from agent_ai.speech_to_text import SpeechToText


def main(): 

    load_dotenv() # carga variables desde .env 
    audio = Audio()

    stt = SpeechToText()

    request_audio = audio.recording()

    content = audio.read(request_audio)

    response_text = stt.transcribe(content)

    print("response", response_text)
    for result in response_text.results:
        print(f"Transcript: {result.alternatives[0].transcript}")
    # keyboard.on_press_key('r', lambda _: audio.recording()) 
    # keyboard.on_press_key('p', lambda _: audio.play()) 
    # keyboard.wait('esc') 
    # print("Saliendo...") 

    # print(os.getenv("GOOGLE_APPLICATION_CREDENTIALS"))

if __name__ == "__main__":
    main()