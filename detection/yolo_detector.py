# from config.config import CONFIDENCE_THRESHOLD

# class YOLODetector:
#     def __init__(self, model):
#         self.model = model

#     def detect(self, frame):
#         detections = []
#         results = self.model(frame, stream=True, conf=CONFIDENCE_THRESHOLD)

#         for r in results:
#             for box in r.boxes:
#                 cls = int(box.cls[0])
#                 conf = float(box.conf[0])

#                 # PERSON ONLY
#                 if cls != 0:
#                     continue

#                 x1, y1, x2, y2 = map(int, box.xyxy[0])

#                 # 🚫 REMOVE VERY SMALL BOXES (NOISE)
#                 if (x2 - x1) * (y2 - y1) < 1500:
#                     continue

#                 detections.append([x1, y1, x2, y2, conf])

#         return detections

# DETECTING PERSON ONLY

from config.config import CONFIDENCE_THRESHOLD

class YOLODetector:
    def __init__(self, model):
        self.model = model

    def detect(self, frame):
        detections = []

        # 🔒 Instruct YOLO to detect PERSON ONLY (class 0)
        results = self.model(
            frame,
            stream=True,
            conf=CONFIDENCE_THRESHOLD,
            classes=[0],  # 👈 PERSON ONLY
            half=True,
            device=0, 
            verbose=False
        )

        for r in results:
            for box in r.boxes:
                conf = float(box.conf[0])
                x1, y1, x2, y2 = map(int, box.xyxy[0])

                # 🚫 Remove very small boxes (noise)
                if (x2 - x1) * (y2 - y1) < 1500:
                    continue

                detections.append([x1, y1, x2, y2, conf])

        return detections
