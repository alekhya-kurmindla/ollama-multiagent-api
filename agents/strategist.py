# agents/strategist.py
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from config import strategist_llm

def create_strategist_agent():
    prompt = ChatPromptTemplate.from_template(
        """You are a content strategist. Create a detailed outline for an article about {topic}.
        
        Provide a structured outline with main sections and key points.
        
        Topic: {topic}
        
        Outline:"""
    )
    
    chain = prompt | strategist_llm | StrOutputParser()
    return chain