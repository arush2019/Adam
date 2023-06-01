import random

def get_random_response():
    responses = [
        "Interesting!",
        "Tell me more.",
        "I'm not sure about that.",
        "What do you think?",
        "That's fascinating!",
        "I'd love to learn more about that.",
        "Could you please elaborate?",
    ]
    return random.choice(responses)

def chatbot():
    print("Hello! I'm a chatbot. How can I assist you today?")
    while True:
        user_input = input("> ")
        user_input = user_input.lower()

        if user_input == "hello":
            print("Hello! How are you?")
        elif user_input == "goodbye":
            print("Goodbye! Have a great day!")
            break
        elif "how are you" in user_input:
            print("I'm just a chatbot, but I'm here to help!")
        else:
            response = get_random_response()
            print(response)
  
# Start the chatbot
chatbot()
