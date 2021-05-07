import pickle
import tkinter
from tkinter import *
from tkinter import filedialog
from tkinter.font import Font
import pickle
root = Tk()
root.title('Elvis Nunez- ToDo List')
root.geometry("800x500")

root.configure(background='white')
#Defining the Font
the_font = Font(
    family = "Californian FB",
    size = 25,
    weight="bold")

#Creating the frame
the_frame = Frame(root)
the_frame.pack(pady=12)
#Created listbox

the_list = Listbox(the_frame,
    font=the_font,
    width=26,
    height = 6,
    bg="white",
    bd=0,
    fg = "#131a10",
    highlightthickness=0,
    selectbackground="#d4bcd9",
    activestyle = "none")

the_list.pack(side=LEFT,fil=BOTH)



#Create scrollbar
scrollbar =Scrollbar(the_frame)
scrollbar.pack(side=RIGHT,fill=BOTH)

#Add scrollbar

the_list.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=the_list.yview())

#create entry box to add item

the_entry = Entry(root, font=("Viner Hand ITC Regular", 24), width = 23)
the_entry.pack(pady=15)


#Create a button frame
button_frame = Frame(root)
button_frame.pack(pady = 15)



#FUNCTIONS
def delete_item():
    #delete what we highligh
    the_list.delete(ANCHOR)
def add_item():
    the_list.insert(END,the_entry.get())
    the_entry.delete(0,END)

def cross_off_item():
    #cross off item
    the_list.itemconfig(
    the_list.curselection(),
    fg="#eee6f0")

    #get rif of selection bar
    the_list.selection_clear(0,END)

def uncross_item():
    # cross off item
    the_list.itemconfig(
        the_list.curselection(),
        fg="#131a10")

    # get rif of selection bar
    the_list.selection_clear(0, END)

#create a delete function
def delete_crossed():
    #counting variable to count size of the item
    counting = 0
    #size function return number of item in the list
    while counting < the_list.size():
        #function itemcget allow to get information about the item
        if the_list.itemcget(counting, "fg") == "#eee6f0":
            #delete item with the index number
            the_list.delete(the_list.index(counting))
        else:
            counting += 1

#create save file function
def guardar_lista ():
    #asksaveasfilename is a function to save the file
    fileNombre = filedialog.asksaveasfilename(
        #where to save the file, try to save the file in your local directory
        initialdir ="C:/Users/Elvis/PycharmProjects/Aprendiendo/data",

        title = "Save the file",
        #What files type to look for
        filetypes=(("Dat files", "*.dat"),("All files", "*.*"))
    )

    if fileNombre:
        #verify if the file have a .dat at the end of the name file
        if fileNombre.endswith(".dat"):
            pass
        #if it does not have a .dot, we put the .dat
        else:
            fileNombre = f'{fileNombre}.dat'
            # counting variable to count size of the item

        #Delete all the corss item before saving the file to avoid bugs
        counting = 0
        # size function return number of item in the list
        while counting < the_list.size():
            # function itemcget allow to get information about the item
            if the_list.itemcget(counting, "fg") == "#eee6f0":
                # delete item with the index number
                the_list.delete(the_list.index(counting))
            else:
                counting += 1

        #get all the items from the list
        cosas = the_list.get(0,END)



        #Open file
        #wb is write to binary
        oFile =open(fileNombre,'wb')

        #use class pickle and function dump to add the items to the file

        pickle.dump(cosas,oFile)


def abrir_lista ():

   fileNombre = filedialog.askopenfilename(
       # where to save the file
       initialdir = "C:/Users/Elvis/PycharmProjects/Aprendiendo/data",

       title = "Open the file",
       # What files type to look for
       filetypes=(("Dat files", "*.dat"), ("All files", "*.*"))
        )
   if fileNombre:
    #Delete current list is there is one
    the_list.delete(0,END)
    #rb is for reading binary
    openFile = open(fileNombre, 'rb')

    #loading the data from file
    cosa = pickle.load(openFile)

    #Output the list to the screen

    for item in cosa:
        the_list.insert(END,item)


def limpiar_lista ():
    the_list.delete(0,END)


#Creating menu

#variables for create the menu to save the to do list
top_menu = Menu(root)
root.config(menu = top_menu)

#creating the file menu
fMenu = Menu(top_menu,tearoff = False)
top_menu.add_cascade(label = "File", menu =fMenu)

fMenu.add_command(label = "Save the List", command = guardar_lista)
fMenu.add_separator()
fMenu.add_command(label = "Open the List", command = abrir_lista)
fMenu.add_separator()
fMenu.add_command(label = "Clear the List", command = limpiar_lista)







#Add some buttons
delete_button = Button(button_frame, text = " Delete Item", command = delete_item, bg = 'red')
add_button = Button(button_frame, text = " Add Item", command = add_item, bg = 'red')
cross_off_button = Button(button_frame, text = " Cross Of Item", command = cross_off_item, bg = 'red')
uncross_button = Button(button_frame, text = " Uncross Item", command = uncross_item, bg = 'red')
delete_cross_button = Button(button_frame, text =" Delete Crossed", command = delete_crossed, bg='red')

delete_button.grid(row = 0,column = 0)
add_button.grid(row = 0,column = 1, padx = 18)
cross_off_button.grid(row=0,column = 2)
uncross_button.grid(row = 0,column = 3, padx = 18)
delete_cross_button.grid(row = 0, column = 4)

root.mainloop()

