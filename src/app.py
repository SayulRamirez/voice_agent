import keyboard
from audio.audio import Audio

def main(): 
    print("Presiona R para grabar, P para reproducir la última grabación, ESC para salir") 
    audio = Audio() 
    keyboard.on_press_key('r', lambda _: audio.recording()) 
    keyboard.on_press_key('p', lambda _: audio.play()) 
    keyboard.wait('esc') 
    print("Saliendo...") 

if __name__ == "__main__":
    main()