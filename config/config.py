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
# CONFIDENCE_THRESHOLD = 0.5
# PERSON_CLASS_ID = 0


# =========================
# MongoDB Atlas Configuration
# =========================
MONGO_URI = (
    "mongodb+srv://shin104051_db_user:uaIrqrgzc061Jc5v@cluster1.cawpy2t.mongodb.net/?appName=Cluster1"
)

DB_NAME = "iRTMS"





# ==============================
# ROI CONFIGURATION
# ==============================

USE_ROI = True   # Turn ROI ON/OFF easily

# ROI coordinates (x1, y1, x2, y2)
ROI_X1 = 500
ROI_Y1 = 100
ROI_X2 = 1420
ROI_Y2 = 1000


# RYZEN 5 OR I5
# MAX_AGE = 20
# MIN_HITS = 3
# IOU_THRESHOLD = 0.3
# MAX_COSINE_DISTANCE = 0.4
# NN_BUDGET = 50
# CONFIDENCE_THRESHOLD = 0.5
# frame_skip = 3
# input_resolution = 640*360


# RYZEN 7
# MAX_AGE = 40
# MIN_HITS = 5
# MAX_COSINE_DISTANCE = 0.3
# NN_BUDGET = 100
# FRAME_SKIP = 1

#Parvathi & Aarthi
# model = yolov8s.pt
# imgsz = 640
# conf = 0.35
# iou = 0.5
# max_det = 50
# device = "cpu"
# max_age = 20
# n_init = 3
# max_iou_distance = 0.7
# max_cosine_distance = 0.2
# nn_budget = 100

#kaviya v8s
# model = yolov8s.pt
# imgsz = 640
# conf = 0.35
# iou = 0.5
# max_det = 40
# device = "cpu"
# max_age = 15
# n_init = 3
# max_iou_distance = 0.7
# max_cosine_distance = 0.2
# nn_budget = 50


#Ponce v8s
# model = yolov8s.pt
# imgsz = 768        # You can safely use 768
# conf = 0.35
# iou = 0.5
# max_det = 60
# device = 0         # GPU
# half = True        # Enable FP16 (important for 4GB VRAM)
# max_age = 25
# n_init = 3
# max_iou_distance = 0.7
# max_cosine_distance = 0.2
# nn_budget = 100

#ponce v8m
# model = yolov8m.pt
# imgsz = 640        # Do NOT go above 640
# conf = 0.35
# iou = 0.5
# max_det = 50
# device = 0
# half = True
# max_age = 20
# n_init = 3
# max_iou_distance = 0.7
# max_cosine_distance = 0.2
# nn_budget = 100


#MADDY
# ==============================
# YOLO SETTINGS
# ==============================

MODEL_PATH = "yolov8m.pt"
IMAGE_SIZE = 640              # 640 is optimal for RTX 2050 4GB
CONFIDENCE_THRESHOLD = 0.35
IOU_THRESHOLD = 0.5
MAX_DETECTIONS = 60
DEVICE = 0                    # 0 = GPU
HALF_PRECISION = True         # Use FP16

# ==============================
# DEEPSORT SETTINGS
# ==============================

MAX_AGE = 30                  # Frames to keep lost track
MIN_HITS = 3                  # Confirm track after 3 detections
IOU_THRESHOLD_TRACK = 0.7     # Matching threshold
MAX_COSINE_DISTANCE = 0.2
NN_BUDGET = 100

# ==============================
# SYSTEM SETTINGS
# ==============================

FRAME_SKIP = 1                # 1 = process every frame
INPUT_RESOLUTION = (640, 480) # Recommended