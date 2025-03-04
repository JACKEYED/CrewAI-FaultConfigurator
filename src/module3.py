import os
from pathlib import Path

from crewai import Agent, Task, Crew
from crewai.knowledge.source.text_file_knowledge_source import TextFileKnowledgeSource
from crewai_tools import BaseTool

chaosmesh_file_path = Path("/home/leo/code/text2fault/knowledge/chaomesh_yaml.txt")
chaosmesh_doc_source =TextFileKnowledgeSource(file_path = chaosmesh_file_path, metadata={"preference": "personal"})

fault_engineer = Agent(
    role='Fault case Generation Agent',
    goal='Based on the prompt template, generate a solution that can be used for fault injection tools.',
    backstory="""
    You are an experienced fault injection expert.
    You need to design a solution according to the prompt template.
    You must not arbitrarily modify the information in the prompt template.
    For example, when injecting into a cloud environment, you would generate a fault injection configuration YAML file according to the previous stage，
    when injecting into physical hosts and Java virtual machines, you must use command-line code according to the previous stage. 
    You need to determine the specifics based on your situation.
    Please be sure to execute that when generating the solution,only the code is required,without any explanatory statements.
    Apart from the above context and other task information, you don't need to consider anything else, just focus on generating this solution.
    """,
    verbose=True,
    allow_delegation=False,
    knowledge_sources=[chaosmesh_doc_source],
)


task3 = Task(
    description=("""
    generate a command-line code or a fault injection configuration YAML file according to the previous stage.
    """
    ),
    expected_output='the pod is `user-service-pod` and the namespace is `testing-namespace`.',
    agent=fault_engineer
)


