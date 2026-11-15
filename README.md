# Week 5 · Day 1 — AutoGen HR Assistant

## Standalone setup (fresh clone, VS Code → Command Prompt)
```bat
py -3.12 -m venv venv
venv\Scripts\activate.bat
pip install -r requirements.txt
copy .env.example .env
REM edit .env and paste your OpenAI key
```

`AssistantAgent` with `system_message="You are an HR assistant."` writes a 5-line JD for a Junior Python Developer, streamed with `Console`, inside `asyncio.run()`, model client closed at the end.

| File | Purpose |
|---|---|
| `hr_agent.py` | The code |
| `output/run.txt` | Captured console output |
| `screenshots/run.png` | Terminal screenshot |

## Run
```bat
venv\Scripts\activate.bat
cd Week5_Day1_AutoGen_HR_Assistant
python hr_agent.py
```
