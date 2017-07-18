# -*- coding: utf-8 -*-
import string
import random
from Tkinter import *
   
def generate():
    password = ''
    if var1.get() == 1:
        password += string.ascii_lowercase
    if var2.get() == 1:
        password += string.ascii_uppercase
    if var3.get() == 1:
        password += string.digits
    if var4.get() == 1:
        password += string.punctuation
    number_of_letters = menu_var.get()
    result = ''
    if var5.get() == 1:
        result = ''.join(random.sample(password, number_of_letters))
    else:
        for i in range(number_of_letters):
            result += (random.choice(password))
    entry.delete(0, END)
    entry.insert(0, result)

def activate():
    if (var1.get() == 0 and var3.get() == 0 and var4.get() == 0):
        button['state'] = 'disabled'
    else:
        button['state'] = 'normal'
    if (var1.get() == 1):
        check2['state'] = 'normal'
    else:
        check2['state'] = 'disabled'
        check2.deselect()

root=Tk()
root.title('Генератор паролей')
root.geometry('400x150+300+200')
root.resizable(False, False)

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
check1=Checkbutton(root, text='Буквы', variable=var1, onvalue=1, offvalue=0, command = activate)
check2=Checkbutton(root, text='Оба регистра', variable=var2, onvalue=1, offvalue=0, state=DISABLED, command = activate)
check3=Checkbutton(root, text='Цифры', variable=var3, onvalue=1, offvalue=0, command = activate)
check4=Checkbutton(root, text='Символы', variable=var4, onvalue=1, offvalue=0, command = activate)
check5=Checkbutton(root, text='Неповторяющиеся символы', variable=var5, onvalue=1, offvalue=0)
check1.place(x=20, y=20)
check2.place(x=20, y=40)
check3.place(x=120, y=20)
check4.place(x=120, y=40)
check5.place(x=20, y=60)

# Поле
entry=Entry(bd=1)
entry.place(x=25, y=100, width = 150, height = 20)

# Кнопка
button=Button(root, text='Сгенерировать', state=DISABLED, command=generate)
button.place(x=200, y=100, width=120, height=20)

# Меню
label = Label(root, text='Длина пароля:')
label.place(x=210, y=25)
menu_var = IntVar()
length_of_password = [i for i in range(6,21)]
menu_var.set(6)
menu = OptionMenu(root, menu_var, *length_of_password)
menu.place(x=300,y=20)

root.mainloop()

