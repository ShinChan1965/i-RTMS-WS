import cv2
from config.config import CAMERA_INDEX, FRAME_WIDTH, FRAME_HEIGHT

class VideoStream:
    def __init__(self):
        self.cap = cv2.VideoCapture(CAMERA_INDEX)

    def read(self):
        ret, frame = self.cap.read()
        if not ret:
            return None

        frame = cv2.resize(frame, (FRAME_WIDTH, FRAME_HEIGHT))
        return frame

    def release(self):
        self.cap.release()
