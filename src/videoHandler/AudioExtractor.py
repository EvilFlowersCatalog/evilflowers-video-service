import os
from moviepy.editor import VideoFileClip, AudioFileClip


class AudioExtractor:
    
    def __init__(self, video_path: str):
        self._validate_document_path(video_path)
        self.video_path = video_path

    def extract_audio(self):
        return VideoFileClip(self.video_path).audio

    ##
    # Private functions
    def _validate_document_path(self, video_path: str):
        assert os.path.exists(
            video_path
        ), f"Document path did not found: {video_path}"
