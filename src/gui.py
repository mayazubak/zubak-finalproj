import tkinter as tk
import subprocess
import os
from config.config import Config


class GUI:
    
    def __init__(self):
        self.root = None
        self.launch_button = None
        self.create_windown()
        self.create_button()
        
    
    def create_window(self):
        self.root = tk.Tk()  # create the tk window object and save it in self.root
        self.root.geometry("{}x{}".format(Config.window_width, Config.window_height))  # set the window size
        self.root.title("Experiment")  # set the window title
        self.root.configure(bg="white")  # set the window background color
        self.root.resizable(False, False)  # set the window so that it is not resizable
        
        
    def create_button(self):
        self.launch_button = tk.Button(self.root, text="Launch Experiment", command=self.launch_experiment)
        self.launch_button.pack(expand=True)
        
    def run(self):
        self.root.mainloop()
        
        
if __name__ == "__main__":
    gui = GUI()
    gui.run()