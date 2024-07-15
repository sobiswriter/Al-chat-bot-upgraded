import vertexai
from vertexai.preview.language_models import TextGenerationModel
import random
import time

vertexai.init(project="x-avenue-425405-v4", location="us-central1")
model = TextGenerationModel.from_pretrained("text-bison@001")

chat_history = []  # Stores chat history for context

greetings = ["Howdy partner! What's on your mind?", "Well hello there! How can I help you today?",
             "Greetings, earthling! What brings you to my digital doorstep?"]
help_offer = "Is there anything I can help you with today?"

print(random.choice(greetings))
time.sleep(1)
print(help_offer)
time.sleep(1)

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Catch you later, space cowboy!")
        time.sleep(1)  # Simulate typing
        break

    chat_history.append(f"User: {user_input}")  # Add user input to history

    response = model.predict(
        prompt=f"{''.join(chat_history)}",  # Include chat history
        temperature=0.8,  # Adjust for creativity (0 to 1)
        max_output_tokens=150  # Adjust for response length
    )
    chatbot_response = response.text

    # Add a bit of personality
    if "how are you" in user_input.lower():
        chatbot_response = "I'm just a bunch of code, but I'm feeling pretty sharp today! How about you?"
    elif "thank you" in user_input.lower() or "thanks" in user_input.lower():
        chatbot_response = "You're most welcome! Is there anything else I can help you with?"

    chat_history.append(f"Chatbot: {chatbot_response}")  # Add bot's response to history
    print(f"Chatbot: {chatbot_response}")

    # Simulate typing for a more natural feel
    typing_delay = random.uniform(0.5, 1.5)  # Vary typing speed between 0.5 and 1.5 seconds
    time.sleep(typing_delay)
