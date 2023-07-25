# import tk
import tkinter as tk

# importing ttk module
from tkinter import ttk

# let's get the language list in this file
import backend

import googletrans
language_translation = googletrans.Translator()

#let's create the do_translation function
def do_translation():
    # stap 1--> get/read the source and target language from the combobox
    source_lang = source_cb.get()
    target_lang = target_cb.get()

    # stap 2--> let's fatch what user has written inn the textbox
    user_message =  input_text.get(1.0, tk.END)
    
    # stap 3---> let's do the translation
    output= language_translator.Translate(text=user_message, src=source_lang, dest=target_lang)
    print(output)

# let's create the language list
languages = backend.get_languages()


# create gui
root = tk.Tk()
root.geometry('700x400')
root.resizable(width=False, height=False) 
root.title('translater')
root.config(bg='#f5fefd')

#universal variable
py = 10
px = 30
bgc = '#722f37'
foc = 'white'
Button_font = 'Helvetica'
Button_font_size = 12

# add widgets
welcome_label = tk.Label(root, text='LANGUAGE TRANSLATER', bg='#f5fefd', font=('Comic Sans MS', 30))
welcome_label.pack(pady=20)

# creating a frame to arrang my widget to grid layout
frame = tk.Frame(root, bg='#e7decc', width=500, height=100)
frame.pack(padx=10, pady=10, fill='both')

#sourse and target language label
source_label = tk.Label(frame, text='Sourse Language', bg=bgc, fg=foc, font=('Comic Sans MS', 20))
target_label = tk.Label(frame, text='Target Language', bg=bgc, fg=foc, font=('Comic Sans MS', 20))
source_label.grid(row=0, column=0, padx=px, pady=py)
target_label.grid(row=0, column=2, padx=px, pady=py)

#Add combobox
source_cb = ttk.Combobox(frame, values=languages, width=30)
# set the default language
source_cb.current(21)
target_cb = ttk.Combobox(frame, values=languages, width=30)
target_cb.current(38)
source_cb.grid(row=1, column=0, padx=px, pady=py)
target_cb.grid(row=1, column=2, padx=px, pady=py)

#Adding row 2 elements
input_text = tk.Text(frame, width=25, height=5)
translate_button = tk.Button(frame, text='Translate', bg=bgc, fg=foc, font=(Button_font, Button_font_size
 ),command=do_translation)
output_label = tk.Label(frame, text='No Translation Yet', bg=bgc, fg=foc, width=30, height=5)
input_text.grid(row=2, column=0, padx=px, pady=py)
translate_button.grid(row=2, column=1, padx=px, pady=py)
output_label.grid(row=2, column=2, padx=px, pady=py)

#Adding row 3 elements
voice_button = tk.Button(frame, text='Say Something', bg=bgc, fg=foc, font=(Button_font, Button_font_size))
clear_button = tk.Button(frame, text='Clear', bg=bgc, fg=foc, font=(Button_font, Button_font_size))
speak_button = tk.Button(frame, text='Speak Something', bg=bgc, fg=foc, font=(Button_font, Button_font_size))
voice_button.grid(row=3, column=0, padx=px, pady=py)
clear_button.grid(row=3, column=1, padx=px, pady=py)
speak_button.grid(row=3, column=2, padx=px, pady=py)


#for display
root.mainloop()