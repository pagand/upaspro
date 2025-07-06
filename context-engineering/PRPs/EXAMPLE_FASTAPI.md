name: "FastAPI and Streamlit Interface for Gemini"
description: |

## Purpose
Create a FastAPI backend that serves as a wrapper for the Gemini API, and a simple Streamlit frontend to interact with it. This demonstrates a basic client-server architecture for building AI-powered applications.

## Core Principles
1. **Context is King**: Include ALL necessary documentation, examples, and caveats
2. **Validation Loops**: Provide executable tests/lints the AI can run and fix
3. **Information Dense**: Use keywords and patterns from the codebase
4. **Progressive Success**: Start simple, validate, then enhance

---

## Goal
Develop a web application with a FastAPI backend and a Streamlit frontend. The backend will handle requests, interact with the Gemini API, and return the results. The frontend will provide a user-friendly interface for sending queries to the backend and displaying the responses.

## Why
- **Business value**: Provides a simple and extensible framework for building and deploying Gemini-powered applications.
- **Integration**: Demonstrates a common pattern for separating frontend and backend concerns.
- **Problems solved**: Creates a reusable service for accessing Gemini's capabilities without embedding the logic directly into a frontend application.

## What
A web-based application where:
- A Streamlit UI provides a text input for users to ask questions.
- The Streamlit app sends the user's question to a FastAPI backend.
- The FastAPI backend forwards the question to the Gemini API.
- The response from Gemini is streamed back through the FastAPI backend to the Streamlit UI.

### Success Criteria
- [ ] FastAPI backend has an endpoint that accepts a query and returns a response from Gemini.
- [ ] Streamlit frontend can send a query to the FastAPI backend.
- [ ] The response from Gemini is displayed in the Streamlit UI.
- [ ] All tests pass and code meets quality standards.

## All Needed Context

### Documentation & References
```yaml
# MUST READ - Include these in your context window
- url: https://fastapi.tiangolo.com/
  why: Core FastAPI framework documentation.
- url: https://docs.streamlit.io/
  why: Core Streamlit framework documentation.
- url: https://ai.google.dev/docs
  why: Gemini API documentation.
```

### Desired Codebase tree with files to be added
```bash
.
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py              # FastAPI application
│   │   └── services/
│   │       └── gemini_service.py # Logic for interacting with Gemini API
│   ├── tests/
│   │   └── test_main.py         # Tests for the FastAPI app
├── frontend/
│   ├── app.py                   # Streamlit application
├── .env.example                 # Environment variables template
└── requirements.txt             # Python dependencies
```

### Known Gotchas & Library Quirks
```python
# CRITICAL: FastAPI relies on Pydantic for data validation.
# CRITICAL: Streamlit reruns the entire script on each user interaction.
# CRITICAL: Store the Gemini API key securely in an environment variable.
# CRITICAL: Use async functions in FastAPI for non-blocking I/O.
# CRITICAL: For streaming responses, use FastAPI's StreamingResponse.
```

## Implementation Blueprint

### Data models and structure

```python
# backend/app/main.py - Pydantic model for requests
from pydantic import BaseModel

class QueryRequest(BaseModel):
    query: str
```

### List of tasks to be completed

```yaml
Task 1: Setup Project Structure
CREATE directories and empty files from the "Desired Codebase tree".

Task 2: Create FastAPI Backend
CREATE backend/app/main.py:
  - Create a FastAPI app instance.
  - Define a /query endpoint that accepts a POST request with a QueryRequest body.
  - The endpoint should call the Gemini service.
CREATE backend/app/services/gemini_service.py:
  - Create a function that takes a query string.
  - This function should initialize the Gemini client and send the query.
  - It should return the response from Gemini.

Task 3: Create Streamlit Frontend
CREATE frontend/app.py:
  - Create a title and a text input field.
  - When the user enters a query and clicks a button, send a POST request to the FastAPI backend's /query endpoint.
  - Display the response from the backend.


Task 4: Add Tests
CREATE backend/tests/test_main.py:
  - Write a test for the /query endpoint.
  - Mock the Gemini service to avoid actual API calls.

Task 5: Create Documentation
UPDATE README.md:
  - Include setup, installation, and usage instructions.
```

### Per task pseudocode

```python
# backend/app/main.py
from fastapi import FastAPI
from pydantic import BaseModel
from .services import gemini_service

app = FastAPI()

class QueryRequest(BaseModel):
    query: str

@app.post("/query")
async def query(request: QueryRequest):
    response = await gemini_service.get_gemini_response(request.query)
    return {"response": response}

# frontend/app.py
import streamlit as st
import requests

st.title("Gemini Q&A")

query = st.text_input("Ask a question:")

if st.button("Submit"):
    response = requests.post("http://backend:8000/query", json={"query": query})
    st.write(response.json()["response"])
```

### Integration Points
```yaml
ENVIRONMENT:
  - add to: .env.example
  - vars: |
      # Gemini API Key
      GEMINI_API_KEY=your_api_key_here
```

## Validation Loop

### Level 1: Syntax & Style
```bash
# Run these FIRST - fix any errors before proceeding
ruff check . --fix
mypy .

# Expected: No errors.
```

### Level 2: Unit Tests
```bash
# Run backend tests
pytest

# Expected: All tests pass.
```

### Level 3: Integration Test
```bash
# Start the application
uvicorn backend.app.main:app


# Open a browser to the Streamlit URL (e.g., http://localhost:8501)
# Enter a question and verify that a response from Gemini is displayed.
```

## Final Validation Checklist
- [ ] All tests pass: `run backend pytest`
- [ ] No linting errors: `ruff check .`
- [ ] No type errors: `mypy .`
- [ ] The application starts with `uvicorn backend.app.main:app`.
- [ ] The Streamlit UI is accessible in a browser.
- [ ] Queries to the Streamlit UI get responses from the FastAPI backend.
- [ ] The backend successfully calls the Gemini API.
- [ ] README includes clear setup instructions.
- [ ] .env.example has all required variables.

---

## Anti-Patterns to Avoid
- ❌ Don't hardcode API keys - use environment variables.
- ❌ Don't block the event loop in FastAPI with long-running synchronous calls.
- ❌ Don't put complex business logic in the Streamlit app; keep it in the backend.
- ❌ Don't forget to handle potential errors from the Gemini API.

## Confidence Score: 8/10

High confidence due to:
- Clear and well-documented frameworks (FastAPI, Streamlit).
- Simple and common architecture.
- The plan starts with a minimal viable product and progressively enhances it.

Minor uncertainty on the specifics of the Gemini Python SDK, but the documentation should be sufficient.
