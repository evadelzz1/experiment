# source url
# gTTS direct output
# : https://stackoverflow.com/questions/51164040/gtts-direct-output
# How to play mp3 from gTTS as bytes without saving on disk
# : https://blog.furas.pl/python-how-to-play-mp3-from-gtts-as-bytes-without-saving-on-disk-gb.html
#
# Error : Couldn't find ffmpeg or avconv - defaulting to ffmpeg, but may not work warn("Couldn't find ffmpeg or avconv - defaulting to ffmpeg, but may not work", RuntimeWarning) 
# - ffmpeg가 설최되더라도 PATH 설정이 제대로 되지 않았을 때 발생함.
#   1) ffmpeg 파일 찾기
#   sudo find / -name ffmpeg 2>/dev/null
#   2) 환경변수에 설정
#   vi .venv/bin/activate
#   =====================
#   ...
#   export PATH="/Users/daniel/Library/Application Support/ffmpeg-downloader/ffmpeg:$PATH"
#   =====================
#   
# - https://ai-creator.tistory.com/78
# - https://stackoverflow.com/questions/74651215/couldnt-find-ffmpeg-or-avconv-python

# pip install pydub
# pip install ffmpeg
# pip install fmpeg-downloader
# ffdl install --add-path

from gtts import gTTS
from io import BytesIO

def text_to_speech(text):
    try:
        print("# 1) get audio from server")
        tts = gTTS(text=text, lang='en', tld='com', slow=False)

        print("# 2) convert to file-like object")
        fp = BytesIO()
        tts.write_to_fp(fp)

        # --- play it ---
        from pydub import AudioSegment
        from pydub.playback import play

        print("# 3) play audio")
        fp.seek(0)
        song = AudioSegment.from_file(fp, format="mp3")
        play(song)
    except Exception as e:
        print(f"Error: {str(e)}")

# Get user input
user_text = "Hello world! This is a streaming test."

# Call the text_to_speech function
text_to_speech(user_text)



