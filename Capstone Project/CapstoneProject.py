import os
from openai import OpenAI
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

# Initialize OpenAI client with the loaded API key
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# Basic function to get AI response
def get_response(prompt):
    try:
        response = client.responses.create(
            model="gpt-4o",
            instructions="You are a helpful and friendly assistant.",
            input=prompt
        )
        return response.output_text.strip()
    except Exception as e:
        return f"Something went wrong: {e}"

# Simple input loop
print("Chat with your AI assistant. Type 'exit' to end.")
while True:
    user_input = input("\nYou: ")
    if user_input.lower() == "exit":
        print("Goodbye!")
        break
    reply = get_response(user_input)
    print("AI:", reply)
