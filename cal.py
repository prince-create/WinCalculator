from tkinter import *


root = Tk()
root.title("WinCalculator")
operator=""
text_Input = StringVar()


def btnClick(numbers):
    global operator
    operator += str(numbers)
    text_Input.set(operator)

# function for clear button
def btnClearDisplay():
    global operator
    operator=""
    text_Input.set("")

# function for equals button
def btnEqualsInput():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)

textDisplay = Entry(root, font=('arial', 20, 'bold'), textvariable=text_Input, bd=30, insertwidth=4, bg="powder blue", justify='right')
textDisplay.grid(columnspan=4)

btn7 = Button(root, padx=16, pady=20, bd=8, fg='black', font=('arial', 20, 'bold'), text="7",command=lambda:btnClick(7))
btn7.grid(row=1, column=0)

btn8 = Button(root, padx=16, pady=20, bd=8, fg='black', font=('arial', 20, 'bold'), text="8",command=lambda:btnClick(8))
btn8.grid(row=1, column=1)

btn9 = Button(root, padx=16, pady=20, bd=8, fg='black', font=('arial', 20, 'bold'), text="9",command=lambda:btnClick(9))
btn9.grid(row=1, column=2)

Addition = Button(root, padx=16, pady=20, bd=8, fg='black', font=('arial', 20, 'bold'), text="+" ,command=lambda:btnClick("+"))
Addition.grid(row=1, column=3)

# the second row

btn4 = Button(root, padx=16, pady=20, bd=8, fg='black', font=('arial', 20, 'bold'), text="4",command=lambda:btnClick(4))
btn4.grid(row=2, column=0)

btn5 = Button(root, padx=16, pady=20, bd=8, fg='black', font=('arial', 20, 'bold'), text="5",command=lambda:btnClick(5))
btn5.grid(row=2, column=1)

btn6 = Button(root, padx=16, pady=20, bd=8, fg='black', font=('arial', 20, 'bold'), text="6",command=lambda:btnClick(6))
btn6.grid(row=2, column=2)

Substraction = Button(root, padx=16, pady=20, bd=8, fg='black', font=('arial', 20, 'bold'), text="-" ,command=lambda:btnClick("-"))
Substraction.grid(row=2, column=3)

#  the third row

btn1 = Button(root, padx=16,pady=20, bd=8, fg='black', font=('arial', 20, 'bold'), text="1",command=lambda:btnClick(1))
btn1.grid(row=3, column=0)

btn2 = Button(root, padx=16, pady=20, bd=8, fg='black', font=('arial', 20, 'bold'), text="2",command=lambda:btnClick(2))
btn2.grid(row=3, column=1)

btn3 = Button(root, padx=16,pady=20, bd=8, fg='black', font=('arial', 20, 'bold'), text="3",command=lambda:btnClick(3))
btn3.grid(row=3, column=2)

Multiplication = Button(root, padx=16, pady=20, bd=8, fg='black', font=('arial', 20, 'bold'), text="*",command=lambda:btnClick("*"))
Multiplication.grid(row=3, column=3)

# fourth row

btn0 = Button(root, padx=16,pady=20, bd=8, fg='black', font=('arial', 20, 'bold'), text="0",command=lambda:btnClick(0))
btn0.grid(row=4, column=0)

btnClear = Button(root, padx=16, pady=20, bd=8, fg='black', font=('arial', 20, 'bold'), text="C",command=btnClearDisplay)
btnClear.grid(row=4, column=1)

btnEquals = Button(root, padx=16, pady=20, bd=8, fg='black', font=('arial', 20, 'bold'), text="=",command=btnEqualsInput)
btnEquals.grid(row=4, column=2)

Divide = Button(root, padx=16, pady=20, bd=8, fg='black', font=('arial', 20, 'bold'), text="/" ,command=lambda:btnClick("/"))
Divide.grid(row=4, column=3)


root.mainloop()