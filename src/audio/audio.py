from datetime import datetime
import os
import sounddevice as sd
from scipy.io.wavfile import write, read

class Audio:

    SAMPLING_FRECUENCY = 16000 # Hz
    SECONDS = 5

    def __init__(self):
        self.path_request = os.path.join("./records/request/")
        self.path_response = os.path.join("./records/response/")
        os.makedirs(self.path_request, exist_ok=True)
        os.makedirs(self.path_response, exist_ok=True)

    def recording(self):
        print('Grabando...')
        audio = sd.rec(int(Audio.SECONDS * Audio.SAMPLING_FRECUENCY), Audio.SAMPLING_FRECUENCY, 1, 'int16')
        sd.wait()

        filename = self.create_name_file()

        file_path = os.path.join(self.path_request, f"{filename}.wav")

        write(file_path, Audio.SAMPLING_FRECUENCY, audio)
        print('Terminado de grabar')
        return file_path

    def read(self, file_path):
        print('Leyendo el audio')
        if os.path.exists(file_path):
            with open(file_path, "rb") as audio_file:
                return audio_file.read()
        return None

    def write(self, audio):
        file_path = os.path.join(self.path_response, f"{self.create_name_file()}.wav")

        with open(file_path, "wb") as out:
            out.write(audio.audio_content)
            print("Grabación de respuesta guardada")
        return file_path

    def create_name_file(self):
        return datetime.strftime(datetime.now(), "%d-%m-%Y_%H-%M-%S")
    
    def play(self, path_audio):
        if not os.path.exists(path_audio):
            print(f"No se encontro el audio: {path_audio}")
        else:
            rate, audio = read(path_audio)
            sd.play(audio, rate)
            sd.wait()
            print('Fin del audio')