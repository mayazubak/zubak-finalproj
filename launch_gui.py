import tkinter as tk
from src.gui_test import ExpGUI
from config.config import Config

def main():
    root = tk.Tk()
    root.title("Experiment")
    root.geometry(f"{Config.window_width}x{Config.window_height}")
    root.configure(bg=Config.instructions_bg_color)
    
    
    test = ExpGUI(root)
    test.start()
    root.mainloop()
    
if __name__ == "__main__":
    main()