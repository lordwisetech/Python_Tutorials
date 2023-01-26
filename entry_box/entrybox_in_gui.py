from tkinter import *
window = Tk()

notice = Label(window,text="ENTER YOUR USERNAME",font=("Arial",10),fg="green")
notice.pack(side=TOP)

entry = Entry(window,font=("Arial",20,"bold"))
entry.pack(side=LEFT)
entry.config(show="*")

def submit():
    global notice
    username = entry.get()
    notice.config(text="hello "+ username)


    pass
submit_btn = Button(window,
                text="SUBMIT",
                font=("Arial",
                      10,"bold"),
                fg="purple",
                bg="green",
                command=submit)

submit_btn.pack(side=RIGHT)
def delete():
    entry.delete(0,END)

delete_btn = Button(window,
                text="delete all",
                font=("Arial",
                      10,"bold"),
                fg="red",
                bg="green",
                command=delete)
delete_btn.pack()

def backspace():
    entry.delete(len(entry.get())-1,END)

backspace_btn = Button(window,
                text="backspace",
                font=("Arial",
                      10,"bold"),
                fg="red",
                bg="green",
                command=backspace)
backspace_btn.pack()



window.mainloop()