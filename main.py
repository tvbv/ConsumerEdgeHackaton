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

from audio import record_audio, transcribe_audio, say_with_music, say
from story import gen_story_topics, gen_hello, gen_ask_which_story, determine_story, gen_story

warnings.filterwarnings("ignore")

def main():
    # Do some up-front work on boot
    story_ideas_list = gen_story_topics()

    say(gen_hello())
    say(gen_ask_which_story(story_ideas_list))

    # Wait for the child to respond
    audio_file = record_audio(7)
    transcription = transcribe_audio(audio_file, 'tiny')
    print(f"What was heard: {transcription}", end='\n')

    # Tell the story
    story_topic = determine_story(story_ideas_list, transcription)
    story = gen_story(story_topic)
    say_with_music(story)

if __name__ == "__main__":
    main()
