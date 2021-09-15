import tkinter as tk
import keyboard
from save_manager import save_manager as mgr
from general_lib import KEYS, stop_thread, format_code, t_enter_code

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master=master)
        self.master=master
        master.title("input save helper")
        self.__create_widgets()
        self.__last_register=None
        self.__thread=None
        self.manager=mgr(tk.Toplevel(), self.__callback_manager)
        self.manager.hide()
        self.master.protocol("WM_DELETE_WINDOW", self.__on_closing)
        self.pack()

    def __create_widgets(self):
        self.sv_code=tk.StringVar()
        self.sv_code.trace_add('write', self.__on_code_change)
        self.entry_code=tk.Entry(self, width=50, textvariable=self.sv_code)
        self.entry_code.pack()

        frame1=tk.Frame(self)
        frame1.pack()
        label_notice=tk.Label(frame1, 
        text=f'''Please set these in overwatch:
        {KEYS["INCREMENT"]} as increment the number (interact)
        {KEYS["DECREMENT"]} as decrement the number (melee)
        {KEYS["ADVANCE"]} as advance (crouch)
        {KEYS["ITEMONLY"]} as item only (reload)
        after register,
        press {KEYS["START"]} to start, {KEYS["STOP"]} to stop.'''
        )
        label_notice.grid(row=0, column=0)

        frame1_1=tk.Frame(frame1)
        frame1_1.grid(row=0, column=1)
        button_register=tk.Button(frame1_1, text='register', command=self.__on_register)
        button_register.grid(row=0, column=0)

        button_deregister=tk.Button(frame1_1, text='deregister', command=self.__on_deregister)
        button_deregister.grid(row=0, column=1)

        # self.iv_item=tk.IntVar()
        # self.checkbox_item=tk.Checkbutton(frame1_1, text='item only', variable=self.iv_item)
        # self.checkbox_item.grid(row=1, column=0)

        self.iv_only_adv=tk.IntVar()
        self.checkbox_adv=tk.Checkbutton(frame1_1, text='advance only', variable=self.iv_only_adv)
        self.checkbox_adv.grid(row=1, column=1)

        button_manager=tk.Button(frame1_1, text="save manager", command=self.__on_manager)
        button_manager.grid(row=3)
        
        self.sv_status=tk.StringVar()
        self.sv_status.set("Not registered")
        label_status=tk.Label(self, textvariable=self.sv_status)
        label_status.pack()

    def __on_code_change(self, *args):
        """Formatting the code to make it looks better."""
        tmp=self.sv_code.get()
        is_insert=self.entry_code.index('insert')==len(tmp)
        cursor_position=self.entry_code.index('insert')
        code=tmp.replace('-','')[:40]
        code=format_code(code)
        self.entry_code.delete(0, 'end')
        self.entry_code.insert(0, code)
        if(is_insert): 
            self.entry_code.icursor("end")
        else:
            self.entry_code.icursor(cursor_position)

    def __on_register(self):
        try:
            self.__on_deregister()
            self.__last_register = [keyboard.add_hotkey(KEYS["START"], self.__enter_code_helper, args=()), keyboard.add_hotkey(KEYS["STOP"], self.__on_deregister, args=())]
            self.sv_status.set("Registered")
            self.entry_code['state']=tk.DISABLED
            # self.checkbox_item['state']=tk.DISABLED
            self.checkbox_adv['state']=tk.DISABLED
        finally:
            pass

    def __enter_code_helper(self):
        self.__thread = t_enter_code(self.sv_code.get(), KEYS, False, self.iv_only_adv.get())
        self.__thread.start()

    def __on_deregister(self):
        try:
            if self.__last_register: 
                for i in self.__last_register:
                    keyboard.remove_hotkey(i)
            if self.__thread: stop_thread(self.__thread)
        finally:
            self.__last_register = None
            self.__thread=None
            self.sv_status.set("Not registered")
            self.entry_code['state']=tk.NORMAL
            # self.checkbox_item['state']=tk.NORMAL
            self.checkbox_adv['state']=tk.NORMAL
    
    def __on_manager(self):
        self.manager.show()

    def __callback_manager(self, code):
        self.sv_code.set(code)

    def __on_closing(self):
        self.manager.master.destroy()
        self.master.destroy()

if __name__ == "__main__":
    app=Application(tk.Tk())
    app.mainloop()