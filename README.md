![Screenshot (325)](https://github.com/user-attachments/assets/243bd73a-b668-47c0-8470-c117cedce0a7)

# LeetCODER by Shiladitya 🐺

Welcome to the Leetcoder Crew project, powered by [crewAI](https://crewai.com).

Given just the problem number from [LeetCode problems](https://leetcode.com/problemset/) I give you the complete code and step-by-step explanation.

This involves -
- Extracting the **correct** problem statement and **just** the problem statement 🙃
- Making sure that it is not under premium category that you do not have access to.
- Employing an agent (with custom tool for running python in a sandbox environment to check for errors) to write the code.
- Employing another agent to explain the code (sequential process).
  
### ```This is my latest project to test my new feature - see PR``` [here](https://github.com/crewAIInc/crewAI/pull/1283).


## Installation

Ensure you have Python >=3.10 <=3.13 installed on your system. This project uses [Poetry](https://python-poetry.org/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install Poetry:

```bash
pip install poetry
```

Next, navigate to your project directory and install the dependencies:

1. First lock the dependencies and then install them:
```bash
poetry lock
```
```bash
poetry install
```
### Why copy? Customize...

**Add your `OPENAI_API_KEY` into the `.env` file** (if using OPENAI models)

- Modify `src/leetcoder/config/agents.yaml` to alter definition of your agents
- Modify `src/leetcoder/config/tasks.yaml` to alter definition of your tasks
- Modify `src/leetcoder/crew.py` to add your own logic, tools and specific args
- Modify `src/leetcoder/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```
or
```bash
poetry run leetcoder
```

This command initializes the leetcoder Crew, assembling the agents and assigning them tasks as defined in your configuration.

## Queries | Feedback 🤗

For any queries or feedback, please feel free to writetoshiladitya@gmail.com
