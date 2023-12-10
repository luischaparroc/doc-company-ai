from typing import Any, List

from abc import ABC, abstractmethod


class AbstractLLMSystem(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def request(self, messages: List[Any], **kwargs: Any):
        pass
