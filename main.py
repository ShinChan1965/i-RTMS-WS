#AUTO START MODE
# VIDEO OUTPUT + DB CONNECTION
import cv2
from ultralytics import YOLO

from camera.video_stream import VideoStream
from detection.yolo_detector import YOLODetector
from tracking.deepsort_tracker import DeepSORTTracker
from logic.line_crossing import LineCrossing
from logic.counter import PassengerCounter
from config.config import LINE_Y

# -------------------------------
# MODE SWITCH
# -------------------------------
DEBUG_MODE = True   # True = Debug | False = Deployment


def main():
    # --------------------------------
    
    # INITIALIZATION
    # --------------------------------
    video = VideoStream()
    yolo = YOLODetector(YOLO("yolov8n.pt"))
    tracker = DeepSORTTracker()
    line = LineCrossing()
    counter = PassengerCounter()

    current_stop = "Surandai"
    stop_index = 1

    print("🚍 Passenger Counting System Started")

    if DEBUG_MODE:
        print("🧪 Running in DEBUG MODE")
        print("Press 'n' → Next stop | Press 'q' → Quit")
    else:
        print("🚀 Running in DEPLOYMENT MODE (Auto-start)")

    try:
        while True:
            # --------------------------------
            # READ FRAME
            # --------------------------------
            frame = video.read()
            if frame is None:
                print("❌ Camera feed lost")
                break

            # --------------------------------
            # YOLO DETECTION
            # --------------------------------
            detections = yolo.detect(frame)

            # --------------------------------
            # DEEPSORT TRACKING
            # --------------------------------
            tracks = tracker.update(detections, frame)

            # --------------------------------
            # DRAW VIRTUAL LINE (DEBUG ONLY)
            # --------------------------------
            if DEBUG_MODE:
                cv2.line(
                    frame,
                    (0, LINE_Y),
                    (frame.shape[1], LINE_Y),
                    (0, 0, 255),
                    2
                )

            # --------------------------------
            # PROCESS TRACKS
            # --------------------------------
            for track in tracks:
                if not track.is_confirmed():
                    continue

                track_id = track.track_id
                x1, y1, x2, y2 = map(int, track.to_ltrb())
                centroid_y = (y1 + y2) // 2

                direction = line.check_crossing(track_id, centroid_y)

                if direction:
                    counter.update(
                        track_id,
                        direction,
                        stop=current_stop,
                        stop_index=stop_index
                    )

                    print(
                        f"[DB UPDATE] ID {track_id} → {direction} "
                        f"at stop {current_stop}"
                    )

                # DEBUG visuals only
                if DEBUG_MODE:
                    cv2.rectangle(frame, (x1, y1), (x2, y2),
                                  (0, 255, 0), 2)
                    cv2.putText(
                        frame,
                        f"ID {track_id}",
                        (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.6,
                        (0, 255, 0),
                        2
                    )

            # --------------------------------
            # DISPLAY INFO (DEBUG ONLY)
            # --------------------------------
            if DEBUG_MODE:
                entered, exited, current = counter.get_counts()

                cv2.putText(frame, f"Entered: {entered}", (20, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                            (255, 255, 255), 2)

                cv2.putText(frame, f"Exited: {exited}", (20, 60),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                            (255, 255, 255), 2)

                cv2.putText(frame, f"Inside: {current}", (20, 90),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                            (255, 255, 255), 2)

                cv2.putText(frame, f"Stop: {current_stop}", (20, 120),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                            (0, 255, 255), 2)

                cv2.imshow("Passenger Counting System", frame)

                key = cv2.waitKey(1) & 0xFF

                if key == ord('n'):
                    counter.store_stop_data(current_stop, stop_index)
                    stop_index += 1
                    current_stop = f"Stop_{stop_index}"
                    print(f"📍 Reached new stop → {current_stop}")

                elif key == ord('q'):
                    print("🛑 Exiting system")
                    break

    except KeyboardInterrupt:
        print("\n🛑 Interrupted")

    finally:
        counter.store_stop_data(current_stop, stop_index)
        video.release()

        if DEBUG_MODE:
            cv2.destroyAllWindows()

        print("✅ MongoDB updated")
        print("📦 Resources released")


if __name__ == "__main__":
    main()


# #VIDEO OUTPUT+DB CONNECTION

# import cv2
# from ultralytics import YOLO

# from camera.video_stream import VideoStream
# from detection.yolo_detector import YOLODetector
# from tracking.deepsort_tracker import DeepSORTTracker
# from logic.line_crossing import LineCrossing
# from logic.counter import PassengerCounter
# from config.config import LINE_Y

# def main():
#     # --------------------------------
#     # INITIALIZATION
#     # --------------------------------
#     video = VideoStream()
#     yolo = YOLODetector(YOLO("yolov8n.pt"))
#     tracker = DeepSORTTracker()
#     line = LineCrossing()
#     counter = PassengerCounter()

#     # Stop info (can be GPS-based later)
#     current_stop = "Surandai"
#     stop_index = 1

#     print("🚍 Passenger Counting System Started")
#     print("Press 'n' → Next stop | Press 'q' → Quit")

#     try:
#         while True:
#             # --------------------------------
#             # READ FRAME
#             # --------------------------------
#             frame = video.read()
#             if frame is None:
#                 print("❌ Camera feed lost")
#                 break

#             # --------------------------------
#             # YOLO DETECTION
#             # --------------------------------
#             detections = yolo.detect(frame)

#             # --------------------------------
#             # DEEPSORT TRACKING
#             # --------------------------------
#             tracks = tracker.update(detections, frame)

#             # --------------------------------
#             # DRAW VIRTUAL LINE
#             # --------------------------------
#             cv2.line(
#                 frame,
#                 (0, LINE_Y),
#                 (frame.shape[1], LINE_Y),
#                 (0, 0, 255),
#                 2
#             )

#             # --------------------------------
#             # PROCESS TRACKS
#             # --------------------------------
#             for track in tracks:
#                 if not track.is_confirmed():
#                     continue

#                 track_id = track.track_id
#                 x1, y1, x2, y2 = map(int, track.to_ltrb())

#                 # Draw bounding box
#                 cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

#                 # Draw ID
#                 cv2.putText(
#                     frame,
#                     f"ID {track_id}",
#                     (x1, y1 - 10),
#                     cv2.FONT_HERSHEY_SIMPLEX,
#                     0.6,
#                     (0, 255, 0),
#                     2
#                 )

#                 # Centroid
#                 centroid_y = (y1 + y2) // 2

#                 # Check line crossing
#                 direction = line.check_crossing(track_id, centroid_y)

#                 if direction:
#                     counter.update(
#                         track_id,
#                         direction,
#                         stop=current_stop,
#                         stop_index=stop_index
#                     )

#                     print(
#                         f"[DB UPDATE] ID {track_id} → {direction} "
#                         f"at stop {current_stop}"
#                     )

#             # --------------------------------
#             # DISPLAY COUNTS
#             # --------------------------------
#             entered, exited, current = counter.get_counts()

#             cv2.putText(frame, f"Entered: {entered}", (20, 30),
#                         cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

#             cv2.putText(frame, f"Exited: {exited}", (20, 60),
#                         cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

#             cv2.putText(frame, f"Inside: {current}", (20, 90),
#                         cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

#             cv2.putText(frame, f"Stop: {current_stop}", (20, 120),
#                         cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)

#             # --------------------------------
#             # SHOW VIDEO
#             # --------------------------------
#             cv2.imshow("Passenger Counting System", frame)

#             # --------------------------------
#             # KEY CONTROLS
#             # --------------------------------
#             key = cv2.waitKey(1) & 0xFF

#             if key == ord('n'):   # next stop
#                 counter.store_stop_data(current_stop, stop_index)
#                 stop_index += 1
#                 current_stop = f"Stop_{stop_index}"
#                 print(f"📍 Reached new stop → {current_stop}")

#             elif key == ord('q'):  # quit
#                 print("🛑 Exiting system")
#                 break

#     except KeyboardInterrupt:
#         print("\n🛑 Interrupted by user")

#     finally:
#         # Save last stop data
#         counter.store_stop_data(current_stop, stop_index)

#         video.release()
#         cv2.destroyAllWindows()

#         print("✅ MongoDB updated")
#         print("📦 Resources released")


# if __name__ == "__main__":
#     main()

#TERMINAL OUTPUT + DB CONNECTION

# from ultralytics import YOLO

# from camera.video_stream import VideoStream
# from detection.yolo_detector import YOLODetector
# from tracking.deepsort_tracker import DeepSORTTracker
# from logic.line_crossing import LineCrossing
# from logic.counter import PassengerCounter


# def main():
#     # -----------------------------
#     # INITIALIZATION
#     # -----------------------------
#     video = VideoStream()
#     yolo = YOLODetector(YOLO("yolov8n.pt"))
#     tracker = DeepSORTTracker()
#     line = LineCrossing()
#     counter = PassengerCounter()

#     # Stop-related info (can be GPS-based later)
#     current_stop = "Koyambedu"
#     stop_index = 1

#     print("\n🚍 Passenger Counting System Started")
#     print("📍 Current Stop:", current_stop)
#     print("Press CTRL+C to stop\n")

#     try:
#         while True:
#             # -----------------------------
#             # READ FRAME
#             # -----------------------------
#             frame = video.read()
#             if frame is None:
#                 print("❌ Camera frame not received. Exiting.")
#                 break

#             # -----------------------------
#             # YOLO DETECTION
#             # -----------------------------
#             detections = yolo.detect(frame)

#             # -----------------------------
#             # DEEPSORT TRACKING
#             # -----------------------------
#             tracks = tracker.update(detections, frame)

#             # -----------------------------
#             # PROCESS TRACKS
#             # -----------------------------
#             for track in tracks:
#                 if not track.is_confirmed():
#                     continue

#                 track_id = track.track_id
#                 x1, y1, x2, y2 = map(int, track.to_ltrb())

#                 # Centroid Y
#                 centroid_y = (y1 + y2) // 2

#                 # Check line crossing
#                 direction = line.check_crossing(track_id, centroid_y)

#                 if direction:
#                     counter.update(
#                         track_id,
#                         direction,
#                         stop=current_stop,
#                         stop_index=stop_index
#                     )

#                     # Terminal log for each event
#                     print(
#                         f"[EVENT] Track ID {track_id} → {direction} | "
#                         f"Stop: {current_stop}"
#                     )

#             # -----------------------------
#             # TERMINAL OUTPUT (LIVE COUNTS)
#             # -----------------------------
#             entered, exited, current = counter.get_counts()

#             print(
#                 f"\rIN: {entered} | OUT: {exited} | "
#                 f"INSIDE: {current} | STOP: {current_stop}",
#                 end=""
#             )

#     except KeyboardInterrupt:
#         print("\n\n🛑 System stopped by user (CTRL+C)")

#         # Store last stop data before exit
#         counter.store_stop_data(current_stop, stop_index)
#         print(f"✅ Stop-wise data saved for: {current_stop}")

#     finally:
#         video.release()
#         print("📦 Resources released. Program ended.")


# if __name__ == "__main__":
#     main()
