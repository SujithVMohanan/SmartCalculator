import time
from gtts import gTTS
import playsound
from getVoice import getVoice, getMicVoice
from operation import callOpr
import os
import random


audio_file = 'no.mp3'
def speak(audio_str):
    try:
        tts = gTTS(text=audio_str, lang='en')
        r = random.randint(1, 1000000)
        audio_file = 'audio-'+str(r)+'.mp3'
        tts.save(audio_file)
        playsound.playsound(audio_file)
        print(audio_str)
        os.remove(audio_file)
    except Exception as es:
        print(es)


def respond(voice_data, val):
    if ('what is your name' or 'what is this') == voice_data:
        speak("I am appu , the Calculator, do you want to calculate something")
    elif 'hello' == voice_data:
        speak('Hello sir. do you want calculate something ')
    elif 'yes' == voice_data:
        speak('Ok sir, Please calculate')
    elif 'please wait' == voice_data:
        time.sleep(60)
        speak('I waited one second do you want to continue yes or no')
        res = getMicVoice()
        if res == 'yes' : 
            saySomething()
        elif res == 'no':
            speak('Thank you sir')

    elif ("Can't Calculate please check values you given " or "Can't Recognized") == voice_data :
        speak('Check Values you given again')
        saySomething() 
    else:
        speak(voice_data + 'is equal to ' + str(val))



speak("I am appu , the Calculator, do you want to calculate something Sir Say yes or no")
def saySomething():
    responsed = 'yes'
    if responsed ==  'yes':
        speak('Calculate')
        responsed = getMicVoice()
        time.sleep(1)
        r_rs = ''
        for rs in responsed:
            r_rs =r_rs + str(rs)
        val = callOpr(responsed)
        respond(str(r_rs), val)
    else:
        respond(responsed[0], '')

saySomething()
            