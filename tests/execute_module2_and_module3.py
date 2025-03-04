

#把module2的输出读进来，作为上下文/提示词
#工具查询namespace和pod

import os
from crewai import Agent, Task, Crew
from crewai_tools import BaseTool
from src.module2 import *




# class tool_pod_message(BaseTool):
#     name: str = "我的工具名称"'tool_pod_message'
#     description: str = "清晰描述此工具用于什么，您的代理将需要这些信息来使用它。"'获取节点系统信息'
#     def _run(self, argument: str) -> str:
#         # 实现在这里
#         return "自定义工具的结果"




yaml_agent = Agent(
    role='故障用例注入专家',
    goal='生成一个可以注入的yaml文件',
    backstory="""您是一位故障用例注入专家。
    您负责根据系统上下文信息，生成可执行用例的yaml文件。""",
    # tools=[tool_pod_message],
    verbose=True,
    allow_delegation=False,
    context=[task2]
)

#crew.kickoff(inputs)

task3 = Task(
    description=(
        "Select a fault injection tool based on your experience!"
        "Generate prompt words to give to the agent in the next stage."
    ),
    expected_output='生成yaml文件,其中pod是###,namespace是###',
    agent=yaml_agent,
)



crew = Crew(
    agents=[fault_expert,yaml_agent],
    tasks=[task2,task3],
    verbose=True,
    memory=True,
    planning=True  # Enable planning feature for the crew
)

print(crew.kickoff())