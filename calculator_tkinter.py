import tkinter as tk

window = tk.Tk()

window.title('Scientific Calculator')
window.geometry('500x700')
window.resizable(width=False, height=False)
window.configure(background="#B3AEAE")


for col in range(6):
    window.columnconfigure(col, weight=1)


result_label = tk.Entry(
    master=window,
    font=('sans-serif', 20, 'bold'),
    border=5,
    justify='right',
    state='readonly',
)
result_label.grid(row=0, column=0, columnspan=6, pady=(30, 30),)


buttons_features = [
    {'text': 'sin', 'bg': '#000000', 'command': print('Sin'), 'command': print('Sin')}, 
    {'text': '99', 'bg': '#000000', 'command': print('Sin')}, 
    {'text': '99', 'bg': '#000000', 'command': print('Sin')}, 
    {'text': '99', 'bg': '#000000', 'command': print('Sin')},
    {'text': '99', 'bg': '#000000', 'command': print('Sin')}, 
    {'text': '99', 'bg': '#000000', 'command': print('Sin')}, 
    {'text': '99', 'bg': '#000000', 'command': print('Sin')}, 
    {'text': '99', 'bg': '#000000', 'command': print('Sin')},
    {'text': '99', 'bg': '#000000', 'command': print('Sin')}, 
    {'text': '99', 'bg': '#000000', 'command': print('Sin')}, 
    {'text': '99', 'bg': '#000000', 'command': print('Sin')}, 
    {'text': '99', 'bg': '#000000', 'command': print('Sin')},
    {'text': '99', 'bg': '#000000', 'command': print('Sin')}, 
    {'text': '99', 'bg': '#000000', 'command': print('Sin')}, 
    {'text': '99', 'bg': '#000000', 'command': print('Sin')}, 
    {'text': '99', 'bg': '#000000', 'command': print('Sin')},
    {'text': '99', 'bg': '#000000', 'command': print('Sin')}, 
    {'text': '99', 'bg': '#000000', 'command': print('Sin')}, 
    {'text': '(', 'bg': '#000000', 'command': print('Sin')}, 
    {'text': ')', 'bg': '#000000', 'command': print('Sin')},
    {'text': '99', 'bg': '#000000', 'command': print('Sin')}, 
    {'text': '99', 'bg': '#000000', 'command': print('Sin')}, 
    {'text': '99', 'bg': '#000000', 'command': print('Sin')}, 
    {'text': '99', 'bg': '#000000', 'command': print('Sin')},
    {'text': '99', 'bg': '#000000', 'command': print('Sin')}, 
    {'text': '7', 'command': print('Sin')}, 
    {'text': '8', 'command': print('Sin')}, 
    {'text': '9', 'command': print('Sin')},
    {'text': '%', 'bg':'#858282', 'command': print('Sin')}, 
    {'text': '^', 'bg':'#858282', 'command': print('Sin')},
    {'text': '99', 'bg': '#000000', 'command': print('Sin'), 'command': print('Sin')}, 
    {'text': '4', 'command': print('Sin')}, 
    {'text': '5', 'command': print('Sin')}, 
    {'text': '6', 'command': print('Sin')}, 
    {'text': '*', 'bg':'#858282', 'command': print('Sin')}, 
    {'text': '/', 'bg':'#858282', 'command': print('Sin')}, 
    {'text': 'AC', 'bg': '#DC1212', 'command': print('Sin')}, 
    {'text': '1', 'command': print('Sin')}, 
    {'text': '2', 'command': print('Sin')}, 
    {'text': '3', 'command': print('Sin')}, 
    {'text': '+', 'bg':'#858282', 'command': print('Sin')}, 
    {'text': '-', 'bg':'#858282', 'command': print('Sin')}, 
    {'text': 'CE', 'bg': '#DC1212', 'command': print('Sin')}, 
    {'text': '+/-', 'command': print('Sin')}, 
    {'text': '0', 'command': print('Sin')}, 
    {'text': '.', 'command': print('Sin')}, 
    {'text': '=', 'bg':'#858282', 'command': print('Equal')},
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
        font=('Helvetica', 18, 'bold'),
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