import os
import keyboard
from audio.audio import Audio
from dotenv import load_dotenv
from agent_ai.speech_to_text import SpeechToText
from agent_ai.text_to_speech import TextToSpeech

def main(): 

    load_dotenv() # carga variables desde .env 
    audio = Audio()

    stt = SpeechToText()

    request_audio = audio.recording()

    content = audio.read(request_audio)

    response_text = stt.transcribe(content)

    text = ''
    
    for result in response_text.results:
        text += result.alternatives[0].transcript + ' '
    # keyboard.on_press_key('r', lambda _: audio.recording()) 
    # keyboard.on_press_key('p', lambda _: audio.play()) 
    # keyboard.wait('esc') 
    # print("Saliendo...") 

    # Aquí iria la integración con algun modelo de LLM

    tts = TextToSpeech()

    response = tts.synthesize(text)

    audio_response = audio.write(response)

    audio.play(audio_response)

if __name__ == "__main__":
    main()