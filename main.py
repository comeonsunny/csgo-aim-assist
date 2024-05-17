import cv2
from src.capture_screen import capture_screen
from src.detect_target import detect_target
from src.move_aim import move_aim_to_target

# Main loop
while True:
    frame = capture_screen()
    target_x, target_y = detect_target(frame)
    if target_x is not None and target_y is not None:
        move_aim_to_target(target_x, target_y, frame)
    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
