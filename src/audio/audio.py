from datetime import datetime
import os
import sounddevice as sd
from scipy.io.wavfile import write, read

class Audio:

    SAMPLING_FRECUENCY = 16000 # Hz
    SECONDS = 5

    def __init__(self):
        self.records = []
        self.path_request = os.path.join("./records/request/")
        self.path_response = os.path.join("./records/response/")
        os.makedirs(self.path_request, exist_ok=True)
        os.makedirs(self.path_response, exist_ok=True)

    def recording(self):
        print('Grabando...')
        audio = sd.rec(int(Audio.SECONDS * Audio.SAMPLING_FRECUENCY), Audio.SAMPLING_FRECUENCY, 1, 'int16')
        sd.wait()

        filename = datetime.strftime(datetime.now(), "%d-%m-%Y_%H-%M-%S")

        self.records.append(filename)

        file_path = os.path.join(self.path_request, f"{filename}.wav")

        write(file_path, Audio.SAMPLING_FRECUENCY, audio)
        print('Terminado de grabar')
        return file_path

    def read(self, file_path):
        if os.path.exists(file_path):
            with open(file_path, "rb") as audio_file:
                return audio_file.read()
        return None
   
    def play(self):
        if not self.records:
            print("No hay audio grabado")
        else:
            print('Reproduciendo...')
            rate, audio_search = read(f"{self.path_request}{self.records[-1]}.wav")
            sd.play(audio_search, rate)
            sd.wait()
            print('Fin de audio')

    def save_response(self, audio_content: bytes): 
        """ Guarda la respuesta de la IA (audio binario, por ejemplo de Google TTS) en la carpeta response/ con el mismo timestamp que el último request. """ 
        if not self.records: 
            print("No hay request previo para vincular la respuesta") 
            return 
        
        filename = self.records[-1] # mismo timestamp que el último request 
        filepath = os.path.join(self.path_response, f"{filename}.wav") 
        
        with open(filepath, "wb") as f: 
            f.write(audio_content) 
            print(f"Respuesta guardada en: {filepath}")

        return filename