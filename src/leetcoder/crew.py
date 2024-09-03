# created by Shiladitya©
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from leetcoder.tools.custom_tool import PythonCompiler
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
load_dotenv()

@CrewBase
class LeetcoderCrew():
	'''Leetcoder crew'''
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	llm = ChatGroq(model='llama-3.1-70b-versatile', api_key = os.environ['GROQ_COWORKER'])
	manager = ChatGroq(model='llama-3.1-70b-versatile', api_key = os.environ['GROQ_MANAGER'])

	def __init__(self):
		self.agents = None

	@agent
	def coding_expert(self) -> Agent:
		return Agent(
			config=self.agents_config['coding_expert'],
			llm = self.llm,
			tools=[PythonCompiler()],
			allow_delegation = False,
			verbose=True,
		)

	@agent
	def teaching_expert(self) -> Agent:
		return Agent(
			config=self.agents_config['teaching_expert'],
			llm = self.llm,
			allow_delegation = False,
			verbose=True,
		)

	@agent
	def manager_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['manager_agent'],
			allow_delegation = True,
			verbose = True,
			llm = self.manager
		)

	@task
	def coding_task(self) -> Task:
		return Task(
			config=self.tasks_config['coding_task'],
		)

	@task
	def teaching_task(self) -> Task:
		return Task(
			config=self.tasks_config['teaching_task'],
			# output_file='report.md'
		)

	@crew
	def crew(self) -> Crew:
		return Crew(
			agents=self.agents[:2],
			tasks=self.tasks,
			process=Process.sequential,
			verbose=True,
			# manager_agent = self.agents[2],
			# memory=True, #needs openai_api_key to run
		)
