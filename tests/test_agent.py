import pytest
from agents.main_agent import Agent

def test_agent_initialization():
    agent = Agent()
    assert agent is not None

def test_agent_run_with_calculate_tool():
    agent = Agent()
    response = agent.run("What is 2 + 2?")
    assert "4" in response

def test_agent_run_rag_pipeline_design():
    agent = Agent()
    response = agent.run("Design a RAG pipeline for PDF documents.")
    assert "Architecture Diagram" in response
    assert "Step-by-step explanation" in response
    assert "Code snippets" in response