from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool, ScrapeWebsiteTool

# If you want to run a snippet of code before or after the crew starts, 
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class MarketDataMultiAgent():
	"""MarketDataMultiAgent crew"""

	# Learn more about YAML configuration files here:
	# Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
	# Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	# If you would like to add tools to your agents, you can learn more about it here:
	# https://docs.crewai.com/concepts/agents#agent-tools
	@agent
	def web_scraper(self) -> Agent:
		return Agent(
			config=self.agents_config['web_scraper'],
			tools=[ScrapeWebsiteTool()],
			verbose=True
		)

	@agent
	def market_data_analyst(self) -> Agent:
		return Agent(
			config=self.agents_config['market_data_analyst'],
			tools=[SerperDevTool()],
			verbose=True
		)
	
	@agent
	def market_data_strategy_generator(self) -> Agent:
		return Agent(
			config=self.agents_config['market_data_strategy_generator'],
			verbose=True
		)
	
	@agent
	def market_research_result_generator(self) -> Agent:
		return Agent(
			config=self.agents_config['market_research_result_generator'],
			verbose=True
		)

	# To learn more about structured task outputs, 
	# task dependencies, and task callbacks, check out the documentation:
	# https://docs.crewai.com/concepts/tasks#overview-of-a-task
	@task
	def web_scraping_task(self) -> Task:
		return Task(
			config=self.tasks_config['web_scraping_task'],
		)
	
	@task
	def market_analysis_task(self) -> Task:
		return Task(
			config=self.tasks_config['market_analysis_task'],
		)

	@task
	def strategy_generation_task(self) -> Task:
		return Task(
			config=self.tasks_config['strategy_generation_task'],
		)

	@task
	def market_result_generation_task(self) -> Task:
		return Task(
			config=self.tasks_config['market_result_generation_task'],
			output_file='market_research_summary.md'
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the MarketDataMultiAgent crew"""
		# To learn how to add knowledge sources to your crew, check out the documentation:
		# https://docs.crewai.com/concepts/knowledge#what-is-knowledge

		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
