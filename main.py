import argparse
from src.crew_setup import build_crew


def run(topic: str) -> str:
    crew = build_crew(topic)
    result = crew.kickoff()
    return str(result)


def main() -> None:
    parser = argparse.ArgumentParser(description="Run a simple CrewAI pipeline with Gemini")
    parser.add_argument("--topic", required=True, help="Topic to research and write about")
    args = parser.parse_args()

    output = run(args.topic)
    print("\n=== Crew Output ===\n")
    print(output)


if __name__ == "__main__":
    main()


