from google.adk import agents
from google.adk import code_executors


root_agent = agents.LlmAgent(
  name="malware_analysis_agent",
  instruction="Eres un experto en ciberseguridad. Ayuda al analista en inteligencia de ciberamenazas.",
  model="gemini-2.5-pro",
  tools=[],
  code_executor=code_executors.BuiltInCodeExecutor()
)