import os

from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
  api_key=os.getenv('GROQ_API_KEY')
)

# Specify the path to the audio file
filename = os.path.dirname(__file__) + "/audio/audio-03.ogg" # Replace with your audio file!

# Open the audio file
with open(filename, "rb") as file:
    # Create a transcription of the audio file
    transcription = client.audio.transcriptions.create(
      file=(filename, file.read()), # Required audio file
      model="whisper-large-v3-turbo", # Required model to use for transcription
      prompt="Specify context or spelling",  # Optional
      response_format="json",  # Optional
      language="br",  # Optional
      temperature=0.0  # Optional
    )
    # Print the transcription text
    print(transcription.text)