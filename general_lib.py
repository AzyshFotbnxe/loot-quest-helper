import threading
import time
import inspect
import ctypes
import pyautogui

KEYS={
    'INCREMENT': "f",
    'DECREMENT': "v",
    "ADVANCE": "ctrl",
    "START": "="
}
class t_enter_code(threading.Thread):
    def __init__(self, code, keys):
        threading.Thread.__init__(self)
        self.code=code
        self.keys=keys

    def run(self):
        enter_code(self.code, self.keys)

## Copy and pasted from internet to stop a thread. 
## https://stackoverflow.com/questions/323972/is-there-any-way-to-kill-a-thread
def stop_thread(thread):
    _async_raise(thread.ident, SystemExit)

def _async_raise(tid, exctype):
    """raises the exception, performs cleanup if needed"""
    tid = ctypes.c_long(tid)
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        # """if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")

def enter_code(code, keys):
    for char in code:
        if char in "0123456789":
            digit = int(char)
            if digit > 5:
                pyautogui.typewrite([keys["DECREMENT"]] * (10-digit), interval=0.1)
            else:
                pyautogui.typewrite([keys["INCREMENT"]] * digit, interval=0.1)
            pyautogui.typewrite([keys["ADVANCE"]], interval = 0.1)

def filter_code(code):
    tmp=filter(lambda ch: ch in '0123456789-', code)
    tmp="".join(list(tmp))
    return tmp

def format_code(code):
    tmp=''
    code = filter_code(code) #always filter. Totally optional.
    if code:
        while(len(code)>3):
            tmp+=code[:4]+'-'
            code=code[4:]
        tmp+=code
        if tmp[-1]=='-':tmp=tmp[:-1]
    return tmp

