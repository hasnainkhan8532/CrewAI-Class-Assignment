import os
from dotenv import load_dotenv
from crewai import Crew, Process
from langchain_google_genai import ChatGoogleGenerativeAI

from .agents import build_researcher, build_writer
from .tasks import research_task, writing_task


def _get_llm() -> ChatGoogleGenerativeAI:
    load_dotenv(override=False)
    api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise RuntimeError("Missing GEMINI_API_KEY/GOOGLE_API_KEY in environment")
    model = os.getenv("LLM_MODEL", "gemini-1.5-flash")
    return ChatGoogleGenerativeAI(model=model, api_key=api_key, temperature=0.4)


def build_crew(topic: str) -> Crew:
    llm = _get_llm()

    researcher = build_researcher(llm)
    writer = build_writer(llm)

    t1 = research_task(researcher, topic)
    t2 = writing_task(writer, topic)

    crew = Crew(
        agents=[researcher, writer],
        tasks=[t1, t2],
        process=Process.sequential,
        verbose=True,
    )
    return crew


