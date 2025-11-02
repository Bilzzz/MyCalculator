import tkinter as tk

def click(event):
    global expression
    text = event.widget.cget("text")

    if text == "=":
        try:
            result = str(eval(expression))
            screen_var.set(result)
            expression = result
        except Exception:
            screen_var.set("Error")
            expression = ""
    elif text == "C":
        expression = ""
        screen_var.set("")
    else:
        expression += text
        screen_var.set(expression)

root = tk.Tk()
root.title("My Calculator")
root.geometry("350x500")

expression = ""
screen_var = tk.StringVar()

# Display screen
screen = tk.Entry(root, textvar=screen_var, font="lucida 20 bold")
screen.pack(fill="x", ipadx=8, padx=10, pady=10)

# Buttons layout
button_texts = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", "C", "=", "+"]
]

for row in button_texts:
    frame = tk.Frame(root)
    frame.pack()
    for text in row:
        button = tk.Button(frame, text=text, font="lucida 15 bold", width=5, height=2)
        button.pack(side="left", padx=5, pady=5)
        button.bind("<Button-1>", click)

root.mainloop()
