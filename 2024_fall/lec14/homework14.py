import datetime
import gtts

def what_time_is_it(lang, filename):
    '''
    Tell me what time it is.
    
    Parameters:
    lang (str) - language in which to speak
    filename (str) - the filename into which the audio should be recorded
    '''
    now = datetime.datetime.now()
    time_str = now.strftime("%H:%M")
    text = f"The current time is {time_str}."
    
    tts = gtts.gTTS(text=text, lang=lang)
    tts.save(filename)

    
import random

def tell_me_a_joke(lang, audiofile):
    '''
    Tell me a joke.
    
    @params:
    filename (str) - filename containing the database of jokes
    lang (str) - language
    audiofile (str) - audiofile in which to record the joke
    '''
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "Why don't skeletons fight each other? They don't have the guts!"
    ]
    
    joke = random.choice(jokes)
    tts = gtts.gTTS(text=joke, lang=lang)
    tts.save(audiofile)


def what_day_is_it(lang, audiofile):
    '''
    Tell me what day it is.

    @params:
    lang (str) - language in which to record the date
    audiofile (str) - filename in which to read the date
    
    @returns:
    url (str) - URL that you can look up in order to see the calendar for this month and year
    '''

    now = datetime.datetime.now()
    date_str = now.strftime("%A, %B %d, %Y")
    text = f"Today is {date_str}."
    

    tts = gtts.gTTS(text=text, lang=lang)
    tts.save(audiofile)
    
    url = f"https://www.timeanddate.com/calendar/?year={now.year}&month={now.month}"
    return url


import speech_recognition as sr

def personal_assistant(lang, filename):
    '''
    Listen to the user, and respond to one of three types of requests:
    What time is it?
    What day is it?
    Tell me a joke!
    
    @params:
    lang (str) - language
    filename (str) - filename in which to store the result
    '''
    recognizer = sr.Recognizer()
    
    try:
        with sr.Microphone() as source:
            print("Listening for your request...")
            audio = recognizer.listen(source)
        
        command = recognizer.recognize_google(audio, language=lang).lower()
       
        if "time" in command:
            what_time_is_it(lang, filename)
        elif "day" in command:
            url = what_day_is_it(lang, filename)
            print(f"Here is the calendar link: {url}")
        elif "joke" in command:
            tell_me_a_joke(lang, filename)
        else:
            text = "Sorry, I did not understand your request."
            tts = gtts.gTTS(text=text, lang=lang)
            tts.save(filename)
    
    except sr.UnknownValueError:
        print("Could not understand the audio.")
    except sr.RequestError as e:
        print(f"Request error: {e}")

