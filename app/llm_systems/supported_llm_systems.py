from enum import Enum
from typing import Any

from app.llm_systems.abstract_llm_system import AbstractLLMSystem
from app.llm_systems.chatgpt_llm_system import ChatGPTLLMSystem


class SupportedLLMSystems(Enum):
    CHATGPT = 'CHATGPT'

    def __init__(self, llm_system: str):
        self.llm_system = llm_system
        self.supported_llms = {
            'CHATGPT': ChatGPTLLMSystem
        }

    def get_llm_system(self, **kwargs: Any) -> AbstractLLMSystem:
        llm_system = self.supported_llms.get(self.llm_system)(**kwargs)

        if not llm_system:
            raise ValueError(
                f'Unsupported LLM System: {self.llm_system}. Supported systems: {self.supported_llms.keys()}'
            )

        return llm_system
