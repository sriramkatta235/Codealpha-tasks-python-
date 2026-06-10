# Basic Chatbot

## Overview

The **Basic Chatbot** is a simple Python command-line application that interacts with users using predefined responses. It accepts user input, checks for matching commands, and provides appropriate replies. The chatbot continues the conversation until the user enters `"bye"` to exit.

## Features

- Interactive command-line conversation.
- Responds to basic greetings like `"hello"`.
- Answers simple questions such as `"how are you"`.
- Exits gracefully when the user types `"bye"`.
- Displays a default response for unrecognized inputs.
- Easy to understand and modify for beginners.

## Requirements

- Python 3.x
- No external libraries are required.

## How to Run

1. Save the program as `basic_chatbot.py`.
2. Open a terminal or command prompt.
3. Navigate to the project directory.
4. Run the following command:

```bash
python basic_chatbot.py
```

## Example

```
Simple Chatbot (type 'bye' to exit)

You: hello
Bot: Hi!

You: how are you
Bot: I'm fine, thanks!

You: what is your name
Bot: Sorry, I don't understand that.

You: bye
Bot: Goodbye!
```

## Working

- The chatbot continuously waits for user input.
- It converts the input to lowercase for easy comparison.
- Based on predefined conditions, it returns an appropriate response.
- The conversation ends when the user enters `"bye"`.

## Future Enhancements

- Add more conversational responses.
- Integrate Natural Language Processing (NLP).
- Support voice input and output.
- Connect with APIs for real-time information.
- Develop a graphical user interface (GUI).

## Author

**Katta Sriram**  
**Computer Science Engineering**
