
import os
import google.generativeai as genai

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

async def get_gemini_response(query: str):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = await model.generate_content_async(query)
    return response.text
