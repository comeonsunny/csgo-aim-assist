import torch

model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

def detect_target(frame):
    results = model(frame)
    detections = results.xyxy[0].cpu().numpy()  # x1, y1, x2, y2, confidence, class
    target_class_id = 0  # Replace with the class ID of your target (e.g., person)
    target_detections = [det for det in detections if det[5] == target_class_id]

    if target_detections:
        target = max(target_detections, key=lambda x: x[4])  # Select the detection with the highest confidence
        target_x = (target[0] + target[2]) / 2
        target_y = (target[1] + target[3]) / 2
        return target_x, target_y
    return None, None
