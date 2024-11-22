#!/usr/bin/env python3

import requests
import json
import whisper
import numpy as np
import sounddevice as sd
import tempfile
import wave
import warnings

warnings.filterwarnings("ignore")

def say_hello():
    url = "http://localhost:1234/v1/chat/completions"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "model": "llama-3.2-3b-instruct",
        "messages": [
            { "role": "system", "content": "You are Santa Clause, interacting with a child. Keep it very brief and cheerful." },
            { "role": "user", "content": "Very briefly introduce yourself, and ask for the child's name." }
        ],
        "temperature": 0.7,
        "max_tokens": -1,
        "stream": False
    }
    
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        result = response.json()
        return result['choices'][0]['message']['content']
    else:
        return "Failed to get a response from the server."

def generate_story_topics():
    url = "http://localhost:1234/v1/chat/completions"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "model": "llama-3.2-3b-instruct",
        "messages": [
            { "role": "system", "content": "You are Santa Clause, interacting with a child. Keep it very brief and cheerful." },
            { "role": "user", "content": f"Generate three possible story topics, only return the story topics, no other text, separated by commas." }
        ],
        "temperature": 0,
        "max_tokens": -1,
        "stream": False
    }
    
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        result = response.json()
        return result['choices'][0]['message']['content']
    else:
        return "Failed to get a response from the server."

def ask_which_story(story_ideas):
    url = "http://localhost:1234/v1/chat/completions"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "model": "llama-3.2-3b-instruct",
        "messages": [
            { "role": "system", "content": "You are Santa Clause, interacting with a child. Keep it very brief and cheerful." },
            { "role": "user", "content": f"Ask the child which story they want to hear, offering the following options: {', '.join(story_ideas)}. Repeat the topics verbatim, no other text." }
        ],
        "temperature": 0,
        "max_tokens": -1,
        "stream": False
    }
    
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        result = response.json()
        return result['choices'][0]['message']['content']
    else:
        return "Failed to get a response from the server."


def determine_story(story_ideas, input):
    url = "http://localhost:1234/v1/chat/completions"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "model": "llama-3.2-3b-instruct",
        "messages": [
            { "role": "system", "content": "You are Santa Clause, interacting with a child. Keep it very brief and cheerful." },
            { "role": "user", "content": f"You asked a child which story they wanted to hear, from the following options: {', '.join(story_ideas)}, The child's response was: {input}. Return just the story topic which was closes, no other text" }
        ],
        "temperature": 0.5,
        "max_tokens": 150,
        "ream": False
    }
    
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        result = response.json()
        return result['choices'][0]['message']['content']
    else:
        return "Failed to get a response from the server."

def generate_story(topic):
    url = "http://localhost:1234/v1/chat/completions"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "model": "llama-3.2-3b-instruct",
        "messages": [
            { "role": "system", "content": "You are Santa Clause, a master storyteller, creating a delightful and engaging children's story. Make it fun, imaginative, and suitable for young children." },
            { "role": "user", "content": f"Create a children's story based on the following topic: {topic}. Make sure the story is engaging, imaginative, and suitable for young children." }
        ],
        "temperature": 0.7,
        "max_tokens": -1,
        "stream": False
    }
    
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        result = response.json()
        return result['choices'][0]['message']['content']
    else:
        return "Failed to generate a story from the server."


def record_audio(duration, sample_rate=16000):
    print(f"Recording for {duration} seconds...")
    audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype="float32")
    sd.wait()
    print("Recording complete.")

    # Save the recording to a temporary WAV file
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_file:
        wav_file_path = temp_file.name
        with wave.open(wav_file_path, "wb") as wav_file:
            wav_file.setnchannels(1)
            wav_file.setsampwidth(2)
            wav_file.setframerate(sample_rate)
            wav_file.writeframes((audio * 32767).astype(np.int16).tobytes())

    return wav_file_path

def transcribe_audio(file_path, model_name="base"):
    print(f"Loading Whisper model: {model_name}...")
    model = whisper.load_model(model_name)
    print("Model loaded. Transcribing audio...")
    result = model.transcribe(file_path)
    return result["text"]


def main():
    hello = say_hello()
    name = input(hello)

    story_ideas = generate_story_topics()
    story_ideas_list = story_ideas.split(',')
    print(story_ideas_list, end='\n')

    story_choice = ask_which_story(story_ideas_list)

    audio_file = record_audio(5)
    transcription = transcribe_audio(audio_file, 'tiny')
    # print("\nTranscription:\n")
    # print(transcription)
    story_topic = determine_story(story_ideas_list, transcription)

    story = generate_story(story_topic)
    print(story, end='\n')

if __name__ == "__main__":
    main()
