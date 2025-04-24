from kafka.consumer import DefaultConsumer
from config.consumer_config import consumer_conf, consumer_subscriptions
from videoHandler.VideoService import VideoService
import json

class MyConsumer(DefaultConsumer):
    def msg_process(self, msg):
        
        json_string = msg.value().decode('utf-8')
        json_object = json.loads(json_string)
        
        video_handler = VideoService(json_object["video_path"])
        extracted_text = video_handler.extract_text_from_video()
        
        print(extracted_text)

if __name__ == "__main__":
    consumer = MyConsumer(consumer_conf, consumer_subscriptions)
    consumer.start_consume()
    print("Consumer started")
