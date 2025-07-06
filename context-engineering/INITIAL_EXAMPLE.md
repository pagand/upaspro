## FEATURE:

- A FastAPI backend that acts as a wrapper for the Gemini API.
- A Streamlit frontend to provide a simple UI for interacting with the backend.
- The application should be containerized using Docker.

## EXAMPLES:

The `PRPs/EXAMPLE_multi_agent_prp.md` has been updated to reflect the new project goal and contains a full blueprint. It should be used as the primary reference. The `examples/` directory will be cleared of old examples.

## DOCUMENTATION:

- FastAPI: https://fastapi.tiangolo.com/
- Streamlit: https://docs.streamlit.io/
- Gemini API: https://ai.google.dev/docs
- Docker: https://docs.docker.com/get-started/

## OTHER CONSIDERATIONS:

- The project should include a `docker-compose.yml` for easy startup.
- A `.env.example` file should be provided to show what environment variables are needed (e.g., `GEMINI_API_KEY`).
- The FastAPI backend should have a dedicated service for Gemini API interaction.
- The Streamlit frontend should make API calls to the FastAPI backend.
