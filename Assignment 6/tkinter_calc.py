import tkinter as tk

# window

window = tk.Tk()
window.minsize(265,250)

# entry

entry = tk.Entry(window, width=40, borderwidth=5)
entry.pack()

# number buttons

def click(n):
    entry.insert(tk.END, str(n))

button = tk.Button(window, text="1", width=10, command= lambda:click(1))
button.place(x=10, y=60-15)

button = tk.Button(window, text="2", width=10, command= lambda:click(2))
button.place(x=90, y=60-15)

button = tk.Button(window, text="3", width=10, command= lambda:click(3))
button.place(x=170, y=60-15)

button = tk.Button(window, text="4", width=10, command= lambda:click(4))
button.place(x=10, y=90-15)

button = tk.Button(window, text="5", width=10, command= lambda:click(5))
button.place(x=90, y=90-15)

button = tk.Button(window, text="6", width=10, command= lambda:click(6))
button.place(x=170, y=90-15)

button = tk.Button(window, text="7", width=10, command= lambda:click(7))
button.place(x=10, y=120-15)

button = tk.Button(window, text="8", width=10, command= lambda:click(8))
button.place(x=90, y=120-15)

button = tk.Button(window, text="9", width=10, command= lambda:click(9))
button.place(x=170, y=120-15)

button = tk.Button(window, text="0", width=10, command= lambda:click(0))
button.place(x=90, y=150-15)



# operators

def add():
    n1 = entry.get()
    entry.delete(0, tk.END)
    global i
    global math
    math = "add"
    i = int(n1)

button = tk.Button(window, text="+", width=10, command=add)
button.place(x=10, y=150-15)

def sub():
    n1 = entry.get()
    entry.delete(0, tk.END)
    global i
    global math
    math = "sub"
    i = int(n1)
    

button = tk.Button(window, text="-", width=10, command=sub)
button.place(x=170, y=150-15)

def mult():
    n1 = entry.get()
    entry.delete(0, tk.END)
    global i
    global math
    math = "mult"
    i = int(n1)
    

button = tk.Button(window, text="*", width=10, command=mult)
button.place(x=10, y=180-15)

def div():
    n1 = entry.get()
    entry.delete(0, tk.END)
    global i
    global math
    math = "div"
    i = int(n1)
    

button = tk.Button(window, text="/", width=10, command=div)
button.place(x=170, y=180-15)



def clear():
    entry.delete(len(entry.get())-1, tk.END)
    

button = tk.Button(window, text="clear", width=10, command=clear)
button.place(x=90, y=180-15)

def AC():
    entry.delete(0,tk.END)

button = tk.Button(window, text="AC", width=10, command=AC)
button.place(x=10, y=210-15)

def equal():
    n2 = entry.get()
    entry.delete(0, tk.END)
    global math
    if math == "add":
        entry.insert(0, i + int(n2))
    elif math == "sub":
        entry.insert(0, i - int(n2))
    elif math == "mult":
        entry.insert(0, i * int(n2))
    elif math == "div":
        entry.insert(0, i / int(n2))

button = tk.Button(window, text="=", width=10, command=equal)
button.place(x=170, y=210-15)



window.mainloop()