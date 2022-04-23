from tkinter import *
import googletrans
import textblob
from tkinter import ttk, messagebox

root = Tk()
root.title('Переводчик')
root.geometry('910x300')
root.configure(bg='#C7FFDE')
root.resizable(False, False)
image1 = PhotoImage(file='translate.png')
root.iconphoto(False, image1)
arrow_image = PhotoImage(file='switch.png')
image_label = Label(root, image=arrow_image, width=200, height=80)
image_label.place(x=352, y=135)

def translate_it():
    transl_text.delete(1.0, END)
    try:
        #получаем ключи из словаря языков
        for key, value in languages.items():
            if (value == original_combo.get()):
                from_language_key = key
        for key, value in languages.items():
            if (value == transl_combo.get()):
                to_language_key = key

        words = textblob.TextBlob(original_text.get(1.0, END))
        words = words.translate(from_lang=from_language_key, to=to_language_key)
        transl_text.insert(1.0, words)
    except Exception as e:
        messagebox.showerror('Ошибка', e)

def clear():
    original_text.delete(1.0, END)
    transl_text.delete(1.0, END)

languages = googletrans.LANGUAGES
language_list = list(languages.values())

original_text = Text(root, bg='#FFFFCC', fg='#F2973C', height=10, width=40)
original_text.grid(row=0, column=0, pady=20, padx=10)

tansl_btn = Button(root, text='Перевести!', font=('Helvetica', 24),
                   activebackground='#ECC88A', cursor='hand2', bd=5,
                   bg='#AEECA7', fg='#03521E', command=translate_it)
tansl_btn.grid(row=0, column=1, padx=10)

transl_text = Text(root, bg='#FFFFCC', fg='#F2973C', height=10, width=40)
transl_text.grid(row=0, column=2, pady=20, padx=10)

original_combo = ttk.Combobox(root, width=50, value=language_list)
original_combo.current(77)
original_combo.grid(row=1, column=0)

transl_combo = ttk.Combobox(root, width=50, value=language_list)
transl_combo.current(21)
transl_combo.grid(row=1, column=2)

clear_btn = Button(root, text='Clear', command=clear)
clear_btn.grid(row=2, column=1)

root.mainloop()
