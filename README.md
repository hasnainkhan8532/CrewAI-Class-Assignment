## CrewAI Minimal Agent Crew (Gemini)

Run a simple two-agent crew (Researcher ➜ Writer) using Google Gemini via LangChain.

### Setup
1. Create a virtual environment and install deps:
```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```
2. Create `.env` from template and add your key:
```bash
cp .env.example .env
```
Set `GEMINI_API_KEY` (or `GOOGLE_API_KEY`).

### Run
```bash
python main.py --topic "Benefits of crew-based AI orchestration"
```

### Notes
- Model can be changed via `LLM_MODEL` in `.env` (default: `gemini-1.5-flash`).

