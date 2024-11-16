from abc import ABC, abstractmethod

class ModelInterface(ABC):
    @abstractmethod
    def audio_to_text(self, audio: dict) -> str:
        pass