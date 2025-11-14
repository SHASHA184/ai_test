from pydantic import BaseModel


class JokeRequest(BaseModel):
    topic: str


class JokeResponse(BaseModel):
    joke: str
