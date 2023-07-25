import tkinter as tk

# let's see what is inside tkinter module
# print(dir(tk))

# let's create the base gui
root = tk.Tk()

# let's create test function
def test(event):
    button_pressed = event.widget.cget('text')
    if button_pressed == '=':
        expression = label.cget('text')
        result = eval(expression)
        label.config(text=result)
    elif button_pressed == "CE" or button_pressed == "C" or button_pressed == "DEL":
        label.config(text='')
    else:
        label_text = label.cget('text')
        if label_text == '0':
            label.config(text=button_pressed)
        else:
            label_text += button_pressed
            label.config(text=label_text)

#gui properties
root.geometry('320x455') # change size
root.resizable(width=False, height=False) # fixed size
root.title('calculater') # add title
root.iconbitmap('calculater icon.ico')
root.config(bg='#FFFDD0') #giving background color

# adding widgets now
# label widget to display text
label = tk.Label(root, text='0',  font=('Comic Sans MS', 30), anchor='e', padx=10, bg='#FFFDD0')
label.pack(pady=(65, 10), fill='x')
print(label.cget('bg'))


# let's add a new container
frame = tk.Frame(root, bg='#FFFDD0')
frame.pack(fill='both')

# add buttons row 0
btn_percent = tk.Button(frame, text='%', width=9, height=3, bg='#ffffff', relief='groove', font=('Trebuchet, 9'))
btn_ce = tk.Button(frame, text='CE', width=9, height=3, bg='#ffffff', relief='groove', font=('Trebuchet, 9'))
btn_c = tk.Button(frame, text='C', width=9, height=3, bg='#ffffff', relief='groove', font=('Trebuchet, 9'))
btn_delete = tk.Button(frame, text='DEL', width=9, height=3, bg='#ffffff', relief='groove', font=('Trebuchet, 9'))
btn_percent.grid(row=0, column=0, padx=3, pady=3)
btn_ce.grid(row=0, column=1, padx=3, pady=3)
btn_c.grid(row=0, column=2, padx=3, pady=3)
btn_delete.grid(row=0, column=3, padx=3, pady=3)

# left click event
btn_percent.bind('<Button-1>',test)
btn_ce.bind('<Button-1>',test)
btn_c.bind('<Button-1>',test)
btn_delete.bind('<Button-1>',test)

# add buttons row 1
btn_7 = tk.Button(frame, text='7', width=9, height=3, bg='#ffffff', relief='groove', font=('Trebuchet, 9'))
btn_8 = tk.Button(frame, text='8', width=9, height=3, bg='#ffffff', relief='groove', font=('Trebuchet, 9'))
btn_9 = tk.Button(frame, text='9', width=9, height=3, bg='#ffffff', relief='groove', font=('Trebuchet, 9'))
btn_x = tk.Button(frame, text='*', width=9, height=3, bg='#ffffff', relief='groove', font=('Trebuchet, 9'))
btn_7.grid(row=1, column=0, padx=3, pady=3)
btn_8.grid(row=1, column=1, padx=3, pady=3)
btn_9.grid(row=1, column=2, padx=3, pady=3)
btn_x.grid(row=1, column=3, padx=3, pady=3)

# left click event
btn_7.bind('<Button-1>',test)
btn_8.bind('<Button-1>',test)
btn_9.bind('<Button-1>',test)
btn_x.bind('<Button-1>',test)


# add buttons row 2
btn_4 = tk.Button(frame, text='4', width=9, height=3, bg='#ffffff', relief='groove', font=('Trebuchet, 9'))
btn_5 = tk.Button(frame, text='5', width=9, height=3, bg='#ffffff', relief='groove', font=('Trebuchet, 9'))
btn_6 = tk.Button(frame, text='6', width=9, height=3, bg='#ffffff', relief='groove', font=('Trebuchet, 9'))
btn_div = tk.Button(frame, text='-', width=9, height=3, bg='#ffffff', relief='groove', font=('Trebuchet, 9'))
btn_4.grid(row=2, column=0, padx=3, pady=3)
btn_5.grid(row=2, column=1, padx=3, pady=3)
btn_6.grid(row=2, column=2, padx=3, pady=3)
btn_div.grid(row=2, column=3, padx=3, pady=3) 

# left click event
btn_4.bind('<Button-1>',test)
btn_5.bind('<Button-1>',test)
btn_6.bind('<Button-1>',test)
btn_div.bind('<Button-1>',test)

# add buttons row 3
btn_1 = tk.Button(frame, text='1', width=9, height=3, bg='#ffffff', relief='groove', font=('Trebuchet, 9'))
btn_2 = tk.Button(frame, text='2', width=9, height=3, bg='#ffffff', relief='groove', font=('Trebuchet, 9'))
btn_3 = tk.Button(frame, text='3', width=9, height=3, bg='#ffffff', relief='groove', font=('Trebuchet, 9'))
btn_div = tk.Button(frame, text='+', width=9, height=3, bg='#ffffff', relief='groove', font=('Trebuchet, 9'))
btn_1.grid(row=3, column=0, padx=3, pady=3)
btn_2.grid(row=3, column=1, padx=3, pady=3)
btn_3.grid(row=3, column=2, padx=3, pady=3)
btn_div.grid(row=3, column=3, padx=3, pady=3) 

# left click event
btn_1.bind('<Button-1>',test)
btn_2.bind('<Button-1>',test)
btn_3.bind('<Button-1>',test)
btn_div.bind('<Button-1>',test)

# add buttons row 3
btn_divide = tk.Button(frame, text='/', width=9, height=3, bg='#ffffff', relief='groove', font=('Trebuchet, 9'))
btn_0 = tk.Button(frame, text='0', width=9, height=3, bg='#ffffff', relief='groove', font=('Trebuchet, 9'))
btn_decimal = tk.Button(frame, text='.', width=9, height=3, bg='#ffffff', relief='groove', font=('Trebuchet, 9'))
btn_equal = tk.Button(frame, text='=', width=9, height=3, bg='#1e90ff', fg='#ffffff', relief='groove', font=('Trebuchet, 9'))
btn_divide.grid(row=4, column=3, padx=3, pady=3)
btn_0.grid(row=4, column=1, padx=3, pady=3)
btn_decimal.grid(row=4, column=2, padx=3, pady=3)
btn_equal.grid(row=4, column=0, padx=3, pady=3) 

# left click event
btn_divide.bind('<Button-1>',test)
btn_0.bind('<Button-1>',test)
btn_decimal.bind('<Button-1>',test)
btn_equal.bind('<Button-1>',test)



# let's run mainloop
root.mainloop()