import os
from crewai import Agent
from textwrap import dedent
from langchain_openai import ChatOpenAI

"""
Creating Agents Cheat Sheet:
- Think like a boss. Work backwards from the goal and think which employee 
    you need to hire to get the job done.
- Define the Captain of the crew who orient the other agents towards the goal. 
- Define which experts the captain needs to communicate with and delegate tasks to.
    Build a top down structure of the crew.

Goal:
- Create a travel itinerary for the given date range with detailed per-day plans,
    including budget, packing suggestions, and safety tips.

Captain/Manager/Boss:
- Expert Travel Agent

Employees/Experts to hire:
- City Selection Expert 
- Local Tour Guide


Notes:
- Agents should be results driven and have a clear goal in mind
- Role is their job title
- Goals should actionable
- Backstory should be their resume
"""


class TravelAgents:
    def __init__(self):
        self.OpenAIGPT35 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
        self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4", temperature=0.7)

    def city_selection_expert(self, search_tools):
        return Agent(
            role="City Selection Expert",
            backstory=dedent(
                f"""Expert at analyzing travel data to pick ideal destinations"""
            ),
            goal=dedent(
                f"""Select the best cities based on weather, season, prices, and traveler interests"""
            ),
            tools=[search_tools],
            verbose=True,
            llm=self.OpenAIGPT35,
            max_iter=3,
        )

    def local_tour_guide(self, search_tools):
        return Agent(
            role="Local Tour Guide",
            backstory=dedent(
                f"""Knowledgeable local guide with extensive information
            about the city, it's attractions and customs"""
            ),
            goal=dedent(f"""Provide the BEST insights about the selected city"""),
            tools=[search_tools],
            verbose=True,
            llm=self.OpenAIGPT35,
            max_iter=3,
        )

    def expert_travel_agent(self, calculator_tools):
        return Agent(
            role="Expert Travel Agent",
            backstory=dedent(
                f"""Expert in travel planning and logistics. 
                I have decades of expereince making travel iteneraries."""
            ),
            goal=dedent(
                f"""
                        Create a travel itinerary for the given date range with detailed per-day plans,
                        include budget, packing suggestions, and safety tips. Always use only the inputs from the co-workers. Do not search anything on your own.
                        """
            ),
            tools=[calculator_tools],
            verbose=True,
            llm=self.OpenAIGPT35,
            max_iter=3,
        )
