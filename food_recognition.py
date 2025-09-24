from PIL import Image
from ultralytics import YOLO

model = YOLO("yolov8n.pt")

FOOD_MAP = {0: "pizza", 1: "burger", 2: "salad", 3: "rice", 4: "chicken"}
NUTRITION_DATA = {
    "pizza": {"calories": 320, "protein": 12, "carbs": 40, "fat": 15},
    "burger": {"calories": 450, "protein": 25, "carbs": 35, "fat": 20},
    "salad": {"calories": 150, "protein": 5, "carbs": 10, "fat": 7},
    "rice": {"calories": 200, "protein": 4, "carbs": 44, "fat": 2},
    "chicken": {"calories": 250, "protein": 27, "carbs": 0, "fat": 10},
}

def analyze_meal(file):
    img = Image.open(file)
    results = model.predict(img)
    detections = []
    for r in results:
        for c in r.boxes.cls:
            label = FOOD_MAP.get(int(c), "unknown")
            nutri = NUTRITION_DATA.get(label, {})
            detections.append({"item": label, "nutrition": nutri})
    return detections