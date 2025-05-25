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

manager = LLM(
    model="gemini/gemini-2.0-flash",
    temperature=0.5,
)

linkup_search = LinkupSearchTool(api_key=os.getenv('LINKUP_API_KEY'))

@CrewBase
class IdeaValidator():
    """Idea Validator crew for validating business ideas and building personas."""

    agents_config = 'config/agents.yaml'  # Assume this is a dict loaded from YAML
    tasks_config = 'config/tasks.yaml'    # Assume this is a dict loaded from YAML

    @agent
    def idea_evaluator(self) -> Agent:
        return Agent(
            config=self.agents_config['idea_evaluator'],
            verbose=True,
            # llm=llm,
            tools=[
                ScrapeWebsiteTool(),
                linkup_search,
            ],
            # allow_delegation=True
        )

    @agent
    def customer_persona_builder(self) -> Agent:
        return Agent(
            config=self.agents_config['customer_persona_builder'],
            verbose=True,
            # llm=llm,
            tools=[
                ScrapeWebsiteTool(),
                linkup_search,
            ],
            # allow_delegation=True
        )

    @agent
    def lean_canvas_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['lean_canvas_agent'],
            verbose=True,
            # llm=llm,
            tools=[
                ScrapeWebsiteTool(),
                linkup_search,
            ],
            # allow_delegation=True
        )

    @agent
    def mvp_recommender(self) -> Agent:
        return Agent(
            config=self.agents_config['mvp_recommender'],
            verbose=True,
            # llm=llm,
            tools=[
                ScrapeWebsiteTool(),
                linkup_search,
            ],
            # allow_delegation=True
        )
        
    @agent
    def business_model_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['business_model_analyst'],
            verbose=True,
            # llm=llm,
            tools=[
                ScrapeWebsiteTool(),
                linkup_search,
            ],
            # allow_delegation=True
        )

    @task
    def evaluate_idea_task(self) -> Task:
        return Task(
            config=self.tasks_config['evaluate_idea_task'],
            # async_execution=True,
        )

    @task
    def build_persona_task(self) -> Task:
        return Task(
            config=self.tasks_config['build_persona_task'],
            # async_execution=True,
        )

    @task
    def lean_canvas_task(self) -> Task:
        return Task(
            config=self.tasks_config['lean_canvas_task'],
            # async_execution=True,
        )

    @task
    def mvp_suggestion_task(self) -> Task:
        return Task(
            config=self.tasks_config['mvp_suggestion_task'],
            # async_execution=True,
        )
    
    @task
    def business_model_task(self) -> Task:
        return Task(
            config=self.tasks_config['business_model_task'],
            # async_execution=True,
        )
        
    

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,    # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            memory=True,
            chat_llm=llm,  # Using the defined LLM for chat interactions
            embedder=None,  # Assuming no embedder is needed for this crew
            short_term_memory=None,  # Assuming no short term memory is needed
            entity_memory=None,  # Assuming no entity memory is needed
            long_term_memory=LongTermMemory(storage=LTMSQLiteStorage(db_path='idea_validation_memory.db'))
            
        )
