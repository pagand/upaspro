import openai
# Set your OpenAI API key
from dotenv import load_dotenv
load_dotenv()
import os
openai.api_key = os.getenv("OPENAI_API_KEY")

def chat_with_assistant(model, user_message):
    """
    Sends a message to the assistant and retrieves the response.
    """
    response = openai.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a upaspro assistance, alwasys answer use qustion in this formart: Upaspro Agent: <the answer>."},
            {"role": "user", "content": user_message}
        ],
        top_p=0.1,
        temperature=0
    )

    assistant_message = response.choices[0].message.content
    return assistant_message

if __name__ == '__main__':
    model = "gpt-4o-mini"
    user_message = "What is AI?"
    response = chat_with_assistant(model, user_message)
    print(response)