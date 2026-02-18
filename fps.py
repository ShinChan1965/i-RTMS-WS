# import time
# import cv2

# cap = cv2.VideoCapture(0)

# while True:
#     start_time = time.perf_counter()

#     ret, frame = cap.read()

#     # YOLO detection here
#     results = model(frame)

#     # DeepSORT tracking here

#     end_time = time.perf_counter()

#     delta = end_time - start_time
#     if delta > 0:
#         fps = 1 / delta
#         print("Real Processing FPS:", round(fps, 2))
import cv2
import time

video = cv2.VideoCapture(0)  # 0 for default camera
num_frames = 120
start = time.time()

for i in range(num_frames):
    ret, frame = video.read()

end = time.time()
seconds = end - start
fps = num_frames / seconds
print(f"Estimated FPS: {fps}")

video.release()
