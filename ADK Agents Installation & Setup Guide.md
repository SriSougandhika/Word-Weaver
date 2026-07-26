# 🚀 Google ADK Installation & Agent Creation Step-By-Step For Beginners!
Hi everyone! Finding issues with ADK installation? ADK not found? Do I need to handle environment variables? API key not found? ADK is running, but the agent is not giving responses?  

To solve these, I have gone through various videos and decided to build an installation guide. 
I did find the ADK documentation helpful, but it still confuses me a bit, so here's a noob's guide to building an agent. 

## 💎 Contents:
- [📦 Step-1: Install Pre-Requisites](#-step-1-install-pre-requisites)
  - [Python](#11-python)
  - [Pip Command](#12-pip-command)
  - [VS Code / Antigravity IDE](#13-vs-code--antigravity-ide)
  - [Google AI Studio Account for API Key](#14-google-ai-studio-account-for-api-key)
- [🛠️ Step-2: Google ADK Installation](#%EF%B8%8F-step-2-google-adk-installation)
  - [Setting up a Virtual Environment and installing ADK](#21-setting-up-a-virtual-environment-and-installing-adk)
- [📂 Step-3: Building The Agent](#-step-3-building-the-agent)
  - [Create the Agent](#31-create-the-agent)
  - [Structure the Agent](#32-structure-the-agent)
- [✨ Step-4: Running the Agent](#-step-4-running-the-agent)
- [📝 Step-5: Troubleshooting Tips that worked for me](#-step-5-troubleshooting-tips-that-worked-for-me)

## 📦 Step-1: Install Pre-Requisites:
### 1.1 Python
- Go to the [Python Official Website](https://www.python.org/downloads/) and hit download for whatever OS you are working on. I suggest using the latest compatible version.
- Click on the installer.exe and install it properly.

### 1.2 Pip Command
- Usually it gets installed with Python, but if not, run the command `python -m ensurepip --upgrade`
- Did not solve the problem? Refer to [pip-documentation](https://pip.pypa.io/en/stable/installation/)

### 1.3 VS Code / Antigravity IDE 
It doesn't really matter what IDE you use to access the files, but it is better to install one.
- For VS Code, begin [here](https://code.visualstudio.com/download)
- For Antigravity, begin [here](https://antigravity.google/download)

If you ask my preference, I like _**Antigravity**_.

### 1.4 Google AI Studio Account for API Key:
- If you do not have a [Google AI Studio](https://aistudio.google.com/) account created, create one by following the on-screen instructions.
- Click on the Create API Key button, name the API key, and select a project there. If you have no projects, create one on the free tier.
- Once created, keep the API Key handy or noted somewhere. We will need this key while creating the project.

**NOTE:** _You need not pay for using API keys for the normal quota assigned to standard Google accounts._

## 🛠️ Step-2: Google ADK Installation
**Before hitting hurried commands of pip install**, we need to set up a virtual environment. Otherwise, it might not work properly. 
Go to the location on your computer where you wish to create the agent repository. No need to create a specific folder for this agent; the ADK does it for us. 

### 2.1 Setting up a Virtual Environment and installing ADK
- Open _Terminal/Power Shell_ inside this folder(where you would want the project repository to be created). 
- Start by creating a **virtual environment** with the command `python3 -m venv .venv`
- Next, you've got to **activate** it. Just creating it will not suffice. Activate it with the command `.venv\Scripts\activate.bat` (for CMD) or `.venv\Scripts\Activate.ps1` (for PowerShell).
- Once activated, you should notice something similar to **"(venv) D:/project_file/path/"** in the terminal.
- Now we install the **ADK** with the command `pip install google-adk`. Stay inside the venv while installing.

## 📂 Step-3: Building The Agent
### 3.1 Create the Agent
- Once done, we can now **create** our agent with the command `adk create my_agent_name`. Make sure you have the venv activated. If not, run the command `.venv\Scripts\Activate.ps1` to activate it again.
- Here, the console will ask you _which model you want_. If you want to explore best with free stuff, go with option 1 - **gemini-3.5-flash**. Enter `1`.
- Next, it will ask you to _choose the backend_; again, go with option 1 - **Google AI**. This is the best, as I have faced issues with the "Login with Google" option, so this one's most convenient. Enter `1` again.
- Now, it will prompt you to paste the _API Key_. Go to the AI Studio, where you kept the API key handy, and paste it there.
- After this, it should create the repository automatically for the agent along with the basic init Python file and agent Python file.

### 3.2 Structure the Agent
- This is where we would be using VS Code or Antigravity to fill up the code files. Open the project folder and begin to write the Python files.   
- Define your **agentic schema** in the **agent.py** file. For reference on how to structure, the ADK series by Google is the best to watch: [Getting started with ADK](https://youtu.be/44C8u0CDtSo?list=PLOU2XLYxmsIIAPgM8FmtEcFTXLLzmh4DK)
- This might be the trickiest step, but the schema might also require extra installations, so keep in mind to install all requirements before running the agent.

## ✨ Step-4: Running the Agent
So, I have two methods noted here, and I love the 2nd option! Before starting to run, ensure you're in the terminal, with the proper path where you have the project folder and virtual environment running.
- **1-Direct Run**:  Use the command `adk run my_agent_name`, and it should begin by showing the conversation between [user] and [root-agent].
- **2-Web Run**: Use the command `adk web`. This will launch the UI on localhost (a link like _http://127.0.0.1:8000/_) to showcase a chat-like UI with some seriously helpful **functionalities**. These involve **visualizing** the agentic schema you have created and seeing exactly how the backend flow is working. 

To _stop running_ the agent, type `exit`, and you will be back in the venv (virtual environment) again. To _deactivate the venv_, type `deactivate`. 

## 📝 Step-5: Troubleshooting Tips that worked for me:
- Configure the **__init__.py** file and use this to call the root agent in this file:
```
from .agent import root_agent
_all_ = ["root_agent"]
```
- Use the model **"gemini-3.5-flash"** (latest one) instead of **"gemini-2.5-flash"** in the code.
- If the model seems not to respond at all, it might be the case that it did not read the api key properly. Go to the .env file, see if a variable GOOGLE_API_KEY is created, and check your api key over there. If it is not inserted, then insert it directly and try saving and running the agent again. 

## ❤️ Yay! You ran an agent successfully with ADK! 
So, summing up, this is how you can simply set up and see the agent running! Try it out now! It is amazing what we can achieve with a simple set of instructions for the agent!

## 👥 Acknowledgements
The resources may contain snippets from:
- Multiple videos out there on YouTube (I can't remember how many I had to see to get a basic agent running up 😆)
- Google ADK Documentation


All the content is self-written and is subject to copyright. 

---

Thanks for taking the time! Hope your agent's running full speed out there!🚀
