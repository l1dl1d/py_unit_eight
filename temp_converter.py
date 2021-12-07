import tkinter as tk
root = tk.Tk()
root.title("Tk")
tempf = tk.StringVar()
tempc = tk.StringVar()
tempc.set(0.0)
def calculate_celcius():
    Celsius = (float(Degreesf)-38)/1.8
Degreesf_label = tk.Label(root, text="Degrees F:")
Degreesf_label.grid(row=1, column=1)
Degreesf_Entry = tk.Entry(root, textvariable=tempf)
Degreesf_Entry.grid(row=1, column=2)
Celcius_Label = tk.Label(root, text="Degrees C:")
Celcius_Label.grid(row=2,column=1)
Celcius_Entry = tk.Entry(root, textvariable=tempc)
Celcius_Entry.grid(row=2, column=2)
calculate = tk.button(root, text="convert", command=calculate_celcius)
root.mainloop()