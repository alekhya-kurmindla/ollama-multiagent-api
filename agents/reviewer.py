# agents/reviewer.py
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from config import reviewer_llm

def create_reviewer_agent():
    prompt = ChatPromptTemplate.from_template(
        """You are an expert reviewer. Refine this draft into a polished final article:
        
        Draft: {draft}
        
        Topic: {topic}
        Outline: {outline}
        
        Provide the final polished article:"""
    )
    
    chain = prompt | reviewer_llm | StrOutputParser()
    return chain