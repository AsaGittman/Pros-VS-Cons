"""
    Main startup file for Pros VS Cons.

    Author: Asa
    Version: 0.01
"""

from tkinter import *
from tkinter import ttk
from queue import PriorityQueue
import node

# App Setup
def main():
 pros = PriorityQueue()
 cons = PriorityQueue()
 # Root window setup
 root = Tk()
 root.title("Pros VS Cons")
 root.geometry("800x600")

 # Menubar setup
 menubar = Menu(root)

 filemenu = Menu(menubar, tearoff=0)
 filemenu.add_command(label="Open")
 filemenu.add_command(label="Save")
 filemenu.add_command(label="Exit", command=root.quit)

 viewmenu = Menu(menubar, tearoff=0)
 viewmenu.add_command(label="Fullscreen (Esc)", command=lambda: root.attributes("-fullscreen", not root.attributes("-fullscreen")))

 menubar.add_cascade(label="File", menu=filemenu)
 menubar.add_cascade(label="View", menu=viewmenu)
 root.config(menu=menubar)

 # Pros and Cons Lists
 pros_frame = Frame(root)
 pros_label = Label(pros_frame, text="Pros", font=("Helvetica", 16))
 pros_label.pack(pady=10)

 pros_listbox = Listbox(pros_frame, width=40, height=20)
 pros_listbox.pack(padx=10)
 pros_frame.pack(side=LEFT, padx=10)

 cons_frame = Frame(root)
 cons_label = Label(cons_frame, text="Cons", font=("Helvetica", 16))
 cons_label.pack(pady=10)

 cons_listbox = Listbox(cons_frame, width=40, height=20)
 cons_listbox.pack(padx=10)
 cons_frame.pack(side=RIGHT, padx=10)

 # Keybinds
 root.bind_all("<KeyPress-Escape>", lambda event: toggle_fullscreen(root, event))

 canvas = Canvas(root, width=800, height=600, bg="white")
 canvas.pack()

 # Node Creation
 create_button = Button(root, text="+", command=lambda: add_node_window(pros, cons, pros_listbox, cons_listbox), width=5, height=1)
 create_button.place(x=10, y=10)
 deploy_button = Button(root, text="Deploy", command=lambda: draw_nodes(canvas, pros, cons), width=5, height=1)
 deploy_button.place(x=10, y=50)


 root.mainloop()

# Create a node
def create_node(type, name, weight, pros, cons):
    new_node = node.Node(name, weight)
    if type == "Pro":
        pros.put((weight, new_node))
    else:
        cons.put((weight, new_node))

# Keybind Setup functions
def toggle_fullscreen(root, event=None):
     current_state = root.attributes("-fullscreen")
     root.attributes("-fullscreen", not current_state)
     return "break"
# For later use, if we want to close the window with a keybind
def close_window(root, event=None):
    root.destroy()
    return "break"

# Helper Functions
def add_node_window(pros, cons, pros_listbox, cons_listbox):
    window = Toplevel()
    window.title("Create Pro or Con")
    window.geometry("300x300")
    window.resizable(False, False)

    label1 = Label(window, text="Select Type")
    label1.pack(pady=10)
    options = ["Pro", "Con"]
    cb = ttk.Combobox(window, values=options)
    cb.pack(pady=10)

    label2 = Label(window, text="Enter Name")
    label2.pack(pady=10)
    text = Text(window, height=1, width=20)
    text.pack(pady=10)

    label3 = Label(window, text="Enter Weight")
    label3.pack(pady=10)
    weight_text = Text(window, height=1, width=20)
    weight_text.pack(pady=10)

    submit_button = Button(window, text="Submit", command=lambda: create_wrapper(cb.get(), text.get("1.0", "end-1c"), float(weight_text.get("1.0", "end-1c") or 0), pros, cons, pros_listbox, cons_listbox))
    submit_button.pack(pady=10)

def draw_nodes(canvas, pros, cons):
    canvas.delete("all")
    y_offset = 50
    for weight, node in pros.queue:
        canvas.create_oval(100, y_offset, 120, y_offset + 20, fill="blue")
        canvas.create_text(130, y_offset + 10, text=f"{node.name} {weight}", anchor="w")
        y_offset += 30
    y_offset = 50
    for weight, node in cons.queue:
        canvas.create_oval(400, y_offset, 420, y_offset + 20, fill="red")
        canvas.create_text(430, y_offset + 10, text=f"{node.name} {weight}", anchor="w")
        y_offset += 30

def create_wrapper(type, name, weight, pros, cons, pros_listbox, cons_listbox):
    create_node(type, name, weight, pros, cons)
    if type == "Pro":
        pros_listbox.insert(END, f"{name} ({weight})")
    else:
        cons_listbox.insert(END, f"{name} ({weight})")


if __name__ == "__main__":
    main()