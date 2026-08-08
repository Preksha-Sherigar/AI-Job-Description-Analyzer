# AI Job Description Analyzer

A Streamlit-based application that analyzes a job description and generates a structured summary including:

- Required technical skills
- Required soft skills
- Experience requirements
- Interview questions
- Learning roadmap

This project uses the Groq LLM API to process the pasted job description and return actionable insights in the browser.

## Features

- Paste any job description into the app
- Generate structured analysis using an LLM
- View the result directly in the browser
- Keep API configuration in a local `.env` file
- Use a clean Python environment with dependency management

## Tech Stack

- Python
- Streamlit
- Groq SDK
- python-dotenv

## Project Structure

- `app.py` - Main Streamlit app interface
- `llm_helper.py` - Handles Groq API calls
- `.env.example` - Example environment variable file
- `requirements.txt` - Python dependencies
- `.gitignore` - Ignores environment and cache files

## Setup Instructions

1. Clone the repository

   ```bash
   git clone https://github.com/Preksha-Sherigar/AI-Job-Description-Analyzer.git
   cd AI-Job-Description-Analyzer
   ```

2. Create and activate a virtual environment

   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

   On macOS/Linux:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies

   ```bash
   pip install -r requirements.txt
   ```

4. Configure environment variables

   Copy the example file and update the key:

   ```bash
   copy .env.example .env
   ```

   Or create a new `.env` file manually:

   ```env
   GROQ_API_KEY=your_groq_api_key_here
   ```

5. Run the Streamlit app

   ```bash
   streamlit run app.py
   ```

## Environment Variables

Create a `.env` file in the project root with the following variable:

```env
GROQ_API_KEY=your_groq_api_key_here
```

The app reads this key from `GROQ_API_KEY` using `python-dotenv` and sends it to the Groq API in `llm_helper.py`.

## Notes

- Do not commit your `.env` file to GitHub.
- Keep the Groq API key private and stored locally.
- The project already ignores `.env` and virtual environment files in `.gitignore`.
- The current model used by the app is `llama-3.3-70b-versatile`.

## GitHub Push

If your remote is already configured, run:

```bash
git add .
git commit -m "Update AI Job Description Analyzer"
git push origin main
```

If the repository is not connected yet, first run:

```bash
git remote add origin https://github.com/Preksha-Sherigar/AI-Job-Description-Analyzer.git
git branch -M main
git push -u origin main
```
