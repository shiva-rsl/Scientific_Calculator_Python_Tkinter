import math
import tkinter as tk
from main import *


window = tk.Tk()

window.title('Scientific Calculator')
window.geometry('500x700')
window.resizable(width=False, height=False)
window.configure(background="#B3AEAE")


for col in range(6):
    window.columnconfigure(col, weight=1)


result_entry = tk.Entry(
    master=window,
    font=('sans-serif', 20, 'bold'),
    border=5,
    justify='right',
)
result_entry.grid(row=0, column=0, columnspan=6, pady=(30, 30),)

# -----------------------------------------------------------------------------------



operation = ''


def button_sin():
    result = f'sin('
    result_entry.delete(0, tk.END)
    result_entry.insert(0, result)


def button_cos():
    result = f'cos('
    result_entry.delete(0, tk.END)
    result_entry.insert(0, result)


def button_tan():
    result = f'tan('
    result_entry.delete(0, tk.END)
    result_entry.insert(0, result)


def button_log_ten():
    result = f'log('
    result_entry.delete(0, tk.END)
    result_entry.insert(0, result)


def button_ln():
    result = f'ln('
    result_entry.delete(0, tk.END)
    result_entry.insert(0, result)


def button_log_two():
    result = f'log('
    result_entry.delete(0, tk.END)
    result_entry.insert(0, result)


def button_sqrt():
    num = result_entry.get()
    if num == '':
        result = f'√('
        result_entry.insert(0, result)
    else:
        result = f'{num}x√('
        result_entry.delete(0, tk.END)
        result_entry.insert(0, result)


def button_abs():
    result_entry.insert(tk.END, '|')

def button_sinh():
    result = f'sinh('
    result_entry.delete(0, tk.END)
    result_entry.insert(0, result)


def button_cosh():
    result = f'cosh('
    result_entry.delete(0, tk.END)
    result_entry.insert(0, result)


def button_tanh():
    result = f'tanh('
    result_entry.delete(0, tk.END)
    result_entry.insert(0, result)


def button_factorial():
    result_entry.insert(1, '!')


def button_power_two():
    # float or int
    num = result_entry.get()
    print(type(num))
    result = f'{num}^(2)'
    result_entry.delete(0, tk.END)
    result_entry.insert(0, result)


def button_power_three():
    # float or int
    num = result_entry.get()
    print(type(num))
    result = f'{num}^(3)'
    result_entry.delete(0, tk.END)
    result_entry.insert(0, result)

def button_pi():
    num = result_entry.get()
    if num == '':
        result_entry.insert(0, '\u03C0')
    else:
        result_entry.delete(0, tk.END)
        result_entry.insert(0, f'2×\u03C0')


def button_e():
    num = result_entry.get()
    if num == '':
        result_entry.insert(0, 'e')
    else:
        result_entry.delete(0, tk.END)
        result_entry.insert(0, f'2×e')


def button_ac():
    length = len(result_entry.get())
    result_entry.delete(length-1)

def button_ce():
    result_entry.delete(0, tk.END)


def button_plus():
    global operation
    operation = '+'
    first_num = result_entry.get()
    return first_num


def button_numbers(num):
    if operation != '':
        result_entry.delete(0, tk.END)
    for i in range(10):
        if i == num:
            result_entry.insert('end', num)






# -----------------------------------------------------------------------------------


buttons_features = [
    {'text': 'sin', 'bg': '#000000', 'command': lambda: button_sin()}, 
    {'text': 'cos', 'bg': '#000000', 'command': lambda: button_cos()}, 
    {'text': 'tan', 'bg': '#000000', 'command': lambda: button_tan()}, 
    {'text': 'lg10', 'bg': '#000000', 'command': lambda: button_log_ten()},
    {'text': 'ln', 'bg': '#000000', 'command': lambda: button_ln()}, 
    {'text': 'lg2', 'bg': '#000000', 'command': lambda: button_log_two()}, 
    {'text': 'sinh', 'bg': '#000000', 'command': lambda: button_sinh()}, 
    {'text': 'cosh', 'bg': '#000000', 'command': lambda: button_cosh()},
    {'text': 'tanh', 'bg': '#000000', 'command': lambda: button_tanh()}, 
    {'text': 'x!', 'bg': '#000000', 'command': lambda: button_factorial()}, 
    {'text': '1/x', 'bg': '#000000', 'command': lambda: print('Sin')}, 
    {'text': '√', 'bg': '#000000', 'command': lambda: button_sqrt()},
    {'text': 'Exp', 'bg': '#000000', 'command': lambda: print('Sin')}, 
    {'text': 'Deg', 'bg': '#000000', 'command': lambda: print('Sin')}, 
    {'text': 'Rad', 'bg': '#000000', 'command': lambda: print('Sin')}, 
    {'text': '2^', 'bg': '#000000', 'command': lambda: print('Sin')},
    {'text': '10^', 'bg': '#000000', 'command': lambda: print('Sin')}, 
    {'text': 'e^', 'bg': '#000000', 'command': lambda: print('Sin')}, 
    {'text': '(', 'bg': '#000000', 'command': lambda: print('Sin')}, 
    {'text': ')', 'bg': '#000000', 'command': lambda: print('Sin')},
    {'text': '|x|', 'bg': '#000000', 'command': lambda: button_abs()}, 
    {'text': 'x²', 'bg': '#000000', 'command': lambda: button_power_two()}, 
    {'text': 'x³', 'bg': '#000000', 'command': lambda: button_power_three()}, 
    {'text': 'x^y', 'bg': '#000000', 'command': lambda: print('Sin')},
    {'text': '\u03C0', 'bg': '#000000', 'command': lambda: button_pi()}, 
    {'text': '7', 'command': lambda: button_numbers(7)}, 
    {'text': '8', 'command': lambda: button_numbers(8)}, 
    {'text': '9', 'command': lambda: button_numbers(9)},
    {'text': '%', 'bg':'#858282', 'command': lambda: print('Sin')}, 
    {'text': '^', 'bg':'#858282', 'command': lambda: print('Sin')},
    {'text': 'e', 'bg': '#000000', 'command': lambda: button_e()}, 
    {'text': '4', 'command': lambda: button_numbers(4)}, 
    {'text': '5', 'command': lambda: button_numbers(5)}, 
    {'text': '6', 'command': lambda: button_numbers(6)}, 
    {'text': '*', 'bg':'#858282', 'command': lambda: print('Sin')}, 
    {'text': '÷', 'bg':'#858282', 'command': lambda: print('Sin')}, 
    {'text': 'AC', 'bg': '#DC1212', 'command': lambda: button_ac()}, 
    {'text': '1', 'command': lambda: button_numbers(1)}, 
    {'text': '2', 'command': lambda: button_numbers(2)}, 
    {'text': '3', 'command': lambda: button_numbers(3)}, 
    {'text': '+', 'bg':'#858282', 'command': lambda: button_plus()}, 
    {'text': '-', 'bg':'#858282', 'command': lambda: print('Sin')}, 
    {'text': 'CE', 'bg': '#DC1212', 'command': lambda: button_ce()}, 
    {'text': '+/-', 'command': lambda: print('Sin')}, 
    {'text': '0', 'command': lambda: button_numbers(0)}, 
    {'text': '.', 'command': lambda: print('Sin')}, 
    {'text': '=', 'bg':'#858282', 'command': lambda: print('=')},
]


calc_buttons = []
plus_button = None
equal_button = None
skip_indexes = []


for key_object in buttons_features:
    bg_color = key_object.get('bg')
    fg_color = {
        '#000000': "#FFFFFF",
        '#DC1212': "#FFFFFF",
    }
    active_bg = {
        '#000000': '#171B17',
        '#DC1212': '#E93939',
        '#858282': "#8F8C8C",
    }
    active_fg = {
        '#DC1212': '#FFFFFF',
        '#000000': "#FFFFFF",
    }
    button = tk.Button(
        master=window,
        text=key_object['text'],
        bg=bg_color,
        fg=fg_color.get(bg_color, "#000000"),
        font=('DejaVu Sans', 18,),
        relief='raised',
        bd=5,
        activebackground=active_bg.get(bg_color, '#c0c0c0'),
        activeforeground=active_fg.get(bg_color, '#000000'),
        padx=15,
        pady=15,
        highlightthickness=0,
        borderwidth=2,
        cursor='hand2',
        command=key_object['command']  
    )
    calc_buttons.append(button)


for index, button in enumerate(calc_buttons):
    if button['text'] == '+':
        plus_button = button
        skip_indexes.append(index)
    elif button['text'] == '=':
        equal_button = button
        skip_indexes.append(index)


rows = 8
cols = 6


for index, button in enumerate(calc_buttons):
    if index in skip_indexes:
        continue
    row = index // cols + 1
    col = index % cols
    button.grid(row=row, column=col, sticky='nsew', padx=5, pady=5)


plus_button.grid(row=7, column=4, rowspan=2, sticky='nsew', padx=5, pady=5)

equal_button.grid(row=8, column=5, sticky='nsew', padx=5, pady=5)


for row in range(1, rows + 2):
    window.rowconfigure(row, weight=1)


window.mainloop()

