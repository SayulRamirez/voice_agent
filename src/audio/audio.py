from datetime import datetime
import os
import sounddevice as sd
from scipy.io.wavfile import write, read

class Audio:
    def __init__(self):
        self.records = []
        self.sampling_frecuency = 16000 # Hz
        self.seconds = 5 # Recording duration
        self.path_request = os.path.join("./records/request/")
        self.path_response = os.path.join("./records/response/")
        os.makedirs(self.path_request, exist_ok=True)
        os.makedirs(self.path_response, exist_ok=True)

    def recording(self):
        print('Grabando...')
        audio = sd.rec(int(self.seconds * self.sampling_frecuency), self.sampling_frecuency, 1, 'int16')
        sd.wait()

        self.records.append(datetime.strftime(datetime.now(), "%d-%m-%Y_%H-%M-%S"))

        write(f"{self.path_request}{self.records[-1]}.wav", self.sampling_frecuency, audio)
        print('Terminado de grabar')

    # def play(self):
    #     if not self.records:
    #         print("No hay audio grabado")
    #     else:
    #         print('Reproduciendo...')
    #         rate, audio_search = read(f"{self.path_request}{self.records[-1]}.wav")
    #         sd.play(audio_search, rate)
    #         sd.wait()
    #         print('Fin de audio')

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
    
    def play(self, filepath):
        if not os.path.exists(filepath):
            print("No hay audio grabado")
        else:
            print('Reproduciendo...')
            rate, audio_search = read(filepath)
            sd.play(audio_search, rate)
            sd.wait()
            print('Fin de audio')