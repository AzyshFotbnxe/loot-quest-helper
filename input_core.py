import pyautogui
import keyboard


CODE = "1234-5678-9098-7654-3210-1234-5678-9098-7654-3210"
KEY_START = "="

class effector:
    def __init__(self):
        self.KEY_INCREMENT = "f"
        self.KEY_DECREMENT = "v"
        self.KEY_ADVANCE = "ctrl"
        self.KEY_START="="

    def enter_code(self, code):
        for char in code:
            if char in "0123456789":
                digit = int(char)
                if digit > 5:
                    pyautogui.typewrite([self.KEY_DECREMENT] * (10-digit), interval=0.1)
                else:
                    pyautogui.typewrite([self.KEY_INCREMENT] * digit, interval=0.1)
                pyautogui.typewrite([self.KEY_ADVANCE], interval = 0.1)


if __name__ == "__main__":
    effector=effector()
    keyboard.add_hotkey(KEY_START, effector.enter_code, args=(CODE, ))
    input("Press enter to quit.")