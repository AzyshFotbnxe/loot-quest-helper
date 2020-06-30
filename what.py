import PySimpleGui as sg
import pyautogui
import keyboard

# the save code, with or without dashes (non-digit characters are ignored)
CODE = sg.PopupGetText("Enter your code here:")

KEY_INCREMENT = "f" # key to increment the number, should be "interact"
KEY_ADVANCE = "ctrl" # key to advance to the next number
KEY_START = "=" # hotkey to trigger entering the code

def enter_code(code):
    for char in code:
        if char not in "0123456789":
            continue
        digit = int(char)
        pyautogui.typewrite([KEY_INCREMENT] * digit + [KEY_ADVANCE], interval=0.1)

keyboard.add_hotkey(KEY_START, enter_code, args=(CODE,))

input("Press enter to quit")