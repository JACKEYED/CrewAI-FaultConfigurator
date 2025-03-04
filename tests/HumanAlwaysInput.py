from dotenv import load_dotenv

from crewai import Agent, Task, Crew, Process
from Tools import HumanTool
from crewai.tasks.task_output import TaskOutput

load_dotenv()
# Set Model


# Loading Human Tools
# human_tools = load_tools(["human"])

# Agents definition
interviewer = Agent(
  role='Interviwer',
  goal='making questions about business to human',
  backstory="""You are an interviewer of business man.""",
  verbose=True,
  allow_delegation=False,
  tools=HumanTool
)

writer = Agent(
  role='Writer',
  goal=' Summarizing interview',
  backstory="""You are a writer and your expertise lies in summarizing interviews.""",
  verbose=True,
  allow_delegation=False,
)

# Tasks definition
interviewer_task = Task(
  description=f"""
Your task is to interview successful entrepreneurs. 
Ask three business questions. Ask one question at a time.
When three questions have been answered by the interviewee, conclude by responding with a list of questions and answers, followed by "finish" on a new line.
To ask a question, use the "human" tool and provide the question to be asked as the "Action Input".
""",
  max_inter=3,
  expected_output="a coherent question",
  agent=interviewer,
  tools=HumanTool
)

writer_task = Task(
  description=f"""
Summarize the content of the provided interview
""",
  max_inter=3,
  agent=writer,
  expected_output="a coherent summary",
  context=[interviewer_task]
)

items_crew = Crew(
  agents=[interviewer,writer],
  tasks=[interviewer_task, writer_task],
  process=Process.sequential,
  memory=True,
  verbose=True,
  full_output=True,
)

# Get your crew to work!
response = items_crew.kickoff()

print("#########")
print(response)
print("#########")