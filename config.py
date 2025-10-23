# config.py
from langchain_ollama import ChatOllama

# Strategist for planning/outlines
strategist_llm = ChatOllama(model="llama3:latest", temperature=0.7)

# Content writer for drafts
writer_llm = ChatOllama(model="Eomer/gpt-3.5-turbo:latest", temperature=0.8)

# Reviewer for refinement/accuracy
reviewer_llm = ChatOllama(model="medllama2:latest", temperature=0.6)