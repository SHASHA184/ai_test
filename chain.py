from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI


class JokeChain:
    def __init__(self, model_name: str, temperature: float, openai_api_key: str):
        self.model = ChatOpenAI(
            model=model_name,
            temperature=temperature,
            api_key=openai_api_key
        )
        self.prompt = ChatPromptTemplate.from_template(
            "Tell me a joke about {topic}."
        )
        self.parser = StrOutputParser()

    @property
    def chain(self):
        return self.prompt | self.model | self.parser

    def generate_joke(self, topic: str) -> str:
        return self.chain.invoke({"topic": topic})
