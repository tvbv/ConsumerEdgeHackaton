import requests
import json

from text_gen import generate_text

def gen_story_topics() -> list:
    topics = generate_text(
        "llama-3.2-3b-instruct", 
        "You are Santa Clause, interacting with a child. Keep it very brief and cheerful.", 
        "Return three story topics, Santa related, make them simple to reference, so the child can easily choose one. "
        "Only return three topics, separated by commas, with no other text, or formatting",
        temperature=0.5,
        max_tokens=-1
    )

    print('Parsed topics:', topics, end='\n')
    return topics.split(',')


def gen_hello() -> str:
    return generate_text(
        "llama-3.2-3b-instruct",
        "You are Santa Clause, interacting with a child. Keep it very brief and cheerful.",
        "Very briefly introduce yourself, and ask for the child's name.",
        temperature=0.7,
        max_tokens=-1
    )

def gen_ask_which_story(story_ideas: list) -> str:
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

def gen_story(topic: str) -> str:
    return generate_text(
        "llama-3.2-3b-instruct",
        "You are Santa Clause, a master storyteller, creating a delightful and engaging children's story. Make it fun, imaginative, and suitable for young children.",
        f"Create a children's story based on the following topic: {topic}. Make sure the story is engaging, imaginative, and suitable for young children. Do not include any formatting, just the text, and just the story",
        temperature=0.7,
        max_tokens=-1
    )

