from crewai import Agent, Crew, Process, Task 
from crewai.project import CrewBase, agent, crew, task 
from crewai.knowledge.source.string_knowledge_source import StringKnowledgeSource
from src.journalist_crew.providers import deepseek_v3, mistral_small
from src.journalist_crew.tools import search_engine_tool , read_json_tool , web_scraping_tool
import os
from src.journalist_crew.models import AllSearchResults , AllExtractedArticles

# Create a knowledge source
company_context = StringKnowledgeSource(
    content="""
            TestAi is a digital newspaper focused on publishing articles and analytical content about the latest developments in technology 
            Its motto is: "Towards a broader technological horizon."
            It publishes daily articles covering innovations, reviews of digital tools, and insights into the future of AI.
            """
)


@CrewBase
class ArticleMakingCrew:
    """
    Article Making Crew for making articles about any given topic.
    Args:
        topic (str): The topic for which to generate articles and research files.
    """
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def web_research_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['web_research_agent'],
            allow_delegation=False,
            verbose=True,
            llm=mistral_small,
            tools=[search_engine_tool]
        )
    
    @task
    def web_research_task(self) -> Task:
        return Task(
            config=self.tasks_config['web_research_task'],
            agent=self.web_research_agent(),
            output_json=AllSearchResults,
            output_file = os.path.join(os.path.dirname(__file__), f"research/step_one_research_topic.json")
        )

    @agent
    def scraper_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['scraper_agent'],
            allow_delegation=False,
            verbose=True,
            llm=mistral_small,
            tools=[read_json_tool, web_scraping_tool]
        )

    @task
    def scraper_task(self) -> Task:
        return Task(
            config=self.tasks_config['scraper_task'],
            agent=self.scraper_agent(),
            output_json=AllExtractedArticles,
            output_file = os.path.join(os.path.dirname(__file__), f"research/step_two_extracted_articles.json")
        )

    @agent
    def article_writer_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['article_writer_agent'],
            allow_delegation=False,
            verbose=True,
            llm=deepseek_v3,
            tools=[read_json_tool]
        )

    @task
    def article_writer_task(self)-> Task:
        return Task(
            config=self.tasks_config['article_writer_task'],
            agent=self.article_writer_agent(),
            allow_delegation=False,
            output_file = os.path.join(os.path.dirname(__file__), f"results/final_article.md")
        )

    @crew
    def crew(self) -> Crew:
        """
        Creates the research crew
        """
        return Crew(
            agents=self.agents,  
            tasks=self.tasks,  
            process=Process.sequential,
            verbose=True, 
            knowledge_sources=[company_context],
        )