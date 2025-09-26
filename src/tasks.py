from crewai import Task
from crewai import Agent


def research_task(agent: Agent, topic: str) -> Task:
    return Task(
        description=(
            f"Research the topic: '{topic}'.\n"
            "Provide a concise bullet list of 5-8 key points and facts."
        ),
        expected_output=(
            "A short bullet list of key insights about the topic, no fluff."
        ),
        agent=agent,
    )


def writing_task(agent: Agent, topic: str) -> Task:
    return Task(
        description=(
            f"Write a short article (<=300 words) about: '{topic}'.\n"
            "Use the research notes from the previous task. Include a brief intro,"
            " a few bullet points if helpful, and a closing sentence."
        ),
        expected_output=(
            "A clear, structured article under 300 words with headings or bullets as needed."
        ),
        agent=agent,
    )


