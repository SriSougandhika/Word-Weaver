# 🧙‍♂️ Word Weaver
A multi-agent storytelling assistant built using **Google ADK** and **Gemini**. The agent interacts with the user, collects the keywords, generates a plot outline, and writes a short story that incorporates all the requested words. 

---

## 🚀 Key Features

- **Planning Agent:** Uses `gemini-3.5-flash` to structure a 3-sentence plot outline and setting based on user inputs.
- **Writing Agent:** Transforms the outline into a narrative, seamlessly incorporating the requested words.
- **Multi-Agent Orchestration:** Powered by Google's Agent Development Kit (ADK).

---

## ⚙️ Setup & Installation
Not sure how to get started with Google's ADK? View [my documentation here](https://github.com/SriSougandhika/Word-Weaver/blob/main/ADK%20Agents%20Installation%20%26%20Setup%20Guide.md) to get your own agent started in minutes!

Once you've got hold of ADKs and how to run agents in them, all you have to do is follow these steps, which should be easy to understand:
- Pull the repository into your local folder
- Create a virtual environment in this, and set up google-adk if it is not installed.
- Insert your api key in the .env file
- Start the code through PowerShell or the terminal by following the commands:
    - Activate virtual environment: `.venv\Scripts\activate.bat` (for CMD) or `.venv\Scripts\Activate.ps1` (for PowerShell).
    - Start and run your agent: `adk run my_agent_name` for running directly in the terminal or `adk web` to use the ADK's web UI.

---

## 🧩 Understanding the Code
I have a very basic flow for the agent for this task. I have an explanation of each code snippet defining the root agent as well as sub-agents. The current flow I have for my task is: 

_**Start -> User Prompt ->  Root Agent -> Planner Agent -> Writer Agent -> End**_

### Writer Agent: 
This LLM handles the writing section. All it does is weave words according to the plan charted out by the planner agent. 

```
writer_agent = LlmAgent(
    name="writer_agent",
    model=MODEL_NAME,
    instruction=(
        "You are a creative writer. Take the plot outline from the planner "
        "and turn it into a short, 1-paragraph story. Ensure the original words are included."
    )
)
```

### **Planner Agent**:
This LLM handles the weaving part. This shows how the words can be connected, but does not properly put them together. It is a rough draft kind of thing. Here we have defined `writer_agent` as the sub-agent because the planner-agent uses it to craft the story. 

```
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
```

### **Root Agent**: 
This is the orchestrating LLM agent that connects the dots. We have a few more instructions written to handle the case if words are not initially provided by the user. In such a case, we wait for the user to provide the words and hence ask for the same. Once words are given, it is now the duty of the planner to handle the rest. Hence, we have listed the `planner_agent` as the sub-agent of the root agent `word_weaver`.  

```
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
```

### **Initialization**:
This serves as the marker that tells Python a folder should be treated as an importable package or module.
- Line 1: It goes into agent.py, imports the root_agent object, and pulls it up to the package level.
- Line 2: It explicitly defines the public API of your package. Tools like Google ADK look at "\_\_all\_\_" to know exactly which entry-point agent to grab when loading your agent directory.

```
from .agent import root_agent

__all__ = ["root_agent"]
```

--- 

## 🕵️ Why I had to go for the "Sub-Agents" method here and failed to use the "WorkFlow" 
I had tried to create this flow with the _WorkFlow_ import. But this created a problem with the cases where the user had not provided the words. It always ran the systematic path:

_**Start -> Welcome Agent -> Planner Agent -> Writer Agent -> End**_

This was always the case even with a simple "Hello" as a user input. So we needed something like a condition. Hence, I broke it down into two things: one being root with planner sub-agent, and two being planner with writer as sub-agent. This narrowed down the structure to call the planner (as well as the writer) whenever the words were provided; until then, it waited at the welcome stage, which is the root agent here (earlier I had tried to use an LlmAgent for welcoming purposes).

Current fixed and proper path:

<img width="184" height="287" alt="flow diagram" src="https://github.com/user-attachments/assets/11d4b306-f3d8-4a2e-8b7b-572e3b40a7a8" />

---

## 🖥️ Code Implementation Visuals:
**How the output looks while processing:**

<img width="959" height="473" alt="mid-process of request" src="https://github.com/user-attachments/assets/a733ba37-33a6-460c-a114-205e41a7c15e" />


**How the final output looks (the story after it is generated):**

<img width="959" height="473" alt="final output" src="https://github.com/user-attachments/assets/3fdd02d5-ecd8-477c-8055-a1022615c1b8" />


---

## 💡 Conclusions:
So with this mini project on Agentic Development with Google ADK, I have had a few major takeaways:
- **_Agentic AI_**: Structuring and building with multiple agents in a more extensive connected way can keep the line clear and also help strategically achieve tasks. 
- **_ADK Web_**: The Development Kit UI helped me understand how the agents are structured and where the agents go next for a response or next course of action. This also helps in resolving issues with structures and flows.
- **_It is actually easy to create agents_**! The hard part is to put the puzzle pieces together and place the agents in their rightful spots to get things running.

---

## 🌟 Acknowledgments:
All the content is self-written and is subject to **copyright**. The content may seem similar and can be found in multiple places and videos, but I have created this for the sake of convenience and for some peeps who just stumbled here while searching for an easy start.  

Thanks for reading!💐
