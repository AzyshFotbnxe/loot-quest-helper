import tkinter as tk 
from general_lib import format_code
import json

class save_manager(tk.Frame):
    def __init__(self, master=None, func_load=None):
        super().__init__(master=master)
        master.title("save manager")
        self.__load_callback = func_load
        self.__create_widgets()
        self.__read_local_save()
        self.pack()

    def __create_widgets(self):
        self.list_saves=tk.Listbox(self)
        self.list_saves.pack()

        frame1=tk.Frame(self)
        frame1.pack()
        label_note=tk.Label(frame1, text="Note:")
        label_note.grid(row=0, column=0)
        self.sv_note=tk.StringVar()
        entry_note=tk.Entry(frame1, textvariable=self.sv_note)
        entry_note.grid(row=0, column=1)

        label_code=tk.Label(frame1, text="Code:")
        label_code.grid(row=1, column=0)
        self.sv_code=tk.StringVar()
        self.entry_code=tk.Entry(frame1, textvariable=self.sv_code)
        self.entry_code.grid(row=1, column=1)


    def __read_local_save(self):
        pass

    def __on_load_click(self):
        pass


if __name__ == "__main__":
    app=save_manager(tk.Tk())
    app.mainloop()