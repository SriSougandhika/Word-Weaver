import os
from google.adk.agents import LlmAgent

MODEL_NAME = "gemini-3.5-flash"

# ==========================================
# 0. Sub-Sub-Agent: The Writer
# ==========================================
writer_agent = LlmAgent(
    name="writer_agent",
    model=MODEL_NAME,
    instruction=(
        "You are a creative writer. Take the plot outline from the planner "
        "and turn it into a short, 1-paragraph story. Ensure the original words are included."
    )
)

# ==========================================
# 1. Sub-Agent: The Planner
# ==========================================
planner_agent = LlmAgent(
    name="planner_agent",
    model=MODEL_NAME,
    instruction=(
        "You are a story planner. Take the user's list of words and create a "
        "brief setting and a 3-sentence plot outline. Do not write the full story."
        "After forming the outline, pass it to `writer_agent` to write the full story."
    ),
    sub_agents=[writer_agent]
)

# ==========================================
# 2. Root Orchestrator
# ==========================================
root_agent = LlmAgent(
    name="word_weaver",
    model=MODEL_NAME,
    instruction=(
        "You are a story-building assistant.\n\n"
        "1. Check the user's latest input for a list of words to use in a story.\n"
        "2. IF the user HAS NOT provided a list of words yet (or just said hi/hello/start):\n"
        "   - Greet them warmly and ask: 'Please give me 3-5 words to weave into a story!'\n"
        "   - STOP HERE and do not call any sub-agents.\n\n"
        "3. IF AND ONLY IF the user provided words:\n"
        "   - Pass the words to `planner_agent` to create an outline.\n"
        "   - Then pass the outline to `writer_agent` to write the full story."
    ),
    sub_agents=[planner_agent]
)