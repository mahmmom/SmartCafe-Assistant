import random

# This file contains random responses for the chatbot
def random_greetings():
    random_list = [
        "Hello! How can I help you today?",
        "Hi there! What can I get for you?",
        "Good day! What's on your mind?",
        "Hey! How can I assist you today?",
        "Good to see you again! What can I get for you?",
        "Welcome back! What's on your mind?",
        "Hi there! What can I get for you?",
        "Good day! What's on your mind?",
        "Hey! How can I assist you today?",
    ]

    list_count = len(random_list)
    random_item = random.randrange(list_count)

    return random_list[random_item]

# This function returns a random string when the chatbot does not understand the user's input
def random_string():
    random_list = [
        "Please try writing something more descriptive.",
        "Oh! It appears you wrote something I don't understand yet",
        "Do you mind trying to rephrase that?",
        "I'm terribly sorry, I didn't quite catch that.",
        "I can't answer that yet, please try asking something else."
    ]

    list_count = len(random_list)
    random_item = random.randrange(list_count)

    return random_list[random_item]