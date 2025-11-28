import pydantic
import datetime

from google.adk import agents
from google.adk import tools
from google.adk.tools import agent_tool

class StructuredInformation(pydantic.BaseModel):
  """Contiene la información extraida de un artículo OSINT"""
  file_hashes:list[str] = pydantic.Field(description="Hashes de ficheros mencionados")
  cves: list[str] = pydantic.Field(description="cves mencionados")
  malware_names: list[str] = pydantic.Field(description="lista de malware mencionados")
  industrias: list[str] = pydantic.Field(description="Industrias atacadas")
  paises_atacados: list[str] = pydantic.Field(description="Paises atacados")
  fecha: str = pydantic.Field(description="Fecha en la que el artículo fue escrito en formato YYYY-MM-DD")
  autor: str = pydantic.Field(description="Autor del artículo")


scraper_agent = agents.LlmAgent(
  name="scraper_agent",
  instruction="Eres un experto extrayendo información de un artículo OSINT.",
  description="Util para extraer información de un artículo OSINT. Es necesario indicarle todos los campos que se quieren extraer.",
  tools=[tools.url_context],
  model="gemini-2.5-pro",
)


root_agent = agents.LlmAgent(
  name="osint_scraper_agent",
  instruction="Extrae la información estructurada del artículo OSINT.",
  model="gemini-2.5-pro",
  tools=[agent_tool.AgentTool(scraper_agent)],
  output_schema=StructuredInformation
)