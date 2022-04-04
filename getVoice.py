import speech_recognition as sr
from word2number import w2n  # convert word number to integer number

# finding the version of sr
# print("Verion of the speechRecognition : "+ sr.__version__)

# Recognizing the audio(speech)
r = sr.Recognizer()

# getting voice from Microphone
def getMicVoice():
    with sr.Microphone() as source:
        # print("Say")
        r.adjust_for_ambient_noise(source)     # reducing the noices 
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
           # print(voice_data)
        except Exception as es:
           # voice_data = "Can't Recognized"
            print(es)
    print("Completed getMicVoice ..") 
    print(voice_data)
    return voice_data


def getVoice(v_data):
    vl = False
    v_data = list(v_data.split())
    l = 0
    while l < len(v_data):
        val = v_data[l]
        a_v = ['add', 'plus', 'addition'] # addtion correcting
        if val in a_v:
            v_data[l] = '+'
        else:
            for v in a_v: 
                vl = v in val
                if vl :
                    v_data[l] = '+'
                    vl = False
                else:
                    pass

        s_v = ['minus', 'substraction'] # substrction correcting
        if val in s_v:
            v_data[l] = '-'
        else:
            for v in s_v: 
                vl = v in val
                if vl :
                    v_data[l] = '-'
                    vl = False
                else:
                    pass

        d_v = ['divideby', 'divion', 'divided', 'divide'] # divide correcting
        if val in d_v:
            v_data[l] = '/'
        else:
            for v in d_v: 
                vl = v in val
                if vl :
                    v_data[l] = '/'
                    vl = False
                else:
                    pass

        x_v = ['into', 'indu', 'in 2', 'multiple', 'multipleby', 'multiple by', 'nto', 'ento', 'hindo']
        if val in x_v:                 # multiple correcting
            v_data[l] = 'x'
        else:
            for v in x_v : 
                vl = v in val
                if vl :
                    v_data[l] = 'x'
                    vl = False
                else:
                    pass
        
        try:
            val = w2n.word_to_num(val)
            v_data[l] = val
        except Exception as es :
            pass
        l += 1
    # print(v_data)
    for l_n in range(len(v_data)):
        val = v_data[l_n]
        try:
            if l_n > 0 :
                is_str = isinstance(v_data[l_n - 1], str) 
                is_2str = isinstance(val, str)
                if is_str and is_2str:
                    v_data = "Can't Calculate"
                    break
        except:
            print('String founding error')
        

    # print(v_data)
    return v_data


# getVoice()
