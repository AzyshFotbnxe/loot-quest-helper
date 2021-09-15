import pyautogui
import keyboard

"""Modified from the script created by Ciege#8558 on discord"""

CODE = "1234-5678-9098-7654-3210-1234-5678-9098-7654-3210"

KEYS={
    'INCREMENT': "f",
    'DECREMENT': "v",
    "ADVANCE": "ctrl",
    "START": "=",
    "ITEMONLY": "r"
}

def enter_code(code, keys):
    for char in code:
        if char in "0123456789":
            digit = int(char)
            if digit > 5:
                pyautogui.typewrite([keys["DECREMENT"]] * (10-digit), interval=0.1)
            else:
                pyautogui.typewrite([keys["INCREMENT"]] * digit, interval=0.1)
            pyautogui.press(keys["ADVANCE"], interval = 0.1)

# class effector:
#     def __init__(self):
#         self.KEY_INCREMENT = "f"
#         self.KEY_DECREMENT = "v"
#         self.KEY_ADVANCE = "ctrl"
#         self.KEY_START="="

#     def enter_code(self, code):
#         for char in code:
#             if char in "0123456789":
#                 digit = int(char)
#                 if digit > 5:
#                     pyautogui.typewrite([self.KEY_DECREMENT] * (10-digit), interval=0.1)
#                 else:
#                     pyautogui.typewrite([self.KEY_INCREMENT] * digit, interval=0.1)
#                 pyautogui.typewrite([self.KEY_ADVANCE], interval = 0.1)


if __name__ == "__main__":
    # effector=effector()
    keyboard.add_hotkey(KEYS["START"], enter_code, args=(CODE, KEYS, ))
    input("Press enter to quit.")
