# Multi-Agent API

The system demonstrates a **Manager agent** orchestrating multiple specialized agents: **Strategist, ContentWriter, and Reviewer**.

A **minimal, production-ready multi-agent system** built with **FastAPI, LangGraph, and LangChain**, orchestrated using **Ollama LLMs**.  

A **FastAPI + LangGraph + LangChain-powered multi-agent system** orchestrated through Ollama.  
This system uses multiple Ollama LLMs as agents for planning, content generation, and review/refinement.

---

## Features

- **Manager Agent:** Orchestrates multiple agents to achieve complex workflows.  
- **Strategist Agent:** Generates outlines and planning for tasks or content.  
- **ContentWriter Agent:** Produces drafts based on the outline.  
- **Reviewer Agent:** Refines and improves content for clarity, correctness, and quality.  
- **Orchestration:** Achieved via **LangGraph**, allowing multi-step workflows with dependency tracking.  
- **Agent Implementation:** Built using **LangChain** to manage LLM calls, prompts, and chaining logic.  
- **API Endpoint:** Exposed via **FastAPI** for easy integration and usage.
---
## Architecture

```

           ┌─────────────────────────────┐
           │        Manager Agent        │
           │  (orchestrates the flow)    │
           └──────────────┬──────────────┘
                          │
          ┌───────────────┼────────────────┐
          │               │                │
  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐
  │ Strategist   │ │ ContentWrite │ │ Reviewer     │
  │ (plans task) │ │ (creates)    │ │ (refines)    │
  └──────────────┘ └──────────────┘ └──────────────┘
                          │
                    ┌─────────────┐
                    │  LangGraph  │
                    │  Workflow   │
                    └─────────────┘
                          │
                    ┌─────────────┐
                    │  FastAPI    │
                    │  Endpoint   │
                    └─────────────┘

```
---
## Project Structure
```
ollama-multiagent-api/
├─ agents/
│ ├─ init.py
│ ├─ strategist.py # Planning & outlines
│ ├─ writer.py # Draft content generation
│ └─ reviewer.py # Review & refinement
├─ graph/
│ ├─ init.py
│ └─ workflow.py # Orchestration workflow with LangGraph
├─ config.py # Ollama model configurations
├─ main.py # FastAPI server entry point
├─ requirements.txt # Python dependencies
├─ .env # Environment variables (optional)
└─ venv/ # Optional virtual environment

```

---

## Setup


```
Create and activate a virtual environment

python3 -m venv venv
source venv/bin/activate       # macOS/Linux
# venv\Scripts\activate        # Windows
Install dependencies


pip install --upgrade pip
pip install -r requirements.txt
Configure environment variables (optional)

Create a .env file:


```

Agents:
---

Strategist (agents/strategist.py) → Plans and creates outlines

ContentWriter (agents/writer.py) → Generates drafts

Reviewer (agents/reviewer.py) → Refines and improves content

Description:
---
All agents use Ollama models configured in config.py.

Workflow Example
You can orchestrate a workflow through graph/workflow.py:

from graph.workflow import run_workflow

topic = "Agentic AI in modern systems"
result = run_workflow(topic)
print(result)
Workflow Steps:

Strategist generates a detailed outline.

ContentWriter drafts content based on the outline.

Reviewer refines the draft for clarity and accuracy.

Notes:
---
Make sure the Ollama daemon is running before calling any LLM.

Adjust temperature and max_tokens in config.py for desired creativity and length.

This setup is ready for local development and can be extended for production deployments.

To kill running port
kill -9 $(lsof -ti:port_number)
kill -9 $(lsof -ti:8000)

Output
{
    "topic": "Benefits of Drinking Water",
    "outline": "Here is a detailed outline for an article on the benefits of drinking water:\n\n**I. Introduction**\n\n* Brief overview of the importance of hydration\n* Thesis statement: Drinking enough water has numerous benefits for overall health, energy levels, and cognitive function.\n\n**II. Physical Health Benefits**\n\n* Improved digestion and reduced risk of constipation (key point 1)\n* Boosted immune system and reduced risk of infections (key point 2)\n* Regulated blood pressure and reduced risk of hypertension (key point 3)\n* Reduced kidney stone formation and improved urinary tract health (key point 4)\n\n**III. Mental Health Benefits**\n\n* Improved mood and reduced symptoms of depression (key point 5)\n* Enhanced focus, concentration, and mental clarity (key point 6)\n* Reduced stress levels and improved emotional regulation (key point 7)\n\n**IV. Cognitive Function Benefits**\n\n* Improved memory and learning ability (key point 8)\n* Enhanced reaction time and problem-solving skills (key point 9)\n* Reduced risk of neurodegenerative diseases, such as Alzheimer's and Parkinson's (key point 10)\n\n**V. Skin and Hair Benefits**\n\n* Improved skin hydration and reduced signs of aging (key point 11)\n* Stronger, healthier hair with reduced breakage and frizz (key point 12)\n\n**VI. Sports and Fitness Performance Benefits**\n\n* Improved athletic performance and endurance (key point 13)\n* Enhanced recovery after exercise and reduced muscle soreness (key point 14)\n* Reduced risk of dehydration-related illnesses, such as heat exhaustion and stroke (key point 15)\n\n**VII. Conclusion**\n\n* Recap of the benefits of drinking water\n* Call to action: Encourage readers to prioritize their hydration and make drinking water a habit.\n\nThis outline provides a comprehensive structure for an article that covers various aspects of the benefits of drinking water, from physical health to cognitive function, skin and hair, and sports performance.",
    "draft": "\nTitle: The Life-Changing Benefits of Drinking Enough Water\n\nIntroduction:\nDrinking enough water is essential for maintaining overall health, energy levels, and cognitive function. In this article, we will explore the numerous benefits of drinking water, from improving digestion and boosting the immune system to enhancing mental clarity and reducing stress. By prioritizing hydration, you can experience a significant improvement in your overall well-being.\n\nPhysical Health Benefits:\n\n1. Improved digestion and reduced risk of constipation: Drinking enough water helps regulate bowel movements and prevents constipation. This is especially important for maintaining good gut health, as a healthy gut microbiome can reduce the risk of various diseases.\n2. Boosted immune system and reduced risk of infections: Water is essential for maintaining the health of your immune system. Drinking enough water helps to flush out toxins and bacteria from your body, reducing the risk of infections.\n3. Regulated blood pressure and reduced risk of hypertension: Drinking water can help regulate blood pressure and reduce the risk of developing hypertension. This is especially important for individuals who are at risk of developing high blood pressure due to genetic factors or lifestyle choices.\n4. Reduced kidney stone formation and improved urinary tract health: Drinking enough water helps to prevent the formation of kidney stones and maintain good urinary tract health. This is especially important for individuals who have a history of kidney stones or other urinary tract problems.\n\nMental Health Benefits:\n\n1. Improved mood and reduced symptoms of depression: Drinking enough water can help regulate mood and reduce symptoms of depression. This is especially important for individuals who are prone to mood swings or experience seasonal affective disorder.\n2. Enhanced focus, concentration, and mental clarity: Drinking water can improve cognitive function and enhance focus, concentration, and mental clarity. This is especially important for individuals who need to stay mentally sharp, such as students, entrepreneurs, or professionals.\n3. Reduced stress levels and improved emotional regulation: Drinking enough water can help reduce stress levels and improve emotional regulation. This is especially important for individuals who experience anxiety or stress-related disorders.\n\nCognitive Function Benefits:\n\n1. Improved memory and learning ability: Drinking water can improve cognitive function and enhance memory and learning ability. This is especially important for individuals who need to retain information or learn new skills.\n2. Enhanced reaction time and problem-solving skills: Drinking water can improve reaction time and problem-solving skills, making it easier to adapt to changing situations.\n3. Reduced risk of neurodegenerative diseases, such as Alzheimer's and Parkinson's: Drinking enough water may reduce the risk of developing neurodegenerative diseases such as Alzheimer's and Parkinson's.\n\nSkin and Hair Benefits:\n\n1. Improved skin hydration and reduced signs of aging: Drinking water can improve skin hydration and reduce the appearance of fine lines, wrinkles, and age spots.\n2. Stronger, healthier hair with reduced breakage and frizz: Drinking enough water can improve the overall health of your hair, reducing breakage and frizz while promoting growth and strength.\n\nSports and Fitness Performance Benefits:\n\n1. Improved athletic performance and endurance: Drinking water before, during, and after exercise can improve athletic performance and endurance by maintaining proper hydration levels.\n2. Enhanced recovery after exercise and reduced muscle soreness: Drinking water after exercise can help reduce muscle soreness and promote faster recovery.\n3. Reduced risk of dehydration-related illnesses, such as heat exhaustion and stroke: Drinking enough water during exercise can reduce the risk of dehydration-related illnesses, such as heat exhaustion and stroke.\n\nConclusion:\nDrinking enough water is essential for maintaining overall health, energy levels, and cognitive function. By prioritizing hydration, you can experience a significant improvement in your well-being. Make drinking water a habit today and enjoy the numerous benefits it has to offer!",
    "final_article": "Here is your refined and polished draft:\nTitle: The Life-Changing Benefits of Drinking Enough Water\n\nIntroduction:\nDrinking enough water is essential for maintaining overall health, energy levels, and cognitive function. In this article, we will explore the numerous benefits of drinking water from improving digestion to enhancing mental clarity. By prioritizing hydration, you can experience a significant improvement in your well-being.\n\nPhysical Health Benefits:\nDrinking enough water has numerous physical health benefits, including improved digestion and reduced risk of constipation, boosted immune system and reduced risk of infections, regulated blood pressure and reduced risk of hypertension, and reduced kidney stone formation and improved urinary tract health.\n\nMental Health Benefits:\nDrinking water can also improve mental health by reducing symptoms of depression, enhancing focus, concentration, and mental clarity, and improving emotional regulation.\n\nCognitive Function Benefits:\nDrinking water has numerous cognitive function benefits, including improved memory and learning ability, enhanced reaction time and problem-solving skills, and reduced risk of neurodegenerative diseases such as Alzheimer's and Parkinson's.\n\nSkin and Hair Benefits:\nDrinking enough water can also improve skin and hair health by reducing signs of aging, promoting stronger and healthier hair growth, and improving overall skin hydration.\n\nSports and Fitness Performance Benefits:\nDrinking water before, during, and after exercise can improve athletic performance and endurance by maintaining proper hydration levels. It can also enhance recovery after exercise and reduce muscle soreness.\n\nConclusion:\nBy prioritizing hydration, you can experience a significant improvement in your overall well-being. Make drinking water a habit today and enjoy the numerous benefits it has to offer!"
}