# 分析故障需求，选择故障工具、故障组合模式等生成提示模板
from crewai import Agent, Task


knowledge_ChaosMesh = """
    ChaosMesh is a cloud-native chaos engineering platform.
    ChaosMesh offers various chaos injection tools, mainly divided into Kubernetes environments and physical machine environments.
    1. In Kubernetes environments, injection is configured using YAML files
    2. while in physical machine environments, the chaosd CLI offered by ChaosMesh is used to implement injection and recovery functions.
"""


knowledge_ChaosBlade = """
    ChaosBlade is a lightweight and flexible chaos engineering experiment toolkit.
    ChaosBlade supports injection experiments in three environments: physical hosts, Kubernetes, and JVM. The injection methods include:  
    1. **CLI Command Mode**: Execute experiments directly through CLI commands, applicable to host , jvm and Kubernetes environments.  
    2. **YAML File Mode**: Used only for Kubernetes cluster experiments by creating experiments with YAML configuration files or defining ChaosBlade CRD resources.  
    3. **Server Mode**: Start the ChaosBlade tool as a server using `./blade server start`, and issue commands via HTTP remote calls.
"""

fault_expert = Agent(
    role='Prompt Generation Agent',
    goal='Analyze the failure use case to generate a prompt template.',
    backstory=("""
        You are a failure Prompt Generation Agent.
        You are responsible for generating the prompt template based on failure use cases.
        You have extensive experience in judging what fault injection tools need to be used for different type of faults.
        You don't need to consider anything else, just focus on completing the prompt template.
        You can generate specific prompt projects based on different fault injection tools and fault use cases, which can be directly used by subsequent agents.
        There are many OSS fault injection tools for you to choose from, such as: ChaosMesh, ChaosBlade, Chaoskube, PowerfulSeal,etc.
    """
    + knowledge_ChaosMesh + '\n'
    + knowledge_ChaosBlade + '\n'
    ),
    verbose=True,
    allow_delegation=False,
)

# Create tasks for your agents
task2 = Task(
    # 你需要分析故障需求，选择故障工具、故障组合模式等生成提示模板，故障工具需要你选择后向我询问
    # 人类工具是否需要？
    description=("""
        1. Select the most appropriate tool for the current injection based on your experience(you need to explain to the user why you chose it).
    """
    ),
    # description=("""
    #         1. Select the most appropriate tool for the current injection based on your experience(you need to explain to the user why you chose it).\n
    #         3. To make the prompt more general, you do not need to generate a specific configuration file.\n
    #         4. Provide the execution methods for the corresponding tools and injection environments.\n
    #         2. Generate prompt words to give to the agent in the next stage base on above description.\n
    #     """
    #     ),
    expected_output="""
    A failure prompt template from the preliminary requirements document.'
    """,
    agent=fault_expert,
)
