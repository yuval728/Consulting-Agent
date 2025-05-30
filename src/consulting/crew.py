from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.memory import LongTermMemory
from crewai.memory.storage.ltm_sqlite_storage import LTMSQLiteStorage
from crewai_tools import ScrapeWebsiteTool, LinkupSearchTool
import os
import dotenv

dotenv.load_dotenv()

llm = LLM(
    model="gemini/gemini-2.0-flash-lite",
    temperature=0.0,
)

linkup_search = LinkupSearchTool(api_key=os.getenv('LINKUP_API_KEY'))

@CrewBase
class Consulting():
    """Consulting crew"""

    agents_config = 'config/agents.yaml'  # Assume this is a dict loaded from YAML
    tasks_config = 'config/tasks.yaml'    # Assume this is a dict loaded from YAML

    @agent
    def market_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['market_analyst'],
            verbose=True,
            llm=llm,
            # tools=[
            #     ScrapeWebsiteTool(),
            #     linkup_search,
            # ],
            # allow_delegation=True
        )

    @agent
    def financial_advisor(self) -> Agent:
        return Agent(
            config=self.agents_config['financial_advisor'],
            verbose=True,
            llm=llm,
            # tools=[
            #     ScrapeWebsiteTool(),
            #     linkup_search,
            # ],
            # allow_delegation=True
        )

    @agent
    def tech_consultant(self) -> Agent:
        return Agent(
            config=self.agents_config['tech_consultant'],
            verbose=True,
            llm=llm,
            # tools=[
            #     ScrapeWebsiteTool(),
            #     linkup_search,
            # ],
            # allow_delegation=True
        )

    @agent
    def marketing_strategist(self) -> Agent:
        return Agent(
            config=self.agents_config['marketing_strategist'],
            verbose=True,
            llm=llm,
            # tools=[
            #     ScrapeWebsiteTool(),
            #     linkup_search,
            # ],
            # allow_delegation=True
        )

    @task
    def market_analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config['market_analysis_task'],
            # async_execution=True,
            output_file='market_analysis.md',
        )

    @task
    def financial_evaluation_task(self) -> Task:
        return Task(
            config=self.tasks_config['financial_evaluation_task'],
            # async_execution=True,
            output_file='financial_evaluation.md',
        )

    @task
    def technology_assessment_task(self) -> Task:
        return Task(
            config=self.tasks_config['technology_assessment_task'],
            # async_execution=True,
            output_file='technology_assessment.md',
        )

    @task
    def marketing_strategy_task(self) -> Task:
        return Task(
            config=self.tasks_config['marketing_strategy_task'],
            # async_execution=True,
            output_file='marketing_strategy.md',
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Consulting crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,    # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            memory=True,
            # chat_llm=llm,  # Using the defined LLM for chat interactions
            # embedder=None,  # Assuming no embedder is needed for this crew
            short_term_memory=None,  # Assuming no short term memory is needed
            entity_memory=None,  # Assuming no entity memory is needed
            long_term_memory=LongTermMemory(storage=LTMSQLiteStorage(db_path='consulting_memory.db'))
            
        )
