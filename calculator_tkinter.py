import math
import tkinter as tk
from main import *


window = tk.Tk()

window.title('Scientific Calculator')
window.geometry('500x760')
window.resizable(width=False, height=False)
window.configure(background="#B3AEAE")


for col in range(6):
    window.columnconfigure(col, weight=1)


result_label = tk.Label(
    master=window,
    font=('sans-serif', 20, 'bold'),
    width=20,
    height=2,
    background="#B3AEAE"
)
result_label.grid(row=0, column=0, columnspan=6, pady=(5,5))


result_entry = tk.Entry(
    master=window,
    font=('sans-serif', 20, 'bold'),
    border=5,
    justify='right',
)
result_entry.grid(row=1, column=0, columnspan=6, pady=(5, 10),)

# -----------------------------------------------------------------------------------



def sin_cos_tan_operations(operator):

    calc_result = result_entry.get()

    if calc_result == '' :
        result = f'{operator}('
        result_entry.delete(0, tk.END)
        result_entry.insert(0, result)

    elif calc_result[-1] == '(':
        calc_result = result_entry.get()
        result = f'{calc_result}{operator}('
        result_entry.delete(0, tk.END)
        result_entry.insert(0, result)

    else:
        result = f'{calc_result} × {operator}('
        result_entry.delete(0, tk.END)
        result_entry.insert(0, result)


def button_sin():
    sin_cos_tan_operations('sin')


def button_cos():
    sin_cos_tan_operations('cos')


def button_tan():
    sin_cos_tan_operations('tan')


def button_log_ten():
    result = 'log('
    result_entry.delete(0, tk.END)
    result_entry.insert(0, result)


def button_ln():

    calc_result = result_entry.get()

    if calc_result == '':
        result = 'ln('
        result_entry.insert(0, result)

    elif calc_result[-1] == '(':
        calc_result = result_entry.get()
        result = f'{calc_result}ln('
        result_entry.delete(0, tk.END)
        result_entry.insert(0, result)

    else:
        result = f'{calc_result}×ln('
        result_entry.delete(0, tk.END)
        result_entry.insert(0, result)


def button_log_two():
    result = 'log('
    result_entry.delete(0, tk.END)
    result_entry.insert(0, result)


def button_sinh():
    sin_cos_tan_operations('sinh')


def button_cosh():
    sin_cos_tan_operations('cosh')


def button_tanh():
    sin_cos_tan_operations('tanh')


def button_factorial():
    num = int(result_entry.get())
    result = math.factorial(num)
    result_entry.delete(0, tk.END)
    result_entry.insert(0, result)
    result_label['text'] = f'{num}! = {result}'


def button_sqrt():
    num = int(result_entry.get())
    calc_result = math.sqrt(num)

    if num == '':
        result = '√('
        result_entry.insert(0, result)
    else:
        result = f'{num}×√('
        result_entry.delete(0, tk.END)
        result_entry.insert(0, result)
    
    return calc_result


def button_parenthes_start():
    result_entry.insert(tk.END, '(')


def button_parenthes_end():
    result_entry.insert(tk.END, ')')


def button_abs():
    result_entry.insert(tk.END, '|')


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
        result_entry.insert(0, '2×e')


def button_ac():
    length = len(result_entry.get())
    result_entry.delete(length-1)

def button_ce():
    result_entry.delete(0, tk.END)
    result_label['text'] = ''


def button_negative():
    calc_state = result_entry.get()
    if calc_state == '':
        result = '(-'
        result_entry.insert(tk.END, result)
    else:
        result = f'(-{calc_state}'
        result_entry.delete(0, tk.END)
        result_entry.insert(0, result)


def button_dot():
    calc_num = result_entry.get()
    if calc_num == '':
        result = '0.'
        result_entry.insert(0, result)
    else:
        result_entry.insert(tk.END, '.')


def button_numbers(num):
    for i in range(10):
        if i == num:
            result_entry.insert('end', num)


def button_main_operations(operator):
    result_entry.insert(tk.END, operator)


def button_equal():
    operation = result_entry.get()
    result = str(eval(operation))
    result_label['text'] = f'{operation} = {result}'
    result_entry.delete(0, tk.END)
    result_entry.insert(0, result)


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
    {'text': '(', 'bg': '#000000', 'command': lambda: button_parenthes_start()}, 
    {'text': ')', 'bg': '#000000', 'command': lambda: button_parenthes_end()},
    {'text': '|x|', 'bg': '#000000', 'command': lambda: button_abs()}, 
    {'text': 'x²', 'bg': '#000000', 'command': lambda: button_power_two()}, 
    {'text': 'x³', 'bg': '#000000', 'command': lambda: button_power_three()}, 
    {'text': 'x^y', 'bg': '#000000', 'command': lambda: print('Sin')},
    {'text': '\u03C0', 'bg': '#000000', 'command': lambda: button_pi()}, 
    {'text': '7', 'command': lambda: button_numbers(7)}, 
    {'text': '8', 'command': lambda: button_numbers(8)}, 
    {'text': '9', 'command': lambda: button_numbers(9)},
    {'text': '%', 'bg':'#858282', 'command': lambda: button_main_operations('%')}, 
    {'text': '^', 'bg':'#858282', 'command': lambda: button_main_operations('^')},
    {'text': 'e', 'bg': '#000000', 'command': lambda: button_e()}, 
    {'text': '4', 'command': lambda: button_numbers(4)}, 
    {'text': '5', 'command': lambda: button_numbers(5)}, 
    {'text': '6', 'command': lambda: button_numbers(6)}, 
    {'text': '*', 'bg':'#858282', 'command': lambda: button_main_operations('*')}, 
    {'text': '÷', 'bg':'#858282', 'command': lambda: button_main_operations('/')}, 
    {'text': 'AC', 'bg': '#DC1212', 'command': lambda: button_ac()}, 
    {'text': '1', 'command': lambda: button_numbers(1)}, 
    {'text': '2', 'command': lambda: button_numbers(2)}, 
    {'text': '3', 'command': lambda: button_numbers(3)}, 
    {'text': '+', 'bg':'#858282', 'command': lambda: button_main_operations('+')}, 
    {'text': '-', 'bg':'#858282', 'command': lambda: button_main_operations('-')}, 
    {'text': 'CE', 'bg': '#DC1212', 'command': lambda: button_ce()}, 
    {'text': '+/-', 'command': lambda: button_negative()}, 
    {'text': '0', 'command': lambda: button_numbers(0)}, 
    {'text': '.', 'command': lambda: button_dot()}, 
    {'text': '=', 'bg':'#858282', 'command': lambda: button_equal()},
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
    row = index // cols + 2
    col = index % cols
    button.grid(row=row, column=col, sticky='nsew', padx=5, pady=5)


plus_button.grid(row=8, column=4, rowspan=2, sticky='nsew', padx=5, pady=5)

equal_button.grid(row=9, column=5, sticky='nsew', padx=5, pady=5)


for row in range(1, rows + 3):
    window.rowconfigure(row, weight=1)


window.mainloop()

