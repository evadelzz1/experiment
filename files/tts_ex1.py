import openai 
import elevenlabs
from queue import Queue

# Set API keys

openai.api_key = "API KEY 여기에 입력"
elevenlabs. set_api_key ("API KEY 여기에 입력")

transcript_result = input("")

# Send the transcript to OpenAI for response generation
response = openai.ChatCompletion.create(
    model = 'gpt-3.5-turbo',
    messages = [
                {"role": "system", "content": ' answer the questions given within a maximum of 30 characters.In perfect sentence'},
                {"role": "user", "content": transcript_result}
            ]
)

text_response = response['choices'][0]['message']['content']


# Convert the response to audio and play it
audio = elevenlabs.generate(
    text=text_response,
    voice="Thomas" # or any voice of your choice
)

print("\nAI:", text_response, end="\r\n")

elevenlabs.play(audio)