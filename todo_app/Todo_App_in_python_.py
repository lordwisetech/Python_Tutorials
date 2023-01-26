from  tkinter import *
window = Tk()
def add_it():
   list_box.insert(list_box.size(),entry_task.get())
def delete():
    list_box.delete(list_box.curselection())
    pass

## header label
header = Label(window,text="TO-DO-LIST-APP",font=("Arial",20,"bold"),fg="green",bg="orange",width=60,bd=5)
header.pack(side=TOP)

addlabel = Label(window,text="CREAT TASK HERE",font=("Arial",20),fg="green",bg='orange')
addlabel.place(x=75, y=54)

tasklabel = Label(window,text="TASKS",font=("Arial",20),fg="green",bg='orange',width=9)
tasklabel.place(x=810, y=54)

## entry (input)
entry_task = Entry(window,font=("Arial",20),fg="green")
entry_task.place(x=54,y=130)

## add button and delete button
add = Button(window,text="ADD",font=("Arial",15,"bold"),fg="green",bg="orange",width=12,command=add_it)
add.place(x=100,y=200)

delete = Button(window,text="DELETE",font=("Arial",15,"bold"),fg="green",bg="orange",width=12,command=delete)
delete.place(x=100,y=250)

## listbox
list_box = Listbox(window,fg="green",bg="black",font=("Constantia",20),width=25)

list_box.place(x=600, y= 100)
list_box.config(height=list_box.size())


## image file
icon = PhotoImage(file="lordwisetech.png")
window.iconphoto(True,icon)

## window
window.config(background="black")
window.title("TODO APP IN PYTHON")
window.geometry("1000x400")
window.mainloop()