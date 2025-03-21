#!/usr/bin/env python
import sys
import warnings

from basic_agent.crew import BasicAgent

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """

    # Custom change to allow the Veritai launchpad to pass inputs to the crew.
    # TODO: submit a PR to crewai to allow their cli run commmand to accept inputs.

    # Original code:
    # inputs = {
    #     'topic': 'AI LLMs'
    # }

    # Custom code start
    import os
    import json
    CREW_INPUT_JSON = os.getenv("CREW_INPUT_JSON")
    inputs = {}
    if CREW_INPUT_JSON:
        with open(CREW_INPUT_JSON, "r") as file:
            inputs = json.load(file)
    # Custom code end

    BasicAgent().crew().kickoff(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        BasicAgent().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        BasicAgent().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        BasicAgent().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")
