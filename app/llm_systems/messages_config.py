from pydantic import BaseModel


class ChatGPTMessage(BaseModel):
    content: str
    role: str
