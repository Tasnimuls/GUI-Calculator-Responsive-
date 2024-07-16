import tkinter as tk

field_text = ""

def update_input(char):
    global field_text
    field_text += char
    show_field(field_text)

def clear_field():
    global field_text
    field_text = ""
    show_field(field_text)

def show_field(text):
    field.delete(0, tk.END)
    field.insert(0, text)

def evaluate():
    global field_text
    try:
        result = eval(str(field_text))
        field_text = str(result)
        show_field(field_text)
    except:
        show_field("ERROR")

root = tk.Tk()
root.geometry("683x632")
# root.minsize(683, 632)
# root.maxsize(683, 632)

field = tk.Entry(root, text="", bg = "#021c36", font=('Arial', 45), width=20, fg="white")
field.grid(row=0, column=0, columnspan=4, pady=5, sticky="nsew")

buttons = [
    ("1",1,0), ("2",1,1), ("3",1,2), ("4",2,0), ("5",2,1), ("6",2,2), ("7",3,0), ("8",3,1), ("9",3,2), ("0",4,1), 
    ("+",1,3), ("-",2,3), ("*",3,3), ("/",4,3), ("=",5,2), ("(",4,0), (")",4,2), ("C",5,1), (".",5,0)
]
for (text, row, column) in buttons:
    if text == "=":
        b = tk.Button(root, text=text, bg = "#021c36", font=('Arial', 40), fg="white", command=evaluate, width=10)
        b.grid(row=row, column=column, columnspan=2, sticky="nsew")
    elif text == "C":
        b = tk.Button(root, text=text, bg = "#021c36", font=('Arial', 40), fg="white", command=clear_field, width=5)
        b.grid(row=row, column=column, padx=3, pady=2, sticky="nsew")
    else:
        b = tk.Button(root, text=text, bg = "#021c36", font=('Arial', 40), fg="white", command=lambda t=text: update_input(t), width=5,)
        b.grid(row=row, column=column, padx=3, pady=2, sticky="nsew")

for i in range(6):
    if i <= 3:
        root.columnconfigure(i, weight=1)
        root.rowconfigure(i, weight=1)
    else:
        root.rowconfigure(i, weight=1)


root.mainloop()