from config.Config import Config
from domain.model.Whisper import Whisper
from typing import Union
import numpy as np

class AudioProcessor:
    
    config: Config = Config()

    def __init__(self):
        self._audio_to_text_processor = self._load_audio_to_text_processor()


    def extract_text(self, audio_input: str) -> str:
        return self._audio_to_text_processor.audio_to_text(audio_input)

    def _load_audio_to_text_processor(self):
        if self.config.get_config()['AUDIO_PROCESSOR_MODEL'] == 'Whisper':
            model = Whisper()
        else:
            raise ValueError(f"Model type {self.config.get_config()['AUDIO_PROCESSOR_MODEL']} not supported")
        return model
