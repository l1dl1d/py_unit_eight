import tkinter as tk
root = tk.Tk()
root.title("hello")
hello_world_label = tk.Label(root, text="Hello, World")
hello_world_label.grid(row=1, column=2)
root.mainloop()