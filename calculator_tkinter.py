import tkinter as tk

window = tk.Tk()

window.title('Scientific Calculator')
window.geometry('500x700')
window.resizable(width=False, height=False)
window.configure(background="#818181")


result_label = tk.Entry(
    master=window,
    font=('sans-serif', 20, 'bold'),
    border=5,
    justify='right'
)
result_label.grid(row=0, column=1, padx=43, pady=15)

buttons = [
    {'text': ''}, {'text': ''}, {'text': ''}, {'text': ''},
    {'text': ''}, {'text': ''}, {'text': ''}, {'text': ''},
    {'text': ''}, {'text': ''}, {'text': ''}, {'text': ''},
    {'text': ''}, {'text': ''}, {'text': ''}, {'text': ''},
    {'text': ''}, {'text': ''}, {'text': ''}, {'text': ''},
    {'text': ''}, {'text': ''}, {'text': ''}, {'text': ''},
    {'text': ''}, {'text': '7', 'bg': 'black',}, {'text': '8', 'bg': 'black',},
    {'text': '9', 'bg': 'black',}, {'text': '%'}, {'text': '^'}, {'text': ''},
    {'text': '4', 'bg': 'black',}, {'text': '5', 'bg': 'black',}, 
    {'text': '6', 'bg': 'black',}, {'text': '*'}, {'text': '/'},
    {'text': 'AC', 'bg': 'red',}, {'text': '1', 'bg': 'black',}, 
    {'text': '2', 'bg': 'black',}, {'text': '3', 'bg': 'black',}, 
    {'text': '+', 'height': 6}, {'text': '-'}, {'text': 'CE', 'bg': 'red',}, 
    {'text': '+/-', 'bg': 'black',}, {'text': '0', 'bg': 'black',}, 
    {'text': '.', 'bg': 'black',}, {'text': '='},
]

window.mainloop()
