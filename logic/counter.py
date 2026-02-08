# class PassengerCounter:
#     def __init__(self):
#         self.entered = 0
#         self.exited = 0
#         self.current = 0

#         # 🔒 Track IDs already counted
#         self.counted_ids = set()

#     def update(self, track_id, direction):
#         # Each person counted only ONCE per journey
#         if track_id in self.counted_ids:
#             return

#         if direction == "IN":
#             self.entered += 1
#             self.current += 1
#             self.counted_ids.add(track_id)

#         elif direction == "OUT":
#             self.exited += 1
#             self.current = max(0, self.current - 1)
#             self.counted_ids.add(track_id)

#     def get_counts(self):
#         return self.entered, self.exited, self.current

# MONGODB CONNECTIOWITH COMMUNITY SERVER

# from datetime import datetime
# from pymongo import MongoClient
# from config.config import (
#     MONGO_URI, DB_NAME,
#     LIVE_COLLECTION, STOP_COLLECTION,
#     BUS_ID
# )

# # MongoDB connection
# client = MongoClient(MONGO_URI)
# db = client[DB_NAME]

# live_col = db[LIVE_COLLECTION]
# stop_col = db[STOP_COLLECTION]


# class PassengerCounter:
#     def __init__(self):
#         self.entered = 0
#         self.exited = 0
#         self.current = 0
#         self.crossed_ids = set()

#         # stop-wise counters
#         self.stop_entered = 0
#         self.stop_exited = 0

#     def update(self, track_id, direction, stop=None, stop_index=None):
#         key = (track_id, direction)

#         if key in self.crossed_ids:
#             return

#         if direction == "IN":
#             self.entered += 1
#             self.current += 1
#             self.stop_entered += 1

#             in_delta, out_delta = 1, 0

#         elif direction == "OUT":
#             self.exited += 1
#             self.current = max(0, self.current - 1)
#             self.stop_exited += 1

#             in_delta, out_delta = 0, 1

#         self.crossed_ids.add(key)

#         # 🔹 UPDATE LIVE DATA IN MONGODB
#         live_col.update_one(
#             {"bus_id": BUS_ID},
#             {
#                 "$inc": {
#                     "in_count": in_delta,
#                     "out_count": out_delta,
#                     "current_passengers": in_delta - out_delta
#                 },
#                 "$set": {
#                     "current_stop": stop,
#                     "stop_index": stop_index,
#                     "last_updated": datetime.now()
#                 }
#             },
#             upsert=True
#         )

#     def store_stop_data(self, stop, stop_index):
#         """
#         Call this ONLY when bus reaches a stop
#         """
#         stop_col.insert_one({
#             "bus_id": BUS_ID,
#             "stop_name": stop,
#             "stop_index": stop_index,
#             "in_count": self.stop_entered,
#             "out_count": self.stop_exited,
#             "timestamp": datetime.now()
#         })

#         # reset stop counters
#         self.stop_entered = 0
#         self.stop_exited = 0

#     def get_counts(self):
#         return self.entered, self.exited, self.current
from pymongo import MongoClient
from datetime import datetime
import certifi
from config.config import MONGO_URI

class PassengerCounter:
    def __init__(self):
        self.entered = 0
        self.exited = 0
        self.processed_ids = set()

         # -----------------------------
        # MongoDB Atlas connection
        # -----------------------------

        self.client = MongoClient(
            MONGO_URI,
            tls=True,
            tlsCAFile=certifi.where()
        )

        self.db = self.client["iRTMS"]
        self.events = self.db["passenger_events"]
        self.stops = self.db["stop_counts"]

        print("✅ MongoDB Atlas connected")

           # ---------------------------------
    # Update count when line crossed
    # ---------------------------------

    def update(self, track_id, direction, stop, stop_index):
        if track_id in self.processed_ids:
            return

        self.processed_ids.add(track_id)

        if direction == "IN":
            self.entered += 1
        else:
            self.exited += 1

        self.events.insert_one({
            "track_id": track_id,
            "direction": direction,
            "stop": stop,
            "stop_index": stop_index,
            "timestamp": datetime.utcnow()
        })

          # ---------------------------------
    # Store stop-wise summary
    # ---------------------------------

    def store_stop_data(self, stop, stop_index):
        self.stops.insert_one({
            "stop": stop,
            "stop_index": stop_index,
            "entered": self.entered,
            "exited": self.exited,
            "inside": self.entered - self.exited,
            "timestamp": datetime.utcnow()
        })

    def get_counts(self):
        return self.entered, self.exited, self.entered - self.exited
