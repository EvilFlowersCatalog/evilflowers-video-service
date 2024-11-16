from abc import ABC, abstractmethod

class ModelInterface(ABC):
    @abstractmethod
    def predict(self, image: Image.Image) -> str:
        pass