#let's import the tkinter module to create GUI's
import tkinter

#lets use dir() function to see whats inside the tkinter module
# print(dir(tkinter))

# let's create an empty GUI / root gui
root = tkinter.Tk()

# let's define function
def add():
  print('Adding task to the list')

  # let's get the text written inside entey
  data = entry.get()
  # print(data)
  #let's check first if data is empty or Not
  if data:
    # task_list.insert(0, data)
    task_list.insert(tkinter.END, data)

    #let's clean the entry widget
    entry.delete(0, tkinter.END)

def delete():
  print('Deleting task from the list')

  #let's delete the active element from the list
  task_list.delete(tkinter.ACTIVE)

#let's define the width and heitgh of gui
root.geometry('400x400')
root.resizable(width=False, height=False)

#let's change the title
root.title('To Do List')

# let's add entry widget
entry=tkinter.Entry(root)
entry.pack(padx=10, pady=10, fill='x')

# let's add a button
add_button = tkinter.Button(root, text='Add Task', width=20, bg='red', fg='white', command=add)
add_button.pack()

# let's add the task list
task_list = tkinter.Listbox(root)
task_list.pack(fill='x', padx=20, pady=10)
add_button.pack()

# let's add one more button
delete_button = tkinter.Button(root, text='Delete Task', width=20, command=delete)
delete_button.pack()

# let's call the mainloop function
root.mainloop()
