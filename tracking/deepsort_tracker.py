# from deep_sort_realtime.deepsort_tracker import DeepSort

# class DeepSORTTracker:
#     def __init__(self):
#         self.tracker = DeepSort(
#             max_age=30,
#             n_init=3,
#             nms_max_overlap=1.0
#         )

#     def update(self, detections, frame):
#         """
#         Input:
#         detections = [[x1,y1,x2,y2,conf], ...]
#         Output:
#         tracks with track_id and bbox
#         """
#         formatted = []

#         for d in detections:
#             x1, y1, x2, y2, conf = d
#             formatted.append(([x1, y1, x2 - x1, y2 - y1], conf, "person"))

#         tracks = self.tracker.update_tracks(formatted, frame=frame)
#         return tracks

# HARDCODE CONFIG FILE

# from deep_sort_realtime.deepsort_tracker import DeepSort

# class DeepSORTTracker:
#     def __init__(self):
#         self.tracker = DeepSort(
#             max_age=60,                 # 🔒 keep ID longer during occlusion
#             n_init=5,                   # 🔒 require 5 hits before confirming
#             max_cosine_distance=0.2,    # 🔒 stricter appearance matching
#             nn_budget=100,              # 🔒 better ReID memory
#             nms_max_overlap=0.7,
#             embedder="mobilenet",       # Stable & fast ReID
#             half=True,
#             bgr=True
#         )

#     def update(self, detections, frame):
#         formatted = []

#         for d in detections:
#             x1, y1, x2, y2, conf = d

#             formatted.append((
#                 [x1, y1, x2 - x1, y2 - y1],  # xywh
#                 conf,
#                 "person"                    # 🔒 single class
#             ))

#         return self.tracker.update_tracks(formatted, frame=frame)

# CONFIG PARAMETERS FROM CONFIG.PY

from deep_sort_realtime.deepsort_tracker import DeepSort

from config.config import (
    MAX_AGE,
    MIN_HITS,
    IOU_THRESHOLD,
    MAX_COSINE_DISTANCE,
    NN_BUDGET
)


class DeepSORTTracker:
    def __init__(self):
        self.tracker = DeepSort(
            max_age=MAX_AGE,
            n_init=MIN_HITS,
            max_cosine_distance=MAX_COSINE_DISTANCE,
            nn_budget=NN_BUDGET,
            nms_max_overlap=IOU_THRESHOLD,
            embedder="mobilenet",
            half=True,
            bgr=True
        )

    def update(self, detections, frame):
        """
        detections format:
        [[x1, y1, x2, y2, confidence], ...]
        """

        formatted = []

        for d in detections:
            x1, y1, x2, y2, conf = d

            formatted.append((
                [x1, y1, x2 - x1, y2 - y1],  # xywh
                conf,
                "person"
            ))

        return self.tracker.update_tracks(formatted, frame=frame)
