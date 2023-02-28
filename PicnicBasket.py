from tkinter import *
import random 
root = Tk()
root.title("Picnic Basket")
root.geometry("500x500")
label1 = Label(root)
label2 = Label(root)
list1 = ["Bottle", "Snacks", "ID Card", "Chocolates", "Money", "Cards"]
label1["text"] = "Listed Items:" + str(list1)
def bag_contents():
    random_list = random.sample(range(0,6),1)
    label2["text"] = "Item Number " + str(random_list) + " in bag"
    
label1.place(relx = 0.5, rely = 0.4, anchor=CENTER)
label2.place(relx = 0.5, rely = 0.6, anchor = CENTER)
btn = Button(root, text="Which item to put in bag", command = bag_contents)
btn.place(relx = 0.5, rely = 0.5, anchor = CENTER)
root.mainloop()