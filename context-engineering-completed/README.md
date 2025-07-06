# Gemini API Wrapper

This project provides a FastAPI backend that acts as a wrapper for the Gemini API, and a Streamlit frontend to provide a simple UI for interacting with the backend.

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2.  **Create a virtual environment and install dependencies:**
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    ```

3.  **Set up your environment variables:**
    -   Copy the `.env.example` file to `.env`:
        ```bash
        cp .env.example .env
        ```
    -   Open the `.env` file and add your Gemini API key:
        ```
        GEMINI_API_KEY=your_api_key_here
        ```

## Usage

1.  **Start the FastAPI backend:**
    ```bash
    uvicorn backend.app.main:app --host 0.0.0.0 --port 8000 &
    ```

2.  **Run the Streamlit frontend:**
    ```bash
    streamlit run frontend/app.py
    ```

3.  **Open your browser:**
    -   Navigate to the Streamlit URL provided in the terminal (usually `http://localhost:8501`).
    -   Enter a query in the text box and click "Submit" to get a response from the Gemini API.

## Testing

To run the backend tests, use pytest:

```bash
pytest
```
