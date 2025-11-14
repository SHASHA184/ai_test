from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

from openai_connection import model

text = """Tell me a joke about {topic}."""

prompt = ChatPromptTemplate.from_template(text)

parser = StrOutputParser()


class JokeChain:
    def __init__(self, model, prompt, parser):
        self.model = model
        self.prompt = prompt
        self.parser = parser

    @property
    def chain(self):
        return self.prompt | self.model | self.parser

    def run(self, topic):
        return self.chain.invoke({"topic": topic})


if __name__ == "__main__":
    joke_chain = JokeChain(model, prompt, parser)
    joke = joke_chain.run("computers")
    print(joke)
