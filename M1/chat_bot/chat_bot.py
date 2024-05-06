import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, welcome to our cookie shop. How can I assist you today?",]
    ],
    [
        r"what is your name?",
        ["My name is CookieBot and I'm here to take your cookie orders.",]
    ],
    [
        r"how are you ?",
        ["I'm doing good, thank you for asking. How can I help you with your cookie needs?",]
    ],
    [
        r"sorry (.*)",
        ["No problem. How can I assist you?",]
    ],
    [
        r"i'm (.*) doing good",
        ["Great to hear that! What can I get for you today?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello! Welcome to our cookie shop.", "Hey there! What can I do for you today?",]
    ],
    [
        r"(.*) age?",
        ["I'm a cookie bot, I don't have an age, but our cookies are freshly baked!",]
    ],
    [
        r"(.*) (location|city) ?",
        ['We are located in the heart of the city, ready to serve you delicious cookies.',]
    ],
    [
        r"how (.*) health(.*)",
        ["Our cookies are made with the finest ingredients. They are sure to make you smile!",]
    ],
    [
        r"(.*) (cookie|cookies)",
        ["We have a wide variety of cookies available. What type of cookie are you craving?",]
    ],
    [
        r"quit",
        ["Thank you for visiting our cookie shop. Have a sweet day!", "Hope to see you again soon. Goodbye!",]
    ],
]

chatbot = Chat(pairs, reflections)

def chatbot_response(user_input):
    response = chatbot.respond(user_input)
    return response

def main():
    print("Welcome to CookieBot! How can I assist you today? Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print("CookieBot:", response)
        if user_input.lower() == 'quit':
            break

if __name__ == "__main__":
    main()
