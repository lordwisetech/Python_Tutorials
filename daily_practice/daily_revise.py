from tkinter import *
def opening_file_with_list():
    lines = [all.strip() for all in open("daily.txt")]
    print(lines)

def writing_into_the_file():
    write = open("write.txt","w")

    print(input("enter your file"),file= write)

    write.close()

window = Tk()

x = IntVar()
def all():
    if(x.get() == 1):
        entry.config(text="you agree")
    else:
        entry.config(text="you dont agree")

entry = Checkbutton(window,font=("Arial",18,"bold"),
              fg="green",
              bg="black",
              text="you dont agree",
                    command=all,
                    variable=x
              )
entry.pack()


window.mainloop()