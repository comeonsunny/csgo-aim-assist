import pyautogui

def move_aim_to_target(target_x, target_y, frame):
    screen_width, screen_height = pyautogui.size()
    target_screen_x = int(target_x * screen_width / frame.shape[1])
    target_screen_y = int(target_y * screen_height / frame.shape[0])
    pyautogui.moveTo(target_screen_x, target_screen_y)
