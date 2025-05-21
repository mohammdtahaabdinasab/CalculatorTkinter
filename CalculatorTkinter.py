import tkinter as tk

calculation = ""
display = None  

def number_button_click(number):
    global calculation
    calculation = calculation + str(number)
    display.delete(0, tk.END)
    display.insert(tk.END, calculation)

def plus_button_click():
    global calculation
    calculation = calculation + "+"
    display.delete(0, tk.END)
    display.insert(tk.END, calculation)

def minus_button_click():
    global calculation
    calculation = calculation + "-"
    display.delete(0, tk.END)
    display.insert(tk.END, calculation)

def multiply_button_click():
    global calculation
    calculation = calculation + "*"
    display.delete(0, tk.END)
    display.insert(tk.END, calculation)

def divide_button_click():
    global calculation
    calculation = calculation + "/"
    display.delete(0, tk.END)
    display.insert(tk.END, calculation)

def clear_button_click():
    global calculation
    calculation = ""
    display.delete(0, tk.END)

def equals_button_click():
    global calculation
    try:
        result = eval(calculation)
        display.delete(0, tk.END)
        display.insert(tk.END, str(result))
        calculation = str(result)
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")
        calculation = ""

window = tk.Tk()
window.title("Calculator")
window.geometry("250x300")
window.configure(bg="#f0f0f0")

display = tk.Entry(window, width=15, font=('Arial', 18), justify='right')
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


tk.Button(window, text="1", width=5, height=2, bg="#ffffff",command=lambda: number_button_click(1)).grid(row=1, column=0, padx=5, pady=5)
tk.Button(window, text="2", width=5, height=2, bg="#ffffff",command=lambda: number_button_click(2)).grid(row=1, column=1, padx=5, pady=5)
tk.Button(window, text="3", width=5, height=2, bg="#ffffff",command=lambda: number_button_click(3)).grid(row=1, column=2, padx=5, pady=5)

tk.Button(window, text="4", width=5, height=2, bg="#ffffff",command=lambda: number_button_click(4)).grid(row=2, column=0, padx=5, pady=5)
tk.Button(window, text="5", width=5, height=2, bg="#ffffff",command=lambda: number_button_click(5)).grid(row=2, column=1, padx=5, pady=5)
tk.Button(window, text="6", width=5, height=2, bg="#ffffff",command=lambda: number_button_click(6)).grid(row=2, column=2, padx=5, pady=5)

tk.Button(window, text="7", width=5, height=2, bg="#ffffff",command=lambda: number_button_click(7)).grid(row=3, column=0, padx=5, pady=5)
tk.Button(window, text="8", width=5, height=2, bg="#ffffff",command=lambda: number_button_click(8)).grid(row=3, column=1, padx=5, pady=5)
tk.Button(window, text="9", width=5, height=2, bg="#ffffff",command=lambda: number_button_click(9)).grid(row=3, column=2, padx=5, pady=5)

tk.Button(window, text="0", width=5, height=2, bg="#ffffff",command=lambda: number_button_click(0)).grid(row=4, column=0, padx=5, pady=5)
tk.Button(window, text="Clear", width=5, height=2, bg="#ff9999",command=clear_button_click).grid(row=4, column=1, padx=5, pady=5)
tk.Button(window, text="=", width=5, height=2, bg="#99ccff",command=equals_button_click).grid(row=4, column=2, padx=5, pady=5)

tk.Button(window, text="+", width=5, height=2, bg="#ffcc99",command=plus_button_click).grid(row=1, column=3, padx=5, pady=5)
tk.Button(window, text="-", width=5, height=2, bg="#ffcc99",command=minus_button_click).grid(row=2, column=3, padx=5, pady=5)
tk.Button(window, text="*", width=5, height=2, bg="#ffcc99",command=multiply_button_click).grid(row=3, column=3, padx=5, pady=5)
tk.Button(window, text="/", width=5, height=2, bg="#ffcc99",command=divide_button_click).grid(row=4, column=3, padx=5, pady=5)

signature = tk.Label(window, text="Created by Mohammad Taha Abdinasab",font=('Arial', 8), bg="#f0f0f0")
signature.grid(row=5, column=0, columnspan=4, pady=10)

window.mainloop() 
