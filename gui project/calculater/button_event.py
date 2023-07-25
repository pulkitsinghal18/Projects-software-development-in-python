import tkinter as tk

# creating empty gui
root = tk.Tk()

def test(event):
    button_text = event.widget.cget('text')
    print('Button', button_text is 'pressed')


# properties
root.geometry('200x200')

#Adding 2 button
button_1 = tk.Button(root, text='1', width=5, height=2)
# right click event-<button-3>
button_1.bind('<Button-3>', test)
button_1.pack()


#display
root.mainloop()
