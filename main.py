import tkinter
from tkinter import *
from tkinter import messagebox


win = Tk()
win.geometry("312x382")
win.title('Calculator')


def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)


def bt_clear():
    global expression
    expression = ""
    input_text.set("")


def bt_equal():
    try:
        global expression
        result = str(eval(expression))
        input_text.set(result)
        expression = ''

    except ZeroDivisionError:
        messagebox.showwarning('Division Error', "Can't divide by zero")
        input_text.set('')
        expression = ""
    except SyntaxError:
        messagebox.showerror('Syntax Error', "Invalid Syntax")
        expression = ""
        input_text.set('')



expression = ""
input_text = StringVar()

input_frame = Frame(win, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black",
                    highlightthickness=2)
input_frame.pack(side=TOP)
input_field = Entry(input_frame, font=('arial', 22), textvariable=input_text, width=50, bg="#eee",
                    bd=0, justify=RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)

btns_frame = Frame(win, width=312, height=380.5, bg="grey")
btns_frame.pack()

# first row
clear = Button(btns_frame, text="C", fg="white", width=32, height=3, bd=0, bg="#192E41", cursor="hand2",
               command=lambda: bt_clear())
divide = Button(btns_frame, text="/",  fg="white", width=10, height=3, bd=0, bg="#192E41", cursor="hand2",
                command=lambda: btn_click("/"))

clear.grid(row=0, column=0, columnspan=3, padx=1, pady=1)
divide.grid(row=0, column=3, padx=1, pady=1)

# second row
seven = Button(btns_frame, text="7", fg="white", width=10, height=3, bd=0, bg="#000", cursor="hand2",
               command=lambda: btn_click(7))
eight = Button(btns_frame, text="8", fg="white", width=10, height=3, bd=0, bg="#000", cursor="hand2",
               command=lambda: btn_click(8))
nine = Button(btns_frame, text="9", fg="white", width=10, height=3, bd=0, bg="#000", cursor="hand2",
              command=lambda: btn_click(9))
multiply = Button(btns_frame, text="*", fg="white", width=10, height=3, bd=0, bg="#192E41", cursor="hand2",
                  command=lambda: btn_click("*"))

seven.grid(row=2, column=0, padx=1, pady=1)
eight.grid(row=2, column=1, padx=1, pady=1)
nine.grid(row=2, column=2, padx=1, pady=1)
multiply.grid(row=2, column=3, padx=1, pady=1)


# third row
four = Button(btns_frame, text="4", fg="white", width=10, height=3, bd=0, bg="#000", cursor="hand2",
              command=lambda: btn_click(4))
five = Button(btns_frame, text="5", fg="white", width=10, height=3, bd=0, bg="#000", cursor="hand2",
              command=lambda: btn_click(5))
six = Button(btns_frame, text="6", fg="white", width=10, height=3, bd=0, bg="#000", cursor="hand2",
             command=lambda: btn_click(6))
minus = Button(btns_frame, text="-", fg="white", width=10, height=3, bd=0, bg="#192E41", cursor="hand2",
               command=lambda: btn_click("-"))

four.grid(row=3, column=0, padx=1, pady=1)
five.grid(row=3, column=1, padx=1, pady=1)
six.grid(row=3, column=2, padx=1, pady=1)
minus.grid(row=3, column=3, padx=1, pady=1)

# fourth row
one = Button(btns_frame, text="1", fg="white", width=10, height=3, bd=0, bg="#000", cursor="hand2",
             command=lambda: btn_click(1))
two = Button(btns_frame, text="2", fg="white", width=10, height=3, bd=0, bg="#000", cursor="hand2",
             command=lambda: btn_click(2))
three = Button(btns_frame, text="3", fg="white", width=10, height=3, bd=0, bg="#000", cursor="hand2",
               command=lambda: btn_click(3))
plus = Button(btns_frame, text="+", fg="white", width=10, height=3, bd=0, bg="#192E41", cursor="hand2",
              command=lambda: btn_click("+"))

one.grid(row=4, column=0, padx=1, pady=1)
two.grid(row=4, column=1, padx=1, pady=1)
three.grid(row=4, column=2, padx=1, pady=1)
plus.grid(row=4, column=3, padx=1, pady=1)

# fifth row
zero = Button(btns_frame, text="0", fg="white", width=21, height=3, bd=0, bg="#000", cursor="hand2",
              command=lambda: btn_click(0))
point = Button(btns_frame, text=".", fg="white", width=10, height=3, bd=0, bg="#000", cursor="hand2",
               command=lambda: btn_click("."))
equals = Button(btns_frame, text="=", fg="white", width=10, height=3, bd=0, bg="#192E41", cursor="hand2",
                command=lambda: bt_equal())

zero.grid(row=5, column=0, columnspan=2, padx=1, pady=1)
point.grid(row=5, column=2, padx=1, pady=1)
equals.grid(row=5, column=3, padx=1, pady=1)


square = Button(btns_frame, text='x^2', fg='white', width=10, height=3, bd=0, bg='#192E41', cursor='hand2',
                command=lambda: btn_click('**2'))
s_root = Button(btns_frame, text='√x', fg='white', width=10, height=3, bd=0, bg="#192E41", cursor='hand2',
                command=lambda: btn_click('**0.5'))
open_bracket = Button(btns_frame, text='(', fg='white', width=10, height=3, bd=0, bg='#192E41', cursor='hand2',
                command=lambda: btn_click('('))
close_bracket = Button(btns_frame, text=')', fg='white', width=10, height=3, bd=0, bg='#192E41', cursor='hand2',
                command=lambda: btn_click(')'))

square.grid(row=1, column=0, padx=1, pady=1, columnspan=1)
s_root.grid(row=1, column=1, pady=1, padx=1)
open_bracket.grid(row=1, column=2, padx=1, pady=1)
close_bracket.grid(row=1, column=3, padx=1, pady=1)

win.mainloop()
