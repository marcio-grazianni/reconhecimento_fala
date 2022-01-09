"""
pip install SpeechRecognition
sudo apt install python3-pyaudio
sudo apt install libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0
pip install pyaudio
"""

import speech_recognition as sr
# from pprint import pprint

rec = sr.Recognizer()
# pprint(sr.Microphone().list_microphone_names())
with sr.Microphone() as mic:
    rec.adjust_for_ambient_noise(mic)
    print("Pode falar que eu vou gravar")
    audio = rec.listen(mic)
    texto = rec.recognize_google(audio, language="pt-BR")
    print(texto)
