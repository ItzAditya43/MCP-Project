from dotenv import load_dotenv
load_dotenv()
from educhain.engines.content_engine import ContentEngine
from educhain.core.config import LLMConfig
import json

topic = "Python Programming Basics"

# Use Gemini as the LLM
llm_config = LLMConfig(model_name="gemini-1.5-flash", api_key=None)
engine = ContentEngine(llm_config=llm_config)

# Generate MCQs (flashcards)
mcqs = engine.generate_flashcards(topic=topic, num=5)

# Generate Lesson Plan
lesson_plan = engine.generate_lesson_plan(topic=topic)

# Save to file
output = {
    "topic": topic,
    "mcqs": mcqs,
    "lesson_plan": lesson_plan
}

with open("sample_output.json", "w") as f:
    json.dump(output, f, indent=2, default=str)

print("✅ Content generated and saved to sample_output.json") 