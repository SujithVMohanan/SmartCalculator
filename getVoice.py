import speech_recognition as sr

# finding the version of sr
print("Verion of the speechRecognition : "+ sr.__version__)

# Recognizing the audio(speech)
r = sr.Recognizer()

# getting voice from Microphone
def getMicVoice():
    with sr.Microphone() as source:
        print("Say What you want to calculate")
        r.adjust_for_ambient_noise(source)     # reducing the noices 
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
            print(voice_data)
        except Exception as es:
            voice_data = "Can't Recognized"
            print(es)
    print("Completed getMicVoice ..") 
    return voice_data

getMicVoice()
