import pyautogui

KEYS={
    'INCREMENT': "f",
    'DECREMENT': "v",
    "ADVANCE": "ctrl",
    "START": "="
}

def enter_code(code, keys):
    for char in code:
        if char in "0123456789":
            digit = int(char)
            if digit > 5:
                pyautogui.typewrite([keys["DECREMENT"]] * (10-digit), interval=0.1)
            else:
                pyautogui.typewrite([keys["INCREMENT"]] * digit, interval=0.1)
            pyautogui.typewrite([keys["ADVANCE"]], interval = 0.1)

def formatcode(code):
    tmp=''
    while(len(code)>3):
        tmp+=code[:4]+'-'
        code=code[4:]
    tmp+=code
    if tmp[-1]=='-':tmp=tmp[:-1]
    return tmp