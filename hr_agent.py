"""
Week 5 - Day 1 : AutoGen HR Assistant Agent
-------------------------------------------
One AssistantAgent with system_message "You are an HR assistant."
asks the model for a 5-line job description and streams it with Console.

Run (inside the VS Code terminal, venv activated):
    python hr_agent.py
"""
import asyncio
import os

from dotenv import find_dotenv, load_dotenv
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient

load_dotenv(find_dotenv())
if not os.getenv("OPENAI_API_KEY"):
    raise SystemExit("OPENAI_API_KEY is not set. Add it to your .env file.")

# The model client talks to OpenAI; it reads OPENAI_API_KEY from the environment
model_client = OpenAIChatCompletionClient(model="gpt-4o-mini")

agent = AssistantAgent(
    name="hr_assistant",
    model_client=model_client,
    system_message="You are an HR assistant.",
)

TASK = (
    "Write a job description for a Junior Python Developer. "
    "Output exactly 6 lines: line 1 is the title 'Junior Python Developer', "
    "then exactly 5 numbered lines (1. to 5.), each one short sentence covering: "
    "responsibilities, core skills, nice-to-have skills, experience/education, "
    "and what we offer. No intro, no closing text, no markdown."
)


async def main() -> None:
    try:
        # run_stream yields messages as they are produced; Console prints them
        await Console(agent.run_stream(task=TASK))
    finally:
        # an unclosed client leaves the script hanging
        await model_client.close()


if __name__ == "__main__":
    asyncio.run(main())
