import re

# Define the chatbot response function
def chatbot_response(user_input):
    # Convert user input to lowercase for case-insensitive matching
    user_input = user_input.lower()

    # Define patterns and responses
    patterns = {
        r"hello|hi|hey": "Hello! How can I help you today?",
        r"how are you": "I'm just a program, but I'm doing great! How can I assist you?",
        r"what is your name|who are you": "I'm a simple chatbot created to assist you. What's your name?",
        r"bye|goodbye": "Goodbye! Have a great day!",
        r"thank you|thanks": "You're welcome! If you have any more questions, feel free to ask.",
        r"what can you do": "I can respond to basic queries and provide assistance with predefined rules. How can I help you?",
        r"how do you work": "I use pattern matching to identify user queries and respond with predefined answers. Try asking me something!",
        r"tell me a joke": "Why don't scientists trust atoms? Because they make up everything!",
        r"what is the weather like": "I'm not connected to the internet, so I can't provide real-time weather updates. But you can check a weather app for the latest information.",
        r"what is the capital of (.*)": handle_capital_query,
        r"who is (.*)": "I'm not sure who {} is. Can you provide more context?",
        r"tell me about (.*)": handle_knowledge_base,
    }

    # Iterate over patterns and find a match
    for pattern, response in patterns.items():
        match = re.search(pattern, user_input)
        if match:
            if callable(response):
                return response(match)
            if "{}" in response:
                return response.format(match.group(1))
            return response

    # Default response if no pattern matches
    return "I'm not sure how to respond to that. Can you please rephrase?"

# Function to handle capital queries
def handle_capital_query(match):
    country = match.group(1)
    capitals = {
        "france": "Paris",
        "germany": "Berlin",
        "italy": "Rome",
        "japan": "Tokyo",
        "india": "New Delhi",
    }
    capital = capitals.get(country.lower(), "I'm not sure what the capital of {} is.".format(country))
    return "The capital of {} is {}.".format(country, capital)

# Function to handle queries from a simple knowledge base
def handle_knowledge_base(match):
    topic = match.group(1)
    knowledge_base = {
        "python": "Python is a high-level programming language known for its readability and versatility.",
        "machine learning": "Machine learning is a field of artificial intelligence that focuses on developing algorithms that learn from and make predictions on data.",
        "chatbots": "Chatbots are AI programs designed to simulate conversation with human users, especially over the Internet.",
    }
    info = knowledge_base.get(topic.lower(), "I'm sorry, I don't have information on {}.".format(topic))
    return info

# Example interaction with the chatbot
while True:
    user_input = input("You: ")
    if user_input.lower() in ["bye", "goodbye"]:
        print("Chatbot: " + chatbot_response(user_input))
        break
    else:
        print("Chatbot: " + chatbot_response(user_input))

