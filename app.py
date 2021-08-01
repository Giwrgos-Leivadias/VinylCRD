from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from db import Database


db = Database('vinyl.db')

root = Tk()

root.title(" Τα Βινύλια Του Μάνθου")
root.iconbitmap('vinyl.ico')
root.geometry("1100x700")



my_tree = ttk.Treeview(root)

my_tree['columns'] = ("ID","Συνθέτης","Στιχουργός","Ορχήστρα-Εκτέλεσης","Χρονολογία","Εκδότης","Αριθμός Μήτρας","Αριθμός Σειράς")

my_tree.column("#0",width=0, stretch=NO)
my_tree.column("ID", anchor=W,width=30,minwidth=0, stretch=NO)
my_tree.column("Συνθέτης", anchor=W,width=150,minwidth=0, stretch=NO)
my_tree.column("Στιχουργός",anchor=W,width=150,minwidth=0, stretch=NO)
my_tree.column("Ορχήστρα-Εκτέλεσης",anchor=W,width=150,minwidth=0, stretch=NO)
my_tree.column("Χρονολογία",anchor=W,width=150,minwidth=0, stretch=NO)
my_tree.column("Εκδότης",anchor=W,width=150,minwidth=0, stretch=NO)
my_tree.column("Αριθμός Μήτρας",anchor=W,width=100,minwidth=0, stretch=NO)
my_tree.column("Αριθμός Σειράς",anchor=W,width=100,minwidth=0, stretch=NO)

#headings
my_tree.heading("#0", text="",anchor=W)
my_tree.heading("ID",text="ID", anchor=W)
my_tree.heading("Συνθέτης",text="Συνθέτης", anchor=W)
my_tree.heading("Στιχουργός",text="Στιχουργός",anchor=W)
my_tree.heading("Ορχήστρα-Εκτέλεσης",text="Ορχήστρα-Εκτέλεσης",anchor=W)
my_tree.heading("Χρονολογία", text="Χρονολογία",anchor=CENTER)
my_tree.heading("Εκδότης", text="Εκδότης", anchor=W)
my_tree.heading("Αριθμός Μήτρας", text="Αριθμός Μήτρας", anchor=CENTER)
my_tree.heading("Αριθμός Σειράς", text="Αριθμός Σειράς", anchor=CENTER)


#add fake data 
my_tree.pack(pady=20)




form_frame = Frame(root)
form_frame.pack(pady=20)


sinthetis_label = Label(form_frame,font='bold', text="Συνθέτης:")
sinthetis_label.grid(row=0, column=0)

stixourgos_label = Label(form_frame, font='bold',text="Στιχουργός:")
stixourgos_label.grid(row=0,column=2)

orxistra_label = Label(form_frame,font='bold', text="Ορχήστρα-Εκτέλεσης:")
orxistra_label.grid(row=0, column=4)

date_label = Label(form_frame,font='bold', text="Χρονολογία:")
date_label.grid(row=0, column=7)

ekdotis_label = Label(form_frame,font='bold',text="Εκδότης:")
ekdotis_label.grid(row=1, column=0, pady=20,padx=5)

matrix_label = Label(form_frame, font='bold',text="Αριθμός Μήτρας:")
matrix_label.grid(row=1, column=2)

serial_number = Label(form_frame,font='bold',text="Αριθμός Σειράς:")
serial_number.grid(row=1,column=4,padx=5)



sinthetis_entry = Entry(form_frame, width=25)
sinthetis_entry.grid(row=0, column=1,padx=5)

stixourgos_entry = Entry(form_frame,width=25)
stixourgos_entry.grid(row=0, column=3,padx=5)

orxistra_entry = Entry(form_frame,width=25)
orxistra_entry.grid(row=0, column=5,padx=5)

date_entry = Entry(form_frame,width=10)
date_entry.grid(row=0, column=8,padx=5)

ekdotis_entry = Entry(form_frame,width=25)
ekdotis_entry.grid(row=1,column=1,padx=5)

matrix_entry = Entry(form_frame)
matrix_entry.grid(row=1,column=3,padx=5)

serial_number_entry = Entry(form_frame)
serial_number_entry.grid(row=1,column=5,padx=5)

button_frame = Frame(root)
button_frame.pack(pady=20)

def add_vinyl():
    if sinthetis_entry.get()=='' or stixourgos_entry.get()=='' or orxistra_entry.get()=='' or date_entry.get()=='' or ekdotis_entry.get()=='' or matrix_entry.get()=='' or serial_number_entry.get()=='':
        messagebox.showerror('Απαιτούμενα πεδία','ΣΥΜΠΕΡΙΛΑΒΕΤΕ ΟΛΑ ΤΑ ΠΕΔΙΑ')
        return
    db.insert(sinthetis_entry.get(), stixourgos_entry.get(), orxistra_entry.get(),
        date_entry.get(),ekdotis_entry.get(),matrix_entry.get(), serial_number_entry.get())
    clear_text()
    populate_list()



def remove_vinyl():
        try:
            global selected_item
            index = my_tree.selection()[0]
            selected_item = my_tree.item(index)['values']
            sinthetis_entry.delete(0,END)
            sinthetis_entry.insert(END, selected_item[1])
            stixourgos_entry.delete(0,END)
            stixourgos_entry.insert(END, selected_item[2])
            orxistra_entry.delete(0,END)
            orxistra_entry.insert(END, selected_item[3])
            date_entry.delete(0,END)
            date_entry.insert(END,selected_item[4])
            ekdotis_entry.delete(0,END)
            ekdotis_entry.insert(END,selected_item[5])
            matrix_entry.delete(0,END)
            matrix_entry.insert(END,selected_item[6])
            serial_number_entry.delete(0,END)
            serial_number_entry.insert(END,selected_item[7])
        except IndexError:
            pass
        db.remove(selected_item[0])
        clear_text()
        populate_list()


add_btn = Button(button_frame,text="ΠΡΟΣΘΗΚΗ",command=add_vinyl)
add_btn.grid(row=1, column=3)

delete_btn = Button(button_frame, text="ΔΙΑΓΡΑΦΗ ΕΠΙΛΕΓΜΕΝΟΥ",command=remove_vinyl)
delete_btn.grid(row=1,column=4,padx=30)


def clear_text():
    sinthetis_entry.delete(0,END)
    stixourgos_entry.delete(0,END)
    orxistra_entry.delete(0,END)
    date_entry.delete(0,END)
    ekdotis_entry.delete(0,END)
    matrix_entry.delete(0,END)
    serial_number_entry.delete(0,END)

def populate_list(query='select * from vinylia'):
    for i in my_tree.get_children():
        my_tree.delete(i)
    for row in db.fetch(query):
        my_tree.insert('', 'end', values=row)

def exit():
    msb = messagebox.askquestion("ΕΞΟΔΟΣ ΠΡΟΓΡΑΜΜΑΤΟΣ","Είστε βέβαιοι ότι θέλετε να βγείτε από την εφαρμογή;",icon='warning')
    if msb=='yes':
        root.destroy()
    else:
        return

populate_list()
root.protocol("WM_DELETE_WINDOW",exit)
mainloop()
