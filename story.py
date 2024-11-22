import requests
import json

from text_gen import generate_text

def generate_story_topics():
    return generate_text(
        "llama-3.2-3b-instruct", 
        "You are Santa Clause, interacting with a child. Keep it very brief and cheerful.", 
        "Return three story topics, Santa related, make them simple to reference, so the child can easily choose one. "
        "Only return three topics, separated by commas, with no other text",
        temperature=0.5,
        max_tokens=-1
    )

def say_hello():
    return generate_text(
        "llama-3.2-3b-instruct",
        "You are Santa Clause, interacting with a child. Keep it very brief and cheerful.",
        "Very briefly introduce yourself, and ask for the child's name.",
        temperature=0.7,
        max_tokens=-1
    )

def ask_which_story(story_ideas):
    return generate_text(
        "llama-3.2-3b-instruct",
        "You are Santa Clause, interacting with a child. Keep it very brief and cheerful.",
        f"Ask the child which story they want to hear, offering the following options: {', '.join(story_ideas)}. Repeat the topics verbatim, no other text.",
        temperature=0,
        max_tokens=-1
    )

def determine_story(story_ideas, input):
    return generate_text(
        "llama-3.2-3b-instruct",
        "You are Santa Clause, interacting with a child. Keep it very brief and cheerful.",
        f"You asked a child which story they wanted to hear, from the following options: {', '.join(story_ideas)}, The child's response was: {input}. Return just the story topic which was closest, no other text",
        temperature=0.5,
        max_tokens=150
    )

def generate_story(topic):
    return generate_text(
        "llama-3.2-3b-instruct",
        "You are Santa Clause, a master storyteller, creating a delightful and engaging children's story. Make it fun, imaginative, and suitable for young children.",
        f"Create a children's story based on the following topic: {topic}. Make sure the story is engaging, imaginative, and suitable for young children.",
        temperature=0.7,
        max_tokens=-1
    )

