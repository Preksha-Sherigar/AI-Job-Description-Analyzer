# AI Job Description Analyzer

A simple Streamlit app that analyzes a job description and returns a structured summary covering:

- Required technical skills
- Required soft skills
- Experience required
- Interview questions
- A learning roadmap

## Features

- Paste any job description into the app
- Generate a structured analysis using an LLM
- View results directly in the browser

## Tech Stack

- Python
- Streamlit
- Groq API
- python-dotenv

## Project Structure

- `app.py` - Main Streamlit application
- `llm_helper.py` - LLM helper for calling the Groq API
- `list_models.py` - Optional script to list available models

## Setup Instructions

1. Clone the repository
2. Create and activate a virtual environment

   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. Install dependencies

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file using the example below

   ```env
   GROQ_API_KEY=your_groq_api_key_here
   ```

5. Run the app

   ```bash
   streamlit run app.py
   ```

## Environment Variables

Create a `.env` file in the project root with:

```env
GROQ_API_KEY=your_groq_api_key_here
```

## Notes

- Keep your API keys private and do not commit them to GitHub.
- The repository already includes `.env` in the ignore rules.
