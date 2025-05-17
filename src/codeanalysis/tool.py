from crewai.tools import BaseTool


class Codeanalysis(BaseTool):
    name: str = "Code Analysis"
    description: str = "You are expert in software code analysis and extracting class, function and module. Also able to form the relationship between it"

    def _run(self, argument: str) -> str:
        # Your tool's logic here
        return "Tool's result"
