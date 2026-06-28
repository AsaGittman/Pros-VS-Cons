"""
    Main startup file for Pros VS Cons.

    Author: Asa
    Version: 0.01
"""

from tkinter import *
from tkinter import ttk

# App Setup
def main():
 root = Tk()
 root.title("Pros VS Cons")
 root.attributes("-fullscreen", True)

 def toggle_fullscreen(event=None):
     current_state = root.attributes("-fullscreen")
     root.attributes("-fullscreen", not current_state)
     return "break"
 
 root.bind_all("<KeyPress-Escape>", toggle_fullscreen)

 frm = ttk.Frame(root, padding=100)
 frm.grid()
 root.mainloop()


if __name__ == "__main__":
    main()