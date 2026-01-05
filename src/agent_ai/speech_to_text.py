from google.cloud import speech
from audio.audio import Audio

class SpeechToText:

    def __init__(self):
        self.client = speech.SpeechClient()
        self.config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=Audio.SAMPLING_FRECUENCY,
            language_code='es-MX'
        )

    def transcribe(self, audio):
        recognition_audio = speech.RecognitionAudio(content=audio)

        return self.client.recognize(config=self.config, audio=recognition_audio)