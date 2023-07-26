import sys
import time

import wolframalpha
client = wolframalpha.Client('') # Get your API key from wolframalpha.com

import wikipedia

def typingPrint(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.025)

def typingInput(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.025)
    value = input()
    return value

import pyttsx3
engine = pyttsx3.init()

engine.say('My name is JARVIS, Just A Really Very Intelligent System.')
engine.runAndWait()

ans = typingInput('Identify yourself:\n').capitalize().strip()
if ans == 'Brandon': # ENTER YOUR OWN NAME HERE
    engine.say('Hello sir. What can I do for you today?')
    engine.runAndWait()

    while True:
        ans = typingInput('Search:\n').capitalize()
        if ans == 'Exit':
            break
        try:
            wiki_res = wikipedia.summary(ans, sentences=2)
            wolfram_res = next(client.query(ans).results).text
            print('Wolfram says: '+ wolfram_res + '\n\n Wikipedia says: '+
            wiki_res)
            engine.say(wolfram_res)
            engine.runAndWait()
        except wikipedia.exceptions.DisambiguationError:
            wolfram_res = next(client.query(ans).results).text
            print('Wolfram says: '+ wolfram_res)
            engine.say(wolfram_res)
            engine.runAndWait()
        except wikipedia.exceptions.PageError:
            wolfram_res = next(client.query(ans).results).text
            print('Wolfram says: '+ wolfram_res)
            engine.say(wolfram_res)
            engine.runAndWait()
        except:
            wiki_res = wikipedia.summary(ans, sentences=2)
            print('Wikipedia says: '+ wiki_res)
            engine.say(wiki_res)
            engine.runAndWait()

else:
    engine.say('You are not authorized for access.')
    engine.runAndWait()
    time.sleep(1)
    exit()
