import tkinter as tk 
import json, os

from general_lib import format_code

#View
class save_manager(object):
    def __init__(self, master=None, func_load=None):
        """ Constructor. Initializes parameters. master """
        self.frame = tk.Frame(master)
        self.frame.pack()
        self.master=master
        master.title("save manager")
        self.controller=save_manager_C(self)
        self.__create_widgets()
        if func_load: self.controller.register_load(func_load)
        self.master.protocol("WM_DELETE_WINDOW", self.hide)
        self.controller.on_refresh_click() #Refresh immediately after initialized.


    def __create_widgets(self):
        ## Create listbox.
        frame1=tk.Frame(self.frame)
        frame1.pack()
        bar_list=tk.Scrollbar(frame1)
        bar_list.pack(side=tk.RIGHT, fill=tk.Y)
        self.list_saves=tk.Listbox(frame1, width=55, yscrollcommand=bar_list.set, exportselection=False)
        self.list_saves.bind("<<ListboxSelect>>", self.controller.on_list_select)
        self.list_saves.pack()
        bar_list.config(command=self.list_saves.yview)

        ## Create note and code.
        frame2=tk.Frame(self.frame)
        frame2.pack()
        label_note=tk.Label(frame2, text="Note:")
        label_note.grid(row=0, column=0)
        self.sv_note=tk.StringVar()
        entry_note=tk.Entry(frame2, textvariable=self.sv_note, width=50)
        entry_note.grid(row=0, column=1)

        label_code=tk.Label(frame2, text="Code:")
        label_code.grid(row=1, column=0)
        self.sv_code=tk.StringVar()
        self.sv_code.trace_add('write', self.controller.on_code_change)
        self.entry_code=tk.Entry(frame2, textvariable=self.sv_code, width=50)
        self.entry_code.grid(row=1, column=1)

        ## Create buttons.
        frame3=tk.Frame(self.frame)
        frame3.pack()
        self.button_new=tk.Button(frame3, text="new", command=self.controller.on_new_click)
        self.button_change=tk.Button(frame3, text="change", command=self.controller.on_change_click)
        self.button_delete=tk.Button(frame3, text="delete", command=self.controller.on_delete_click)
        self.button_refresh=tk.Button(frame3, text="refresh", command=self.controller.on_refresh_click)
        self.button_select=tk.Button(frame3, text="select", command=self.controller.on_select_click)

        self.button_new.grid(row=0, column=0)
        self.button_change.grid(row=0, column=1)
        self.button_delete.grid(row=0, column=2)
        self.button_refresh.grid(row=0, column=3)
        self.button_select.grid(row=0, column=4)
        self.button_select['state']=tk.DISABLED

    def hide(self):
        self.master.withdraw()

    def show(self):
        self.master.update()
        self.master.deiconify()
#Model
class save_manager_M():
    def __init__(self):
        self.__saves=[]
        try:
            if os.path.exists('saves.json'):
                self.__read_local_save()
            self.__write_local_save()
        finally:
            pass

    def __read_local_save(self):
        with open('saves.json', 'r', encoding='utf8') as saves_json:
            self.__saves=json.loads(saves_json.read())
    
    def __write_local_save(self):
        with open('saves.json', 'w', encoding='utf8') as saves_json:
            saves_json.write(json.dumps(self.__saves))

    def add(self, code, note=None):
        self.__saves.append([note, code])
        self.__write_local_save()

    def delete(self, index):
        self.__saves.pop(index)
        self.__write_local_save()

    def change(self, index, code, note):
        self.__saves[index]=[note, code]
        self.__write_local_save()

    def roster(self):
        tmp=[]
        for item in self.__saves:
            tmp.append(item[0] if item[0] else item[1])
        return tmp
    
    def request(self, index):
        return self.__saves[index]

#Controller
class save_manager_C():
    def __init__(self, view):
        self.view=view
        self.model=save_manager_M()
        self.func_load=None

    def on_list_select(self, *args):
        # When an entry in the list is selected, update the GUI and show the note and code.
        index=self.view.list_saves.curselection()
        if index:
            item=self.model.request(index[0])
            self.view.sv_note.set(item[0])
            self.view.sv_code.set(item[1])

    def on_new_click(self):
        code = self.view.sv_code.get()
        note = self.view.sv_note.get()
        if code:
            self.model.add(code, note)
            self.view.list_saves.insert('end', note if note else code)
            self.view.list_saves.selection_clear(0, 'end')
            self.view.list_saves.selection_set('end')
            self.view.list_saves.activate('end')

    def on_change_click(self):
        index=self.view.list_saves.curselection()
        if index:
            index = index[0]
            code = self.view.sv_code.get()
            note = self.view.sv_note.get()
            if code:
                self.model.change(index, code, note)
                self.view.list_saves.delete(index)
                self.view.list_saves.insert(index, note if note else code)
                self.view.list_saves.selection_clear(0, 'end')
                self.view.list_saves.selection_set(index)
                self.view.list_saves.activate(index)
    
    def on_delete_click(self):
        index=self.view.list_saves.curselection()
        if index:
            index = index[0]
            self.model.delete(index)
            self.view.list_saves.delete(index)
            self.view.list_saves.selection_clear(0, 'end')
            self.view.sv_code.set("")
            self.view.sv_note.set("")
    
    def on_refresh_click(self):
        self.view.list_saves.delete(0, 'end')
        tmp=self.model.roster()
        for i in tmp:
            self.view.list_saves.insert('end', i)
        self.view.sv_code.set("")
        self.view.sv_note.set("")
    
    def on_select_click(self):
        self.func_load(self.view.sv_code.get())

    def on_code_change(self, *args):
        """Formatting the code to make it looks better."""
        tmp=self.view.sv_code.get()
        is_insert=self.view.entry_code.index('insert')==len(tmp)
        cursor_position=self.view.entry_code.index('insert')
        code=tmp.replace('-','')[:40]
        code=format_code(code)
        self.view.entry_code.delete(0, 'end')
        self.view.entry_code.insert(0, code)
        if(is_insert): 
            self.view.entry_code.icursor("end")
        else:
            self.view.entry_code.icursor(cursor_position)

    def register_load(self, func_load):
        if func_load:
            self.view.button_select['state']=tk.NORMAL
            self.func_load=func_load

if __name__ == "__main__":
    root=tk.Tk()
    app=save_manager(root)
    root.mainloop()