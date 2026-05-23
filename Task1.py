responses = {
    'hello': 'Hi there! How can I help you?',
    'hi': 'Hey! Welcome to DecodeLabs Bot!',
    'how are you': 'I am just a bot, but running perfectly!',
    'what is ai': 'AI stands for Artificial Intelligence!',
    'bye': 'Goodbye! Have a great day!',
    'help': 'I can answer: hello, hi, how are you, what is ai, bye',
    'name': 'My name is DecodeBot!',
    'joke': 'Why do programmers prefer dark mode? Light attracts bugs!',
    'age': 'I was just created today!',
    'weather': 'I cannot check weather, but stay hydrated!',
}

def get_response(user_input):
    clean_input = user_input.lower().strip()
    if clean_input == 'exit':
        return None
    return responses.get(clean_input, "I don't understand. Type 'help'.")

def main():
    print("=" * 40)
    print("   DecoBot - Rule-Based AI Chatbot")
    print("   Type 'exit' to quit")
    print("=" * 40)
    while True:
        user_input = input("You: ")
        response = get_response(user_input)
        if response is None:
            print("Bot: Goodbye!")
            break
        print(f"Bot: {response}")

main()