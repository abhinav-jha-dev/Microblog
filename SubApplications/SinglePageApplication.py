import tkinter as tk
import random
# Connection MongoDb to manage todo list
import pymongo
from pymongo import MongoClient

# Setting up mongodb
client = MongoClient("mongodb+srv://abhinav:abhi123@smsclustor-zndnc.mongodb.net/")
db = client.get_database("MyToDo")
collection= db.get_collection("MyToDoCollection")

# create root window
root = tk.Tk()
root.configure(bg='white')
root.title("My todo list application")
root.geometry("250x500")

# create const and variable
tasks = []

# create functions

def updateLabel(message):
    lbl_display.config(text=message)

def validateUnique(task_name):
    tasks= collection.find()
    for task in tasks:
        if task['Title'].lower().strip() == task_name.lower().strip():
            return False
    return True

def update_task():
    lb_tasks.delete(0,'end')
    tasks=collection.find()
    for task in tasks:
        lb_tasks.insert("end",task['Title'])

def add_task():
    if (txt_input.get() != "" and validateUnique(txt_input.get())):
        task = { "Title" : txt_input.get()}
        collection.insert_one(task)
        txt_input.delete(0,'end')
        update_task()
        updateLabel('') 
    else:
        updateLabel('Please add valid task name.') 

def delete_task():
    cursorInfo=lb_tasks.curselection()
    if cursorInfo != ():
        taskName = lb_tasks.get(cursorInfo)
        tasks=collection.find()
        for task in tasks:
            if task['Title'] == taskName:
                collection.delete_one({'_id': task['_id']})
                update_task()
                updateLabel('')
    else:
        updateLabel('Please select a task.')
    
def delete_all():
    collection.delete_many({})
    lb_tasks.delete(0,'end')

def sort_asc():
    tasks= list(lb_tasks.get(0,'end'))
    tasks.sort(key=str.lower)
    lb_tasks.delete(0,'end')
    for task in tasks:
        lb_tasks.insert("end",task)

def sort_dec():
    tasks= list(lb_tasks.get(0,'end'))
    tasks.sort(key=str.lower,reverse=True)
    lb_tasks.delete(0,'end')
    for task in tasks:
        lb_tasks.insert("end",task)

def choose_rand():
    tasks= list(lb_tasks.get(0,'end'))
    updateLabel(random.choice(tasks))

def show_number_of_tasks():
    tasks= list(lb_tasks.get(0,'end'))
    updateLabel(len(tasks))


# create UI Elements
lbl_title= tk.Label(root,text='My To-do List', bg='white')
lbl_title.pack()
lbl_display= tk.Label(root,text='', bg='white')
lbl_display.pack()

txt_input= tk.Entry(root,width=35)
txt_input.pack()

btn_add_task = tk.Button(root,text='Add Task', fg='green', bg='white', command=add_task)
btn_add_task.pack()

btn_delete_task = tk.Button(root,text='Delete Task', fg='green', bg='white', command=delete_task)
btn_delete_task.pack()

btn_delete_all = tk.Button(root,text='Delete All', fg='green', bg='white', command=delete_all)
btn_delete_all.pack()

btn_sort_asc = tk.Button(root,text='Sort Accending', fg='green', bg='white', command=sort_asc)
btn_sort_asc.pack()

btn_sort_dec = tk.Button(root,text='Sort Descending', fg='green', bg='white', command=sort_dec)
btn_sort_dec.pack()

btn_choose_rand = tk.Button(root,text='Choose Random', fg='green', bg='white', command=choose_rand)
btn_choose_rand.pack()

btn_number_of_tasks = tk.Button(root,text='Number Of Tasks', fg='green', bg='white', command=show_number_of_tasks)
btn_number_of_tasks.pack()

btn_exit = tk.Button(root,text='Exit', fg='green', bg='white', command=exit)
btn_exit.pack()

lb_tasks= tk.Listbox(root, width=100)
lb_tasks.pack()

update_task()
# start the main event loop
root.mainloop()