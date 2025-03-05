import tkinter as tk
from tkinter import ttk  
from tkinter import *
import time
import pyodbc
import os
import pygame
from PIL import Image, ImageTk

class load_Screen(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.pack()
        pygame.mixer.init()  
        self.start_button = tk.Button(self, text="Start", command=lambda: [self.fx('load_press'), self.start()])
        self.start_button.pack(pady=20)
        self.progress = ttk.Progressbar(self, orient="horizontal", length=300, mode="determinate")
        self.progress.pack(pady=20)

    def fx(self, sound_type):
        sound_files = {
            "button": "Resources/SoundFX/UI/button.mp3",
            "load_press": ["Resources/SoundFX/UI/matchFound.mp3", "Resources/SoundFX/UI/button.mp3"]
        }
        try:
            if sound_type in sound_files:
                sounds = sound_files[sound_type] if isinstance(sound_files[sound_type], list) else [sound_files[sound_type]]
                for sound_path in sounds:
                    if os.path.exists(sound_path):
                        sound = pygame.mixer.Sound(sound_path)
                        sound.play()
                    else:
                        print(f"Sound file not found: {sound_path}")
            else:
                print(f"Sound type '{sound_type}' not found in sound_files dictionary.")
        except pygame.error as e:
            print(f"Error playing sound '{sound_type}': {e}")

    def start(self):
        self.progress['value'] = 0  
        self.progress['maximum'] = 100
        self.update_progress()

    def update_progress(self):
        for i in range(101):
            time.sleep(0.03)
            self.progress['value'] = i
            self.update_idletasks()
        self.show_new_frame()
        
    def show_new_frame(self):
        for widget in self.winfo_children():
            widget.destroy()
        new_frame = champ_Select(self)
        new_frame.pack(expand=True, fill='both')

class champ_Select(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.conn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=MARCO;'
            'DATABASE=lolchamps;'
            'Trusted_Connection=yes;')
        self.cursor = self.conn.cursor()

        self.top_frame = tk.Frame(self, bg="#091428", height=70)
        self.top_frame.pack(side=tk.TOP, fill=tk.X)

        self.canvas_frame = tk.Frame(self, bg="#091428")
        self.canvas_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.champions_canvas = tk.Canvas(self.canvas_frame, bg='#061F36', width=800, height=730)
        self.champions_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar = ttk.Scrollbar(self.canvas_frame, orient="vertical")
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        style = ttk.Style()
        style.theme_use('default')
        style.configure("Custom.Vertical.TScrollbar", 
                        background="#C8AA6E", 
                        troughcolor="#091428", 
                        bordercolor="#C8AA6E", 
                        arrowcolor="#FFFFFF", 
                        gripcount=0, 
                        relief="flat")
        style.map("Custom.Vertical.TScrollbar", 
                  background=[('active', '#D4B975'), ('!active', '#C8AA6E')])
        self.scrollbar.configure(style="Custom.Vertical.TScrollbar")
        self.scrollbar.configure(command=self.champions_canvas.yview)

        self.champions_canvas.configure(yscrollcommand=self.scrollbar.set)

        self.champions_canvas.bind("<MouseWheel>", self._on_mousewheel)
        self.champions_canvas.bind("<Button-4>", self._on_mousewheel_up)
        self.champions_canvas.bind("<Button-5>", self._on_mousewheel_down)

        self.search = tk.Entry(self.top_frame, width=20, highlightthickness=2, highlightbackground='#C8AA6E')
        self.search.place(x=30, y=20)
        self.search.insert(0, "Find Champion...")
        self.search.bind('<FocusIn>', self.clear_placeholder)
        self.search.bind('<FocusOut>', self.restore_placeholder)
        self.search.bind('<KeyRelease>', self.search_champions)
        
        self.all_icon = tk.PhotoImage(file=r'Resources/Images/Lane_icons/all.png')
        self.all = tk.Button(self.top_frame, image=self.all_icon, background='#091428', borderwidth=4, 
                            command=lambda: self.select_champion('All'))
        self.all.image = self.all_icon
        self.all.place(x=550, y=15)

        self.supp_icon = tk.PhotoImage(file=r'Resources/Images/Lane_icons/support.png')
        self.support = tk.Button(self.top_frame, image=self.supp_icon, background='#091428', 
                                borderwidth=4, command=lambda: self.select_champion('Support'))
        self.support.image = self.supp_icon
        self.support.place(x=590, y=15)

        adc_icon = tk.PhotoImage(file=r'Resources/Images/Lane_icons/adc.png')
        adc = tk.Button(self.top_frame, image=adc_icon, background='#091428', borderwidth=4, 
                       command=lambda: self.select_champion('Bot'))
        adc.image = adc_icon
        adc.place(x=630, y=15)

        mid_icon = tk.PhotoImage(file=r'Resources/Images/Lane_icons/mid.png')
        mid = tk.Button(self.top_frame, image=mid_icon, background='#091428', borderwidth=4, 
                       command=lambda: self.select_champion('Mid'))
        mid.image = mid_icon
        mid.place(x=670, y=15)

        jungle_icon = tk.PhotoImage(file=r'Resources/Images/Lane_icons/jungle.png')
        jungle = tk.Button(self.top_frame, image=jungle_icon, background='#091428', borderwidth=4, 
                          command=lambda: self.select_champion('Jungle'))
        jungle.image = jungle_icon
        jungle.place(x=710, y=15)

        top_icon = tk.PhotoImage(file=r'Resources/Images/Lane_icons/top.png')
        top = tk.Button(self.top_frame, image=top_icon, background='#091428', borderwidth=4, 
                       command=lambda: self.select_champion('Top'))
        top.image = top_icon
        top.place(x=750, y=15)

        self.champion_images = {}
        self.display_all_champions()

    def _on_mousewheel(self, event):
        self.champions_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def _on_mousewheel_up(self, event):
        self.champions_canvas.yview_scroll(-1, "units")

    def _on_mousewheel_down(self, event):
        self.champions_canvas.yview_scroll(1, "units")

    def clear_placeholder(self, event):
        if self.search.get() == "Find Champion...":
            self.search.delete(0, tk.END)

    def restore_placeholder(self, event):
        if not self.search.get():
            self.search.insert(0, 'Find Champion...')

    def search_champions(self, event):
        search_term = self.search.get().strip().lower()
        if search_term == 'find champion...':
            search_term = ''
        self.champions_canvas.delete("all")
        for widget in self.champions_canvas.winfo_children():
            widget.destroy()
        query = """
        SELECT ChampionName, ImageFile
        FROM Champions
        WHERE ChampionName LIKE ?
        """
        self.cursor.execute(query, (f"%{search_term}%",))
        champs = self.cursor.fetchall()
        self.display_champions(champs)
    
    def select_champion(self, lane):
        self.champions_canvas.delete("all")
        for widget in self.champions_canvas.winfo_children():
            widget.destroy()
        if lane == 'All':
            query = "SELECT ChampionName, ImageFile FROM Champions"
            self.cursor.execute(query)
        else:
            query = """
            SELECT c.ChampionName, c.ImageFile
            FROM Champions c
            JOIN ChampionLanes cl ON c.ChampionID = cl.ChampionID
            JOIN Lanes l ON cl.LaneID = l.LaneID
            WHERE l.LaneName = ?
            """
            self.cursor.execute(query, (lane,))
        champs = self.cursor.fetchall()
        self.display_champions(champs)

    def display_all_champions(self):
        query = 'SELECT ChampionName, ImageFile FROM Champions'
        self.cursor.execute(query)
        champs = self.cursor.fetchall()
        self.display_champions(champs)

    def display_champions(self, champs):
        y_offset = 10
        x_offset = 5
        base_path = r'Resources/Images/Champ_icons/'
        cols = 10
        rows = (len(champs) + cols - 1) // cols
        total_height = rows * 70 + y_offset
        for i, champ in enumerate(champs):
            champ_name = champ[0]
            image_file = champ[1]
            x = (i % cols) * 80 + x_offset
            y = (i // cols) * 70 + y_offset
            small_canvas = tk.Canvas(self.champions_canvas, width=70, height=70, 
                                   bg='#061F36', highlightthickness=2, 
                                   highlightbackground='#C8AA6E')
            try:
                full_path = os.path.join(base_path, image_file)
                if os.path.exists(full_path):
                    img = Image.open(full_path).resize((50, 50), Image.Resampling.LANCZOS)
                    champ_image = ImageTk.PhotoImage(img)
                    self.champion_images[champ_name] = champ_image
                    small_canvas.create_image(35, 25, image=champ_image)
                else:
                    raise FileNotFoundError(f"Image not found: {full_path}")
            except Exception as e:
                print(f"Error loading image for {champ_name}: {e}")
            small_canvas.create_text(35, 60, text=champ_name, fill='white', font=('Arial', 8))
            self.champions_canvas.create_window(x + 35, y + 35, window=small_canvas)
        self.champions_canvas.config(scrollregion=(0, 0, 800, total_height))

    def __del__(self):
        self.cursor.close()
        self.conn.close()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Main Menu")
    root.geometry("1280x720")
    root.config(bg="#061F36") 
    app = load_Screen(root)
    root.mainloop()