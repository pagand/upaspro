import os
from dotenv import load_dotenv
from google import genai
import pathlib
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
# Assume the client already exists:
client = genai.Client(api_key=api_key)
model = "gemini-2.0-flash"

pdf_path = "./upaspro.pdf" 
# Retrieve the PDF
file_path = pathlib.Path(pdf_path)
# Upload the PDF using the File API
sample_file = client.files.upload(file=file_path,)
user_prompt = "Answer the question based on the attached PDF file:"
question_1 = "When was \"AI Optimization: The Key to Smart Transportation\" published?"
question_2 = "What is the price of Platinum package in Upaspro?"
prompt= user_prompt  + question_1
response = client.models.generate_content(model=model, contents=[sample_file, prompt], config={"topP":0.5, "maxOutputTokens":4096, "temperature": 0})
print(question_1)
print(response.text)
print("\n")


prompt= user_prompt  + question_2
response = client.models.generate_content(model=model, contents=[sample_file, prompt], config={"topP":0.5, "maxOutputTokens":4096, "temperature": 0})
print(question_2)
print(response.text)