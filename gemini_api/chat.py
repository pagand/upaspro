from openai import OpenAI
# Set your OpenAI API key
from dotenv import load_dotenv
load_dotenv()
import os
api_key = os.getenv("GEMINI_API_KEY")
from google import genai
from google.genai import types
from pprint import pprint


def chat_from_gemini(model, prompt):
    client = genai.Client(api_key=api_key)
     
    contents = [ 
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=prompt),
            ],
        ),
    ]
    out = ""
    generate_content_config = types.GenerateContentConfig(
        system_instruction="You are a upaspro assistance, alwasys answer use qustion in this formart: Upaspro Agent: <the answer>.",
        temperature=1,
        top_p=0.95,
        top_k=40,
        max_output_tokens=8192,
        response_mime_type="text/plain",
    )
    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        pprint(chunk.text)
        out += chunk.text
    return out


def chat_from_chatgpt(model, user_message):
    """
    Sends a message to the assistant and retrieves the response.
    """
    client = OpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/")

    response = client.chat.completions.create(
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
    model = "gemini-2.0-flash"
    user_message = "What is Captial of Canada?"
    response = chat_from_gemini(model, user_message)
    print(response)
    response = chat_from_chatgpt(model, user_message)
    print(response)