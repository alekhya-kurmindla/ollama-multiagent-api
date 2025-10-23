# agents/writer.py
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from config import writer_llm

def create_writer_agent():
    prompt = ChatPromptTemplate.from_template(
        """You are a professional writer. Write a detailed draft based on this outline:
        
        {outline}
        
        Topic: {topic}
        
        Write a comprehensive draft:"""
    )
    
    chain = prompt | writer_llm | StrOutputParser()
    return chain