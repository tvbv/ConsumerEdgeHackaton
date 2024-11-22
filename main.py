#!/usr/bin/env python3

import requests
import json
import whisper
import numpy as np
import sounddevice as sd
import tempfile
import wave
import warnings
from playsound import playsound
from pydub import AudioSegment
from pydub.playback import play


from audio import record_audio, transcribe_audio
from story import generate_story_topics, say_hello, ask_which_story, determine_story, generate_story
from backup_elevenlabs import text_to_speech_file
from audio import combine_audio

warnings.filterwarnings("ignore")

def main():
    # Say hello
    hello = say_hello()
    print(hello, end='\n')
    file = text_to_speech_file(hello)
    audio = AudioSegment.from_file(file, format="mp3")
    play(audio)

    # Generate Story Ideas
    story_ideas = generate_story_topics()
    story_ideas_list = story_ideas.split(',')
    print(story_ideas_list, end='\n')

    # Ask which story they want to hear
    which_story = ask_which_story(story_ideas_list)
    print(which_story, end='\n')

    file = text_to_speech_file(which_story)
    audio = AudioSegment.from_file(file, format="mp3")
    play(audio)

    # Wait for the child to respond
    audio_file = record_audio(10)
    transcription = transcribe_audio(audio_file, 'tiny')

    print(f"What was heard: {transcription}", end='\n')

    story_topic = determine_story(story_ideas_list, transcription)

    story = generate_story(story_topic)
    file = text_to_speech_file(story)
    audio = combine_audio(file, "sounds/jingle_bells.mp3")
    play(audio)

    print(story, end='\n')

if __name__ == "__main__":
    main()
