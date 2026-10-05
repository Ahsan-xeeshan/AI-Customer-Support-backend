from pydantic import BaseModel


class Message(BaseModel):
    role: str
    content: str

class SupportRequest(BaseModel):
    message: str
    history: list[Message] = []