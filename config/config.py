# # Camera
# CAMERA_INDEX = 0

# # Virtual line (horizontal door line)
# LINE_Y = 300   # y-coordinate of door line

#  # Frame resize (optional, improves speed)
# FRAME_WIDTH = 640
# FRAME_HEIGHT = 480

# # # YOLO
# # YOLO_CONFIDENCE = 0.5
# # YOLO_PERSON_CLASS_ID = 0

# # BUS_ID = "BUS_001"



# # MONGO_URI = "mongodb://localhost:27017/"
# # DB_NAME = "bus_management"
# # LIVE_COLLECTION = "live_bus_status"
# # STOP_COLLECTION = "stop_wise_counts"



# # =========================
# # MongoDB Atlas Config
# # =========================

# MONGO_URI = (
#    "mongodb+srv://shin104051_db_user:uaIrqrgzc061Jc5v@cluster1.cawpy2t.mongodb.net/?appName=Cluster1"
# )

# DB_NAME = "iRTMS"
# # PASSENGER_COLLECTION = "passenger_events"
# # STOP_COLLECTION = "stop_summary"


# #RYZEN 5 OR I5
# MAX_AGE = 20
# MIN_HITS = 3
# IOU_THRESHOLD = 0.3
# MAX_COSINE_DISTANCE = 0.4
# NN_BUDGET = 50
# CONFIDENCE_THRESHOLD = 0.5
# frame_skip = 1
# input_resolution = 640*360 or 640*480


# # RYZEN 7
# # MAX_AGE = 40
# # MIN_HITS = 5
# # MAX_COSINE_DISTANCE = 0.3
# # NN_BUDGET = 100
# # FRAME_SKIP = 1

#AUTO STARTUP

# =========================
# Camera Configuration
# =========================
CAMERA_INDEX = 0

FRAME_WIDTH = 640
FRAME_HEIGHT = 480


# =========================
# Virtual Line Configuration
# =========================
LINE_Y = 300   # Door line (calibrated based on camera position)


# =========================
# YOLO Configuration
# =========================
CONFIDENCE_THRESHOLD = 0.5
PERSON_CLASS_ID = 0


# =========================
# MongoDB Atlas Configuration
# =========================
MONGO_URI = (
    "mongodb+srv://shin104051_db_user:uaIrqrgzc061Jc5v@cluster1.cawpy2t.mongodb.net/?appName=Cluster1"
)

DB_NAME = "iRTMS"


# =========================
# Hardware Profile Selection
# =========================
# Choose ONE profile only:
# "LOW_END"  → i5 / Ryzen 5 / Integrated GPU
# "HIGH_END" → i7 / Ryzen 7 / Dedicated GPU

HARDWARE_PROFILE = "LOW_END"


# =========================
# DeepSORT Tuning Profiles
# =========================

if HARDWARE_PROFILE == "LOW_END":
    # i5 / Ryzen 5 (Integrated graphics)
    MAX_AGE = 20
    MIN_HITS = 3
    IOU_THRESHOLD = 0.3
    MAX_COSINE_DISTANCE = 0.4
    NN_BUDGET = 50
    FRAME_SKIP = 1

elif HARDWARE_PROFILE == "HIGH_END":
    # i7 / Ryzen 7 (Better CPU / GPU)
    MAX_AGE = 40
    MIN_HITS = 5
    IOU_THRESHOLD = 0.4
    MAX_COSINE_DISTANCE = 0.3
    NN_BUDGET = 100
    FRAME_SKIP = 1

else:
    raise ValueError("❌ Invalid HARDWARE_PROFILE selected")
