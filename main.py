# main.py
from fastapi import FastAPI
from graph.workflow import build_workflow

app = FastAPI(title="Ollama Multi-Agent API")

workflow = build_workflow()

@app.post("/generate/")
def generate_content(payload: dict):
    topic = payload.get("topic", "AI in Healthcare")
    
    # Initialize state with the topic
    initial_state = {"topic": topic}
    
    # Run the workflow
    result = workflow.invoke(initial_state)
    
    return {
        "topic": topic,
        "outline": result["outline"],
        "draft": result["draft"],
        "final_article": result["final_article"]
    }

@app.get("/")
def read_root():
    return {"message": "Ollama Multi-Agent API is running!"}

# Optional: Add health check endpoint
@app.get("/health")
def health_check():
    return {"status": "healthy", "message": "API is running successfully"}