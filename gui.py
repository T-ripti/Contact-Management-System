import main
from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("800x720")
root.title("Contact Management")
root.configure(bg='#f0f4f7')  # Light greyish-blue background

# Frame for display (treeview and scrollbar)
display_frame = Frame(root, bg='#ffffff', bd=2, relief=SOLID)  # White background for contrast
display_frame.place(x=10, y=10, width=780, height=500)

style = ttk.Style()
style.theme_use("clam")

style.configure("Treeview",
                background="#f7fbfc",
                foreground="black",
                rowheight=25,
                fieldbackground="#f7fbfc",
                font=('Helvetica', 10))
style.configure("Treeview.Heading",
                background="#004aad", 
                foreground="white",
                font=("Helvetica", 12, "bold"))

treev = ttk.Treeview(display_frame, height=25)
treev.pack(side=LEFT, fill=BOTH, expand=True)

verscrlbar = ttk.Scrollbar(display_frame, orient="vertical", command=treev.yview)
verscrlbar.pack(side=RIGHT, fill=Y)
treev.configure(yscrollcommand=verscrlbar.set)

treev["columns"] = ("1", "2", "3", "4")
treev['show'] = 'headings'

treev.column("1", width=100, anchor='c')
treev.column("2", width=200, anchor='c')
treev.column("3", width=200, anchor='c')
treev.column("4", width=200, anchor='c')

treev.heading("1", text="Sl. No.")
treev.heading("2", text="First Name")
treev.heading("3", text="Last Name")
treev.heading("4", text="Phone Number")

treev.tag_configure('oddrow', background='#e9f5fb')  # Light blue row
treev.tag_configure('evenrow', background='#f7fbfc')  # Even lighter blue row

# Frame for add/update/delete
input_frame = Frame(root, bg='#e1ecf4', bd=2, relief=SOLID)  # Light greyish-blue background
input_frame.place(relx=0.5, rely=1.0, anchor=S, width=780, height=180)

def add_one(First, Last, Number):
    main.add_one(First, Last, Number)
    show()

def update(id, First, Last, Number):
    main.update(id, First, Last, Number)
    show()

def delete(id):
    main.delete(id)
    show()

id_label = Label(input_frame, text="ROW ID:", bg='#e1ecf4', font=('Helvetica', 10))
id_label.grid(row=0, column=0, padx=5, pady=10, sticky=W)
id_entry = Entry(input_frame, width=7, font=('Helvetica', 10))
id_entry.grid(row=0, column=1, padx=5, pady=10, sticky=W)

first_label = Label(input_frame, text="FIRST NAME:", bg='#e1ecf4', font=('Helvetica', 10))
first_label.grid(row=0, column=2, padx=5, pady=10, sticky=W)
first_entry = Entry(input_frame, width=15, font=('Helvetica', 10))
first_entry.grid(row=0, column=3, padx=5, pady=10, sticky=W)

last_label = Label(input_frame, text="LAST NAME:", bg='#e1ecf4', font=('Helvetica', 10))
last_label.grid(row=0, column=4, padx=5, pady=10, sticky=W)
last_entry = Entry(input_frame, width=15, font=('Helvetica', 10))
last_entry.grid(row=0, column=5, padx=5, pady=10, sticky=W)

number_label = Label(input_frame, text="PHONE:", bg='#e1ecf4', font=('Helvetica', 10))
number_label.grid(row=0, column=6, padx=5, pady=10, sticky=W)
number_entry = Entry(input_frame, width=15, font=('Helvetica', 10))
number_entry.grid(row=0, column=7 ,padx=5, pady=10, sticky=W)

create_button = Button(input_frame, text="Create", bg='#004aad', fg='white', font=('Helvetica', 13), command=lambda: add_one(first_entry.get(), last_entry.get(), number_entry.get()))
create_button.grid(row=1, column=2, padx=10, pady=13)

update_button = Button(input_frame, text="Update", bg='#007bff', fg='white', font=('Helvetica', 13), command=lambda: update(id_entry.get(), first_entry.get(), last_entry.get(), number_entry.get()))
update_button.grid(row=1, column=4, padx=10, pady=13)

delete_button = Button(input_frame, text="Delete", bg='#dc3545', fg='white', font=('Helvetica', 13), command=lambda: delete(id_entry.get()))
delete_button.grid(row=1, column=6, padx=10, pady=13)

def show():
    global treev
    try:
        treev.delete(*treev.get_children())
    except:
        pass
    for i in main.show_all():
        if i[0] % 2 == 0:
            treev.insert("", 'end', values=(i[0], i[1], i[2], i[3]), tags=('evenrow',))
        else:
            treev.insert("", 'end', values=(i[0], i[1], i[2], i[3]), tags=('oddrow',))

show()
root.mainloop()
