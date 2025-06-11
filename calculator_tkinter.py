import tkinter as tk

window = tk.Tk()

window.title('Scientific Calculator')
window.geometry('500x700')
window.resizable(width=False, height=False)
window.configure(background='#818181')

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)

result_label = tk.Entry(
    master=window,
    font=('sans-serif', 20, 'bold'),
    border=5,
    justify='right',
    state='readonly',
)
result_label.grid(row=0, column=0, columnspan=6, pady=(30, 10),)


buttons_features = [
    {'text': 'sin', 'bg': '#060706',}, {'text': '99', 'bg': '#060706'}, {'text': '99', 'bg': '#060706'}, {'text': '99', 'bg': '#060706'},
    {'text': '99', 'bg': '#060706'}, {'text': '99', 'bg': '#060706'}, {'text': '99', 'bg': '#060706'}, {'text': '99', 'bg': '#060706'},
    {'text': '99', 'bg': '#060706'}, {'text': '99', 'bg': '#060706'}, {'text': '99', 'bg': '#060706'}, {'text': '99', 'bg': '#060706'},
    {'text': '99', 'bg': '#060706'}, {'text': '99', 'bg': '#060706'}, {'text': '99', 'bg': '#060706'}, {'text': '99', 'bg': '#060706'},
    {'text': '99', 'bg': '#060706'}, {'text': '99', 'bg': '#060706'}, {'text': '(', 'bg': '#060706'}, {'text': ')', 'bg': '#060706'},
    {'text': '99', 'bg': '#060706'}, {'text': '99', 'bg': '#060706'}, {'text': '99', 'bg': '#060706'}, {'text': '99', 'bg': '#060706'},
    {'text': '99', 'bg': '#060706'}, {'text': '7'}, {'text': '8'}, {'text': '9'},
    {'text': '%', 'bg':'#858282'}, {'text': '^', 'bg':'#858282'},
    {'text': '99', 'bg': '#060706'}, {'text': '4'}, {'text': '5'}, {'text': '6'}, 
    {'text': '*', 'bg':'#858282'}, {'text': '/', 'bg':'#858282'}, 
    {'text': 'AC', 'bg': '#DC1212'}, {'text': '1'}, {'text': '2'}, {'text': '3'}, 
    {'text': '+', 'bg':'#858282'}, {'text': '-', 'bg':'#858282'}, 
    {'text': 'CE', 'bg': '#DC1212'}, {'text': '+/-'}, {'text': '0'}, {'text': '.'}, 
    {'text': '=', 'bg':'#858282'},
]


calc_buttons = []
plus_button = None
equal_button = None
skip_indexes = []


for key_object in buttons_features:
    bg = key_object.get('bg')
    fg = 
    



window.mainloop()