from google.cloud import texttospeech
class TextToSpeech:

    def __init__(self):
        self.client = texttospeech.TextToSpeechClient()
        self.voice = texttospeech.VoiceSelectionParams(
            language_code="es-Mx",
            ssml_gender=texttospeech.SsmlVoiceGender.FEMALE
        )

        self.audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.LINEAR16
        )

    def synthesize(self, text):
        synthesis_input = texttospeech.SynthesisInput(text=text)

        return self.client.synthesize_speech(
            input=synthesis_input,
            voice=self.voice,
            audio_config=self.audio_config
        )

