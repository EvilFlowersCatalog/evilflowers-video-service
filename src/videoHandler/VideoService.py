import os
from videoHandler.AudioExtractor import AudioExtractor
from videoHandler.AudioProcessor import AudioProcessor


class VideoService:
    _instance = None
    audio_extractor: AudioExtractor
    audio_processor: AudioProcessor

    def __init__(self, video_path: str):
        if not hasattr(self, "initialized"):
            self.audio_extractor = AudioExtractor(video_path)
            self.audio_processor = AudioProcessor()
            self.initialized = True
        else:
            return self._instance
        
    def extract_text_from_video(self):
        audio = self.audio_extractor.extract_audio()

        temp_audio_path = "../../temp/temp_audio.mp3"
        os.makedirs(os.path.dirname(temp_audio_path), exist_ok=True)
        audio.write_audiofile(temp_audio_path)

        text = self.audio_processor.extract_text(temp_audio_path)
        
        os.remove(temp_audio_path)
        
        return text
