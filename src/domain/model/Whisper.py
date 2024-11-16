from typing import Union
import torch
import numpy as np
from domain.base.ModelInterface import ModelInterface
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline

class Whisper(ModelInterface):

    _torch_dtype: torch.dtype
    _model_id: str
    _model: AutoModelForSpeechSeq2Seq
    _processor: AutoProcessor
    _device: str

    def __init__(self):
        _model_id = "openai/whisper-large-v3"
        
        self._device = "cuda:0" if torch.cuda.is_available() else "cpu"
        self._torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32
        self._model = AutoModelForSpeechSeq2Seq.from_pretrained(
            _model_id, torch_dtype=self._torch_dtype, low_cpu_mem_usage=True, use_safetensors=True)
        self._processor = AutoProcessor.from_pretrained(_model_id)
        self._model.to(self._device)


    def audio_to_text(self, audio_input: str) -> str:
        """
        Process audio input and convert to text.
        
        Args:
            audio_input: Can be either:
                - Path to audio file (str)
                - Raw audio array (np.ndarray)
                - Audio waveform array (np.ndarray)
        """
        pipe = pipeline(
            "automatic-speech-recognition",
            model=self._model,
            tokenizer=self._processor.tokenizer,
            feature_extractor=self._processor.feature_extractor,
            torch_dtype=self._torch_dtype,
            device=self._device,
        )

        result = pipe(audio_input, return_timestamps=True)
        return result["text"]
