# 🧙‍♂️ Word Weaver
A multi-agent storytelling assistant built using **Google ADK** and **Gemini**. The agent interacts with the user, collects the keywords, generates a plot outline, and writes a short story that incorporates all the requested words. 

---

## 🚀 Features

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


---

## 🕵️ Why I had to go for the "Sub-Agents" method here and failed to use the "WorkFlow" 


---

## 💡 Tips
