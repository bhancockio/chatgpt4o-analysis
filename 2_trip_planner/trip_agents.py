from crewai import Agent
from langchain_openai import ChatOpenAI

from tools.calculator_tools import CalculatorTools
from tools.search_tools import SearchTools


class TripAgents():
    def __init__(self):
        self.llm = ChatOpenAI(
            model="gpt-4o"
            # model="gpt-4-turbo"
        )

    def city_selection_agent(self):
        return Agent(
            role='City Selection Expert',
            goal='Select the best city based on weather, season, and prices',
            backstory='An expert in analyzing travel data to pick ideal destinations',
            tools=[
                SearchTools.search_internet,
            ],
            llm=self.llm,
            verbose=True)

    def local_expert(self):
        return Agent(
            role='Local Expert at this city',
            goal='Provide the BEST insights about the selected city',
            backstory="""A knowledgeable local guide with extensive information
        about the city, it's attractions and customs""",
            tools=[
                SearchTools.search_internet,
            ],
            llm=self.llm,
            verbose=True)

    def travel_concierge(self):
        return Agent(
            role='Amazing Travel Concierge',
            goal="""Create the most amazing travel itineraries with budget and 
        packing suggestions for the city""",
            backstory="""Specialist in travel planning and logistics with 
        decades of experience""",
            tools=[
                SearchTools.search_internet,
                CalculatorTools.calculate,
            ],
            llm=self.llm,
            verbose=True)
