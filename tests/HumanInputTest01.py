from dotenv import load_dotenv
import os
from crewai import Agent, Task, Crew
from crewai_tools import SerperDevTool
from Tools import HumanTool

load_dotenv()

# Loading Tools
human_tool=HumanTool()
# Define your agents with roles, goals, tools, and additional attributes
fault_analyser = Agent(
    role='Fault Analyst',
    goal='Understand error messages provided to users',
    backstory=(
        "You are an experienced failure use case design expert. "
        "You need to understand and prompt users to complete relevant information that requires fault injection."
        "But you don’t need to design use cases, you just need to help complete the user’s fault injection needs."
        "You can call human_tool to let users enter missing information and ultimately get complete information.Calling the tool requires passing in the information you want the user to input."
    ),
    verbose=True,
    allow_delegation=False,
    tools=[human_tool]
)

# Create tasks for your agents
task1 = Task(
    description=(
        "Understand and organize the fault use case generation requirements input by the user."
        "Prompt the user to input again if the information provided by the user is not enough."
        "User failure use case requirements: {fault}"
    ),
    expected_output='Extract key information such as target service of fault injection, injected fault type, injected fault mode, etc.',
    agent=fault_analyser,
    tools=[human_tool],
    human_input=True
)

# Instantiate your crew with a sequential process
crew = Crew(
    agents=[fault_analyser],
    tasks=[task1],
    verbose=True,
    memory=True,
    planning=True  # Enable planning feature for the crew
)
inputs = {
        'fault': 'Please help me inject a communication type fault.'
    }

# Get your crew to work!
result = crew.kickoff(inputs)

print("######################")
print(result)


