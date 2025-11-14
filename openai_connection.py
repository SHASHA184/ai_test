from langchain.agents import create_agent
from langchain_openai import ChatOpenAI

from config import settings

model = ChatOpenAI(model="gpt-4o", temperature=settings.llm_temperature)
agent = create_agent(model)
