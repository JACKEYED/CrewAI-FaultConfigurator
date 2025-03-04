from crewai import Agent, Task, Crew
from tools import HumanInputTool
from dotenv import load_dotenv
from crewai.knowledge.source.text_file_knowledge_source import TextFileKnowledgeSource
from pathlib import Path

load_dotenv()

fault_introduce_file_path = Path("../knowledge/fault_introduce.txt")
fault_introduce_doc_source =TextFileKnowledgeSource(file_path = fault_introduce_file_path, metadata={"preference": "personal"})

# Loading Tools
human_tool=HumanInputTool()
# Define your agents with roles, goals, tools, and additional attributes
fault_analyst = Agent(
    role='Fault Requirement Analyst',
    goal='Understand the fault information provided by the user and design it into primary failure use cases.',
    backstory=("""
        You are an experienced requirement analyst for fault injection.
        You are especially skilled at gathering user requirements and designing them into primary failure use cases.
        You need to understand and guide the user to provide relevant information to generate the failure use case.
        If the user asks you to complete the failure information on your own, you need to use your extensive experience to reasonably refine the information.        
        You don't need to consider other matters, you only need to assist the user in completing and refining their needs.
    """
    ),
    verbose=True,
    allow_delegation=False,
    tools=[human_tool],
    knowledge_sources=[fault_introduce_doc_source],
)

# Create tasks for your agents
task1 = Task(
    description=("""
        1. User failure use case requirements: {fault}.\n
        2. If necessary, you can call human_tool to let users enter missing information and ultimately get complete information.Calling the tool requires passing in the information you want the user to input.\n
        3. Extract key information such as target service of fault injection, injected fault type, injected fault mode, and necessary arguments information.\n     
    """
    ),
    expected_output="""
    A preliminary requirements document generated from the key fault injection information extracted from the user.
    """,
    agent=fault_analyst,
    tools=[human_tool],
    human_input=True
)




