import pyautogui
distance = 0
pyautogui.moveTo(900, 200)
while distance <= 10:
    pyautogui.drag(distance, 0, duration=0.5)   # move right
    distance -= 5
    pyautogui.drag(0, distance, duration=0.5)   # move down
    pyautogui.drag(-distance, 0, duration=0.5)  # move left
    distance = 5
    pyautogui.drag(0, -distance, duration=0.5)  # move upimport pyautogui
    pyautogui.drag(distance, 0, duration=0.5)   # move right
    distance = 10
    pyautogui.drag(0, distance, duration=0.5)   # move down
    pyautogui.drag(-distance, 0, duration=0.5)  # move left
    distance -= 10
    pyautogui.drag(0, -distance, duration=0.5)  # move upimport pyautogui
