import pytest
from agents.main_agent import Agent

@pytest.fixture
def agent():
    return Agent()

def test_agent_initialization(agent):
    assert agent is not None
    assert agent.system_prompt is not None

def test_agent_dummy_tool(agent):
    response = agent.run("Use the dummy tool")
    assert "This is a dummy tool" in response