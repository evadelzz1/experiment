# source url
# 텍스트를 음성으로 변환하기 : https://scribblinganything.tistory.com/522
# How to Create a Speech Synthesis System with gTTS : https://reintech.io/blog/how-to-create-a-speech-synthesis-system-with-gtts
# Playing and Recording Sound in Python : https://realpython.com/playing-and-recording-sound-python/

# pip install --upgrade wheel    # workaround : https://stackoverflow.com/questions/76078698/why-is-there-an-error-when-i-try-to-install-playsound-module-in-vscode
# pip install playsound
# pip install PyObjC

from gtts import gTTS
from playsound import playsound
import os

# Function to convert text to speech
def text_to_speech(text):
    try:
        tts = gTTS(text=text, lang='en', tld='com', slow=False)
        tts.save("output_en_com.mp3")

        tts = gTTS(text=text, lang='en', tld='co.uk', slow=False)
        tts.save("output_en_couk.mp3")
        
        print("play 1")
        playsound("output_en_com.mp3") # Play the audio file
        print("play 2")
        playsound("output_en_couk.mp3")
    except Exception as e:
        print(f"Error: {str(e)}")

# Get user input
user_text = input("Enter the text you want to convert to speech: ")

# Call the text_to_speech function
text_to_speech(user_text)
