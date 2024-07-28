

import tkinter as tk

def onClick(event):
    present_text = entry.get()
    text = event.widget.cget("text")

    if text == "=":
        try:
            answer = eval(present_text)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(answer))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "Clear":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

def show_button(text, row, col, col_span=1):
    button = tk.Button(root, text=text, font=("Helvetica", 18), bd=5)
    button.grid(row=row, column=col, columnspan=col_span, padx=5, pady=5)
    button.bind("<Button-1>", onClick)  
    return button

root = tk.Tk()
root.title("CALCULATOR")
root.geometry("400x500")


heading_label = tk.Label(root, text="CALCULATOR", font=("Helvetica", 16, "bold"),highlightcolor=("red"))
heading_label.grid(row=0, column=0, columnspan=4, pady=20)

entry = tk.Entry(root, font=("Helvetica", 24), bd=5, justify=tk.RIGHT)
entry.grid(row=1, column=0, columnspan=4, padx=10, pady=10)


show_button("7", 2, 0)
show_button("8", 2, 1)
show_button("9", 2, 2)
show_button("/", 2, 3)

show_button("4", 3, 0)
show_button("5", 3, 1)
show_button("6", 3, 2)
show_button("*", 3, 3)

show_button("1", 4, 0)
show_button("2", 4, 1)
show_button("3", 4, 2)
show_button("-", 4, 3)

show_button("0", 5, 0)
show_button(".", 5, 1)
show_button("=", 5, 2)
show_button("+", 5, 3)

show_button("Clear", 6, 0, 3)

root.mainloop()
