import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import pyjokes
import datetime

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def run_alexa():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_sphinx
            command = command.lower()
            print(command)

            if 'alexa' in command:
                command = command.replace('alexa', '')

            if 'play' in command:
                song = command.replace('play', '')
                talk('playing ' + song)
                pywhatkit.playonyt(song)

            elif 'time' in command:
                time = datetime.datetime.now().strftime('%I:%M %p')
                print(time)
                talk('Current time is ' + time)

            elif 'who the heck is' in command:
                person = command.replace('who the heck is', '')
                info = wikipedia.summary(person, 1)
                print(info)
                talk(info)

            elif 'date' in command:
                talk('Sorry, I have a headache')

            elif 'are you single' in command:
                talk('I am in a relationship with Google')

            elif 'joke' in command:
                talk(pyjokes.get_joke())

            else:
                talk('Please say the command again.')

    except sr.UnknownValueError:
        talk('Sorry, I did not understand that')

    except sr.RequestError:
        talk('Sorry, I am experiencing technical difficulties')

while True:
    run_alexa()
