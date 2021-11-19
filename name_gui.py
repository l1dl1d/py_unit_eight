import tkinter as tk
root = tk.Tk()
root.title("name")
response_to_hello_label = tk.Label(root, text="hello ", )
response_to_hello_label.grid(row=2, column=2)
response_to_hello_entry = tk.Entry(root)
root.mainloop()