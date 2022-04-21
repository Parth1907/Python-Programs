from tkinter import *

main=Tk()

e=Entry(main, width=23 , borderwidth=5)
e.grid(row=0,column=0,columnspan=4, padx=10,pady=10)

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current)+str(number))
    
def button_clear():
    e.delete(0, END)
    
def button_add():
    first_number=e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)
    
def button_equal():
    second_number = e.get()
    e.delete(0, END)

    if math=="addition":
        e.insert(0, f_num + int(second_number))
    if math=="subtraction":
        e.insert(0, f_num - int(second_number))
    if math=="multiplication":
        e.insert(0, f_num * int(second_number))
    if math=="division":
        e.insert(0, f_num / int(second_number))
    

def button_subtract():
    first_number=e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)
    
def button_multiply():
    first_number=e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)
    
def button_divide():
    first_number=e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)
    
# Define Buttons
Button1 = Button(main, text="1", padx=20, pady=10, command=lambda: button_click(1))
Button2 = Button(main, text="2", padx=20, pady=10, command=lambda: button_click(2))
Button3 = Button(main, text="3", padx=20, pady=10, command=lambda: button_click(3))
Button4 = Button(main, text="4", padx=20, pady=10, command=lambda: button_click(4))
Button5 = Button(main, text="5", padx=20, pady=10, command=lambda: button_click(5))
Button6 = Button(main, text="6", padx=20, pady=10, command=lambda: button_click(6))
Button7 = Button(main, text="7", padx=20, pady=10, command=lambda: button_click(7))
Button8 = Button(main, text="8", padx=20, pady=10, command=lambda: button_click(8))
Button9 = Button(main, text="9", padx=20, pady=10, command=lambda: button_click(9))
Button0 = Button(main, text="0", padx=20 ,pady=10, command=lambda: button_click(0))

ButtonAdd = Button(main, text="+", padx=20 ,pady=10, command=button_add)
ButtonSubtract = Button(main, text="-", padx=20, pady=10 ,command=button_subtract)
ButtonMultiply = Button(main, text="*", padx=20, pady=10 ,command=button_multiply)
ButtonDivide = Button(main, text="/", padx=20, pady=10, command=button_divide)
ButtonEqual = Button(main, text="=", padx=19, pady=10, command=button_equal)
ButtonClear = Button(main, text="CE", padx=15, pady=10, command=button_clear)

# Placing Buttons
Button1.grid(row=3, column=0)
Button2.grid(row=3, column=1)
Button3.grid(row=3, column=2)

Button4.grid(row=2, column=0)
Button5.grid(row=2, column=1)
Button6.grid(row=2, column=2)

Button7.grid(row=1, column=0)
Button8.grid(row=1, column=1)
Button9.grid(row=1, column=2)

Button0.grid(row=4, column=0)

ButtonAdd.grid(row=1, column=3)
ButtonSubtract.grid(row=2, column=3)
ButtonMultiply.grid(row=3, column=3)
ButtonDivide.grid(row=4, column=3)                      
ButtonEqual.grid(row=4, column=2)
ButtonClear.grid(row=4, column=1)
main.mainloop()
