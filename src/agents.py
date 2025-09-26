from crewai import Agent
from typing import Any


def build_researcher(llm_model: Any) -> Agent:
    return Agent(
        role="Researcher",
        goal=(
            "Collect concise, relevant information and key points about the given topic."
        ),
        backstory=(
            "You excel at skimming sources and extracting essential facts,"
            " lists, and brief summaries that another agent can use to write."
        ),
        llm=llm_model,
        verbose=True,
        allow_delegation=False,
    )


def build_writer(llm_model: Any) -> Agent:
    return Agent(
        role="Writer",
        goal=(
            "Transform the research notes into a clear, structured, and engaging short article."
        ),
        backstory=(
            "You are a precise technical writer who produces readable content with headings"
            " and bullet points when helpful. Keep it under 300 words."
        ),
        llm=llm_model,
        verbose=True,
        allow_delegation=False,
    )


