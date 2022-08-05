from tkinter import*
import random

root=Tk()
root.title("Number List")
root.geometry("400x400")

random_number_list = Label(root)
random_sorted_number_list = Label(root)

def numberlist():
    random_numbers = random.sample(range(10,30),5)
    random_number_list['text'] = "Random List is " + str(random_numbers)
    random_numbers.sort()
    random_sorted_number_list['text'] = "Sorted List is " + str(random_numbers)
    
btn = Button(text="Create Random Number List", command=numberlist)
btn.place(relx=0.5, rely=0.4, anchor=CENTER)

random_number_list.place(relx=0.5, rely=0.5, anchor=CENTER)
random_sorted_number_list.place(relx=0.5, rely=0.6, anchor=CENTER)

root.mainloop()