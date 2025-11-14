from fastapi import FastAPI
from schemas import JokeRequest, JokeResponse
from config import settings
from chain import JokeChain
from mangum import Mangum

app = FastAPI()
joke_chain = JokeChain(
    model_name=settings.llm_model_name,
    temperature=settings.llm_temperature,,
    openai_api_key=settings.openai_api_key,
)

@app.post("/generate_joke", response_model=JokeResponse)
async def generate_joke(request: JokeRequest):
    joke = joke_chain.generate_joke(request.topic)
    return JokeResponse(joke=joke)

handler = Mangum(app)
