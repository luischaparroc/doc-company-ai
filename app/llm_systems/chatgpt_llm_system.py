import os
from typing import Any, List

from openai import OpenAI

from app.llm_systems.abstract_llm_system import AbstractLLMSystem
from app.llm_systems.messages_config import ChatGPTMessage


class ChatGPTLLMSystem(AbstractLLMSystem):

    def __init__(self, model: str = 'gpt-3.5-turbo'):
        super().__init__()
        self.model = model

        openai_api_key = os.environ.get('OPENAI_API_KEY')
        if not openai_api_key:
            raise ValueError('"OPENAI_API_KEY" environment variable not set. Please, set this env variable')

        self._openai_api_key = openai_api_key
        self._client = OpenAI(
            api_key=openai_api_key
        )

    def request(self, messages: List[ChatGPTMessage], temperature: int = 0, **kwargs: Any):
        response = self._client.chat.completions.create(
            model=self.model,
            messages=[message.model_dump() for message in messages],
            temperature=temperature
        )
        return response.choices[0].message.content
