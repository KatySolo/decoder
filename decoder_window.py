
from Tkinter import Tk, Button,Entry,Label

root = Tk()

label_input_text_dir = Label(root,text="'input.txt' directory",font = "arial 15")
label_input_basic_dir = Label(root,text="Basic words directory", font = 'arial 15')
entry_input_text = Entry(root,width=50)
entry_input_basic_words = Entry(root, width=50)
miracle_label = Label(root)

def show_all_data():
    print "Clicked"

buttonOK = Button(root,text='OK',width=10,height=2,bg='white',command='show_all_data')

miracle_label.grid(row=0,column=0,columnspan=3)
label_input_text_dir.grid(row=1,column=0)
entry_input_text.grid(row=1,column=1)
label_input_basic_dir.grid(row=2,column=0)
entry_input_basic_words.grid(row=2,column=1)
buttonOK.grid(row=3,column=3)
root.mainloop()

entry_input_basic_words.get()
entry_input_text.get()