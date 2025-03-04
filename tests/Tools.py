from crewai_tools import BaseTool
class HumanTool(BaseTool):
    name: str = "Human interact"
    description: str = (
        "Ask the user questions to collect information."
    )

    def _run(self, argument: str) -> str:
        # Implementation goes here
        res = input(f"{argument} \n")
        return res