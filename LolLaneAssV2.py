import tkinter as tk
from tkinter import ttk  
from tkinter import *
import time

class load_Screen(tk.Frame):
    def __init__(self, master, *arg, **kwargs):
        tk.Frame.__init__(self, master, *arg, **kwargs)
        self.pack()  

        self.start_button = tk.Button(self, text="Start", command=self.start)
        self.start_button.pack(pady = 20)

        self.progress = ttk.Progressbar(self, orient="horizontal", length=300, mode="determinate")
        self.progress.pack(pady = 20)

    def start(self):
        self.progress['value'] = 0  
        self.progress['maximum'] = 50
        self.update_progress()

    def update_progress(self):
        for i in range(101):
            time.sleep(0.01)
            self.progress['value'] = i
            self.update_idletasks()
        self.show_new_frame()
        
    def show_new_frame(self):
        for widget in self.winfo_children():
            widget.destroy()
        new_Frame = champ_Select(self)
        new_Frame.pack(expand = True, fill = 'both')
        
            
class champ_Select(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.config(bg = "#091428")

        self.champions_canvas = tk.Canvas(self, bg='#061F36', width=800, height=800, highlightthickness = 7, highlightbackground="#C8AA6E")
        self.champions_canvas.pack(side= tk.BOTTOM, fill=tk.BOTH, expand=True)

        
        self.search = tk.Entry(self, width = 20, highlightthickness = 2, highlightbackground = '#C8AA6E')
        self.search.place(x = 30, y = 30)
        self.search.insert(0, "Find Champion...")

        self.supp_icon = tk.PhotoImage(file=r'Resources/Images/Lane_icons/support.png')
        self.support = tk.Button(self, image=self.supp_icon, background = '#091428', borderwidth = 4, command=lambda: self.select_champion('Support'))
        self.support.image = self.supp_icon
        self.support.place(x = 590, y = 30)

        adc_icon = tk.PhotoImage(file=r'Resources/Images/Lane_icons/adc.png')
        adc = tk.Button(self, image=adc_icon, background = '#091428', borderwidth = 4, command=lambda: self.select_champion('ADC'))
        adc.image = adc_icon
        adc.place(x = 630, y = 30)

        mid_icon = tk.PhotoImage(file=r'Resources/Images/Lane_icons/mid.png')
        mid = tk.Button(self, image=mid_icon, background = '#091428', borderwidth = 4, command=lambda: self.select_champion('Mid'))
        mid.image = mid_icon
        mid.place(x = 670, y = 30)

        jungle_icon = tk.PhotoImage(file=r'Resources/Images/Lane_icons/jungle.png')
        jungle = tk.Button(self, image=jungle_icon, background = '#091428', borderwidth = 4, command=lambda: self.select_champion('Jungle'))
        jungle.image = jungle_icon
        jungle.place(x = 710, y = 30)

        top_icon = tk.PhotoImage(file=r'Resources/Images/Lane_icons/top.png')
        top = tk.Button(self, image=top_icon, background = '#091428', borderwidth = 4, command=lambda: self.select_champion('Top'))
        top.image = top_icon
        top.place(x = 750, y = 30)

 
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Main Menu")
    root.geometry("1280x720") 
    app = load_Screen(root)
    root.mainloop()