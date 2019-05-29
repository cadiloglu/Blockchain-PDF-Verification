import hashlib
from tkinter import *
import tkinter.filedialog
from tkinter import ttk
from tkinter import messagebox


window = Tk()

window.wm_minsize(200, 350)
window.title("Blokchain Database Verification Program Demo (Version 1.0.12)")
window.iconbitmap('icon.ico')

def check_pdf(name, pdf_path):
    ledgerFile = open("/Users/cankat/Desktop/chain-ledger.txt", "r+")

    ledgerStr = ledgerFile.readlines()
    ledgerFile.close()

    allHashes = []

    pdf = open(pdf_path, 'rb')
    hashedPdf = hashlib.sha256()
    hashedPdf.update(name.encode('utf-8'))
    hashedPdf.update(pdf.read())
    searchingHash = hashedPdf.hexdigest()

    print(name.encode('utf-8'))
    print(str(searchingHash))


    if not len(ledgerStr) == 0:
        for i in range(0, len(ledgerStr)):
            if ledgerStr[i].startswith("Block Data:"):
                allHashes.append(ledgerStr[i].split("Block Data: ", 1)[1])
    searchingHash = str(searchingHash).rstrip()
    for hash in allHashes:
        print("hash:   " + hash)
        print("search: " + searchingHash)
        if searchingHash == hash.rstrip():
            return True

    return False


def print_path():
    f = tkinter.filedialog.askopenfilename(
        parent=window, initialdir='C:/Desktop',
        title='Choose file',
        filetypes=[('PDF files', '.pdf'),
                   ('png images', '.png'),
                   ('jpeg images', '.jpeg')]
    )
    list1.insert(END, f)
    # print(f)


def send_button():

    name = str(name_text.get()) + str(surname_text.get())
    pdf_path = list1.get(END)

    if check_pdf(name, pdf_path):
        messagebox.showinfo("Verification Information", "PDF File is Verified.")
    else:
        messagebox.showinfo("Verification Information", "PDF File Could Not Be Verified.")

    name_text.set("")
    surname_text.set("")
    list1.delete(0, 'end')




#define Labels
header = Label(window, text="HOSPITAL RECORD \nVERIFICATION SYSTEM", font=("arial", 20, "bold"), fg="steelblue", anchor=CENTER)
header.grid(row=0, column=0)

l1 = Label(window, text='Name')
l1.grid(row=1, column=0)
l1.grid_anchor(anchor=W)

l1 = Label(window, text='Surname', anchor=E)
l1.grid(row=2, column=0)

l1 = Label(window, text='')
l1.grid(row=4, column=0)

l1 = Label(window, text='')
l1.grid(row=6, column=0)

#define Entries
name_text = StringVar()
e1 = Entry(window, textvariable=name_text)
e1.grid_anchor(anchor=W)
e1.grid(row=1, column=1)

surname_text = StringVar()
e2 = Entry(window, textvariable=surname_text)
e2.grid(row=2, column=1)


#define Button
b1 = ttk.Button(window, text="SEND", command=send_button)
b1.grid(row=9, column=0, columnspan=2)

b2 = ttk.Button(window, text="Upload File")
b2.grid(row=8, column=0, columnspan=2)
b2.config(command=print_path)

#define List
list1 = Listbox(window, height=5, width=45)
list1.grid(row=7, column=0)


window.mainloop()


