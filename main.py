#!/usr/bin/env python3

import warnings
from rapidfuzz import fuzz
import threading

from audio import record_audio, transcribe_audio, say_with_music, say, play_with_music, play_sound
from story import gen_story_topics, gen_hello, gen_ask_which_story, determine_story, gen_story, gen_confirm_story
from elevenlabs_tty import text_to_speech_file

# Filter out some log spew
warnings.filterwarnings("ignore")

def get_best_match(story_topic, stories):
    best_match = None
    highest_score = 0
    for topic in stories.keys():
        score = fuzz.ratio(story_topic, topic)
        if score > highest_score:
            highest_score = score
            best_match = topic
    return best_match

def main():
    story_ideas_list = gen_story_topics()
    stories = {topic: gen_story(topic) for topic in story_ideas_list}

    say_with_music(gen_hello("Karim", "boy"), "sounds/christmas_transitions.mp3")
    say(gen_ask_which_story(story_ideas_list))

    # Wait for the child to respond
    audio_file = record_audio(5)
    transcription = transcribe_audio(audio_file, 'tiny')
    print(f"What was heard: {transcription}", end='\n')

    # Tell the story
    probabalistic_story_topic = determine_story(story_ideas_list, transcription)
    story_topic = get_best_match(probabalistic_story_topic, stories)
    say(gen_confirm_story(story_topic))
    threading.Thread(target=play_sound, args=("sounds/jingle_bells.mp3",)).start()

    say(stories[story_topic])

if __name__ == "__main__":
    main()