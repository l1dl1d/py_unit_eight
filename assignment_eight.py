import tkinter as tk
root = tk.Tk()
root.title("Calculator")
def one():
    var = equation.get()
    var = var + "1"
    equation.set(var)
def two():
    tar = equation.get()
    tar = tar + "2"
    equation.set(tar)
def three():
    thar = equation.get()
    thar = thar + "3"
    equation.set(thar)
def four():
    far = equation.get()
    far = far + "4"
    equation.set(far)
def five():
    fir = equation.get()
    fir = fir + "5"
    equation.set(fir)
def six():
    sar = equation.get()
    sar = sar + "6"
    equation.set(sar)
def seven():
    ser = equation.get()
    ser = ser + "7"
    equation.set(ser)
def eight():
    er = equation.get()
    er = er + "8"
    equation.set(er)
def nine():
    pass
def zero():
    pass
equation = tk.StringVar()
Entry_entry = tk.Entry(root, textvariable=equation)
Entry_entry.grid(row=1, column=1)
one = tk.Button(root, text="1", command=one)
one.grid(row=2, column=1)
two = tk.Button(root, text="2", command=two)
two.grid(row=2, column=2)
three = tk.Button(root, text="3", command=three)
three.grid(row=2, column=3)
four = tk.Button(root, text="4", command=four)
four.grid(row=3, column=1)
five = tk.Button(root, text="5", command=five)
five.grid(row=3, column=2)
six = tk.Button(root, text="6", command=six)
six.grid(row=3, column=3)
seven = tk.Button(root, text="7", command=seven)
seven.grid(row=4, column=1)
eight = tk.Button(root, text="8", command=eight)
eight.grid(row=4, column=2)
nine = tk.Button(root, text="9", command=nine)
nine.grid(row=4, column=3)
zero = tk.Button(root, text="0", command=zero)
zero.grid(row=5, column=2)

root.mainloop()