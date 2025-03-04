from crewai import Crew,Process
from module1 import fault_analyst, task1
from module2 import fault_expert, task2
from module3 import fault_engineer, task3
from dotenv import load_dotenv

load_dotenv()
# Instantiate your crew with a sequential process
crew = Crew(
    agents=[fault_analyst, fault_expert, fault_engineer],
    tasks=[task1, task2, task3],
    process=Process.sequential,
    # verbose=True,
    # memory=True,
    # planning=True  # Enable planning feature for the crew
)
inputs = {
    'fault': 'Please help me inject a network-level fault to the order service',
    'service': 'order',
    'fault_type': 'communication',
}

# Get your crew to work!
result = crew.kickoff(inputs)

print("######################")
print(result)