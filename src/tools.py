# from crewai_tools import BaseTool
# class HumanTool(BaseTool):
#     name: str = "Human interact"
#     description: str = (
#         "Ask the user questions to collect information.The incoming parameter 'information_needed' is what information needs to be input by the person"
#     )
#
#     def _run(self, information_needed: str) -> str:
#         # Implementation goes here
#         res = input(f"{information_needed} \n")
#         return res

from typing import Type
from crewai.tools import BaseTool
from pydantic import BaseModel, Field

class MyToolInput(BaseModel):
    """Input schema for MyCustomTool."""
    information_needed: str = Field(..., description="What information needs to be input by the person.")

class HumanInputTool(BaseTool):
    name: str = "human_input"
    description: str = "Ask the user questions to collect information."
    args_schema: Type[BaseModel] = MyToolInput
    def _run(self, information_needed: str) -> str:
        # Implementation goes here
        res = input(f"{information_needed} \n")
        return res
