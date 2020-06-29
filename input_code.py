import pyautogui
import keyboard

CODE = "4936-3163-9230-3565-2194-4833-0679-5215-2447-0984"

KEY_INCREMENT = "f"
KEY_DECREMENT = "v"
KEY_ADVANCE = "ctrl"
KEY_START = "="

def enter_code(code):
    for char in code:
        if char in "0123456789":
            digit = int(char)
            if digit > 5:
                pyautogui.typewrite([KEY_DECREMENT] * (10-digit), interval=0.1)
            else:
                pyautogui.typewrite([KEY_INCREMENT] * digit, interval=0.1)
            pyautogui.typewrite([KEY_ADVANCE], interval = 0.1)


if __name__ == "__main__":
    keyboard.add_hotkey(KEY_START, enter_code, args=(CODE, ))
    input("Press enter to quit.")