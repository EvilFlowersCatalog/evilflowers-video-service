from videoHandler.VideoService import VideoService


def main():
    video_path = "test_data/video_EN.mp4"
    video_service = VideoService(video_path)
    return video_service.extract_text_from_video()

if __name__ == "__main__":
    extracted_text = main()
    print("Extracted_text", extracted_text)
