def chatbot():
    print("Simple Chatbot (type 'bye' to exit)")

    while True:
        user = input("You: ").strip().lower()

        if user == "hello":
            print("Bot: Hi!")
        elif user == "how are you":
            print("Bot: I'm fine, thanks!")
        elif user == "bye":
            print("Bot: Goodbye!")
            break
        else:
            print("Bot: Sorry, I don't understand that.")

if __name__ == "__main__":
    chatbot()
