import pytest
from agents.main_agent import Agent

def test_agent_initialization():
    agent = Agent()
    assert agent is not None

def test_agent_run_with_calculate_tool():
    agent = Agent()
    response = agent.run("Calculate 2 + 2")
    assert "4" in response

def test_agent_run_with_rag():
    agent = Agent()
    # This test assumes that the RAG system is set up and populated
    # with some data.  You'll need to adjust the query to match your data.
    response = agent.run("What is the capital of France?")
    # The response should contain information about Paris, retrieved from the RAG system.
    assert "Paris" in response