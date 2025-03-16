import time
import openai
# load dot evn
import os
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
# Assume the client already exists:
client = openai.OpenAI()

def upload_file(pdf_path, purpose="assistants"):
    """Uploads a PDF file using the client's file upload endpoint with purpose 'assistant'."""
    with open(pdf_path, "rb") as file:
        file_response = client.files.create(file=file, purpose=purpose)
    return file_response.id

def create_assistant(name="PDF Q&A Assistant",
                     instructions="You help answer questions based on the content of the provided PDF.",
                     model="gpt-4-turbo",
                     tools=[{"type": "file_search"}]):
    """
    Creates an assistant instance using the client's beta assistants endpoint.
    You only need to create the assistant once and reuse its ID for multiple queries.
    """
    assistant = client.beta.assistants.create(
        name=name,
        instructions=instructions,
        model=model,
        tools=tools
    )
    return assistant.id

def ask_question_assistant(assistant_id, file_id, question):
    """
    Creates a thread, sends a question that references the uploaded PDF,
    and retrieves the assistant's response once the run is complete.
    """
    # Create a new conversation thread
    thread = client.beta.threads.create()
    
    # Send a message with the question and attach the file
    client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=question,
        attachments=[{"tools": [{"type":"file_search"}], "file_id": file_id}]
    )
    
    # Start the assistant run on this thread
    run = client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=assistant_id
    )
    
    # Poll until the run is complete
    while run.status in ["queued", "in_progress"]:
        time.sleep(0.5)
        run = client.beta.threads.runs.retrieve(
            thread_id=thread.id,
            run_id=run.id
        )
    
    # Retrieve messages from the thread and return the assistant's answer
    messages = client.beta.threads.messages.list(thread_id=thread.id)
    for message in messages.data:
        if message.role == "assistant":
            return message.content
    return "No answer received."

# Example usage:
if __name__ == "__main__":
    pdf_path = "upaspro.pdf"  # Replace with your PDF file path
    question_1 = "When was \"AI Optimization: The Key to Smart Transportation\" published?"
    question_2 = "What is the price of Platinum package in Upaspro?"
    
    # Upload the PDF file (purpose must be "assistant")
    file_id = upload_file(pdf_path)
    
    # Create an assistant instance (store the assistant_id for future queries)
    assistant_id = create_assistant()
    
    # Ask a question using the assistant approach
    answer_1 = ask_question_assistant(assistant_id, file_id, question_1)
    answer_2 = ask_question_assistant(assistant_id, file_id, question_2)
    
    print("Answer to question 1:", answer_1)
    print("\n\nAnswer to question 2:", answer_2)
