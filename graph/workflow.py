# graph/workflow.py
from langgraph.graph import StateGraph, END
from typing import TypedDict
from agents.strategist import create_strategist_agent
from agents.writer import create_writer_agent
from agents.reviewer import create_reviewer_agent

class ArticleState(TypedDict):
    topic: str
    outline: str
    draft: str
    final_article: str

def build_workflow():
    workflow = StateGraph(ArticleState)
    
    # Create agents
    strategist = create_strategist_agent()
    writer = create_writer_agent()
    reviewer = create_reviewer_agent()
    
    # Define nodes
    def strategist_node(state):
        outline = strategist.invoke({"topic": state["topic"]})
        return {"outline": outline}
    
    def writer_node(state):
        draft = writer.invoke({
            "topic": state["topic"],
            "outline": state["outline"]
        })
        return {"draft": draft}
    
    def reviewer_node(state):
        final_article = reviewer.invoke({
            "topic": state["topic"],
            "outline": state["outline"],
            "draft": state["draft"]
        })
        return {"final_article": final_article}
    
    # Add nodes to graph
    workflow.add_node("strategist", strategist_node)
    workflow.add_node("writer", writer_node)
    workflow.add_node("reviewer", reviewer_node)
    
    # Define edges
    workflow.set_entry_point("strategist")
    workflow.add_edge("strategist", "writer")
    workflow.add_edge("writer", "reviewer")
    workflow.add_edge("reviewer", END)
    
    return workflow.compile()