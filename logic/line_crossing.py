import cv2
from config.config import LINE_Y

class LineCrossing:
    def __init__(self):
        self.previous_positions = {}

    def check_crossing(self, track_id, centroid_y):
        if track_id not in self.previous_positions:
            self.previous_positions[track_id] = centroid_y
            return None

        prev_y = self.previous_positions[track_id]
        self.previous_positions[track_id] = centroid_y

        if prev_y < LINE_Y and centroid_y >= LINE_Y:
            return "IN"

        if prev_y > LINE_Y and centroid_y <= LINE_Y:
            return "OUT"

        return None

    # 🔹 ADD THIS
    def draw_line(self, frame):
        h, w, _ = frame.shape
        cv2.line(frame, (0, LINE_Y), (w, LINE_Y), (0, 255, 255), 2)

