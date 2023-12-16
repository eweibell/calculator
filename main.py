# Imports
from tkinter import *

#Creating variables
root = Tk()
reset = False
skyblue = '#A0D0EA'
yellow = '#EFFF93'
equationbg = '#F1FBEB'
bgcolor = '#EFEFEF'
bgside = yellow
border = 6
equationVariable = ''
buttonFont = ('Helvetica', 18)
equationFont = ('Helvetica', 24)

root.title("Calculator")
root.minsize(425, 450)
root.maxsize(425, 450)
root.config(bg="skyblue")

Grid.rowconfigure(root, 0, weight=1)
Grid.rowconfigure(root, 1, weight=1)
Grid.columnconfigure(root, 0, weight=1)

# ---- Equation Bar

# Creating Equation Bar Frame
equation_bar = Frame(root, width=425, height=50, bg=skyblue)
equation_bar.grid(row=0, column=0, padx=0, pady=0, sticky="NSEW")

#Equation Bar Config
equation_bar.columnconfigure(0, weight=1)
equation_bar.rowconfigure(0, weight=1, pad=0)
equation_bar.rowconfigure(1, weight=1, pad=0)

#Equation Label Creation/Config
equation = Label(equation_bar, text=equationVariable, bg=equationbg, font=equationFont)
equation.grid(row=1, column=0, pady=10, padx=8, sticky="NSEW")

# ---- NumPad

#Creating NumPad Frame
num_pad = Frame(root, width=425, height=400, bg=skyblue)
num_pad.grid(row=1, column=0, padx=0, pady=0, sticky="NSEW")

#NumPad Config
num_pad.columnconfigure((0, 1, 2, 3), uniform="equal", weight=1)
num_pad.rowconfigure((1, 2, 3, 4), uniform="equal", weight=1)

#All Button Functions
def one():
    global reset
    global equationVariable
    if not reset:
        addToEquationVariable(1)
    else:
        equationVariable = str('')
        addToEquationVariable(1)
        reset = False
def two():
    global reset
    global equationVariable
    if not reset:
        addToEquationVariable(2)
    else:
        equationVariable = str('')
        addToEquationVariable(2)
        reset = False
def three():
    global reset
    global equationVariable
    if not reset:
        addToEquationVariable(3)
    else:
        equationVariable = str('')
        addToEquationVariable(3)
        reset = False
def four():
    global reset
    global equationVariable
    if not reset:
        addToEquationVariable(4)
    else:
        equationVariable = str('')
        addToEquationVariable(4)
        reset = False
def five():
    global reset
    global equationVariable
    if not reset:
        addToEquationVariable(5)
    else:
        equationVariable = str('')
        addToEquationVariable(5)
        reset = False
def six():
    global reset
    global equationVariable
    if not reset:
        addToEquationVariable(6)
    else:
        equationVariable = str('')
        addToEquationVariable(6)
        reset = False
def seven():
    global reset
    global equationVariable
    if not reset:
        addToEquationVariable(7)
    else:
        equationVariable = str('')
        addToEquationVariable(7)
        reset = False
def eight():
    global reset
    global equationVariable
    if not reset:
        addToEquationVariable(8)
    else:
        equationVariable = str('')
        addToEquationVariable(8)
        reset = False
def nine():
    global reset
    global equationVariable
    if not reset:
        addToEquationVariable(9)
    else:
        equationVariable = str('')
        addToEquationVariable(9)
        reset = False
def zero():
    global reset
    global equationVariable
    if not reset:
        addToEquationVariable(0)
    else:
        equationVariable = str('')
        addToEquationVariable(0)
        reset = False
def add():
    global reset
    global equationVariable
    if not reset:
        addToEquationVariable('+')
    else:
        return
def sub():
    global reset
    global equationVariable
    if not reset:
        addToEquationVariable('-')
    else:
        return
def multi():
    global reset
    global equationVariable
    if not reset:
        addToEquationVariable('*')
    else:
        return
def div():
    global reset
    global equationVariable
    if not reset:
        addToEquationVariable('/')
    else:
        return
def clear():
    global reset
    global equationVariable
    equationVariable = ''
    refreshEquation()
    reset = False
def equal():
    global reset
    if not reset:
        calculateAnswer()
    else:
        return

#Creating and config buttons
def NumPadButtons():
    one_button = Button(num_pad, text="1", command=one, bg=bgcolor, font=buttonFont)
    one_button.grid(row=1, column=0, pady=border, padx=border, sticky="NSEW")

    two_button = Button(num_pad, text="2", command=two, bg=bgcolor, font=buttonFont)
    two_button.grid(row=1, column=1, pady=border, padx=border, sticky="NSEW")

    three_button = Button(num_pad, text="3", command=three, bg=bgcolor, font=buttonFont)
    three_button.grid(row=1, column=2, pady=border, padx=border, sticky="NSEW")

    add_button = Button(num_pad, text="+", command=add, bg=bgside, font=buttonFont)
    add_button.grid(row=1, column=3, pady=border, padx=border, sticky="NSEW")

    four_button = Button(num_pad, text="4", command=four, bg=bgcolor, font=buttonFont)
    four_button.grid(row=2, column=0, pady=border, padx=border, sticky="NSEW")

    five_button = Button(num_pad, text="5", command=five, bg=bgcolor, font=buttonFont)
    five_button.grid(row=2, column=1, pady=border, padx=border, sticky="NSEW")

    six_button = Button(num_pad, text="6", command=six, bg=bgcolor, font=buttonFont)
    six_button.grid(row=2, column=2, pady=border, padx=border, sticky="NSEW")

    sub_button = Button(num_pad, text="-", command=sub, bg=bgside, font=buttonFont)
    sub_button.grid(row=2, column=3, pady=border, padx=border, sticky="NSEW")

    seven_button = Button(num_pad, text="7", command=seven, bg=bgcolor, font=buttonFont)
    seven_button.grid(row=3, column=0, pady=border, padx=border, sticky="NSEW")

    eight_button = Button(num_pad, text="8", command=eight, bg=bgcolor, font=buttonFont)
    eight_button.grid(row=3, column=1, pady=border, padx=border, sticky="NSEW")

    nine_button = Button(num_pad, text="9", command=nine, bg=bgcolor, font=buttonFont)
    nine_button.grid(row=3, column=2, pady=border, padx=border, sticky="NSEW")

    multi_button = Button(num_pad, text="*", command=multi, bg=bgside, font=buttonFont)
    multi_button.grid(row=3, column=3, pady=border, padx=border, sticky="NSEW")

    c_button = Button(num_pad, text="C", command=clear, bg='#FD9FA9', font=buttonFont)
    c_button.grid(row=4, column=0, pady=border, padx=border, sticky="NSEW")

    zero_button = Button(num_pad, text="0", command=zero, bg=bgcolor, font=buttonFont)
    zero_button.grid(row=4, column=1, pady=border, padx=border, sticky="NSEW")

    equal_button = Button(num_pad, text="=", command=equal, bg=bgcolor, font=buttonFont)
    equal_button.grid(row=4, column=2, pady=border, padx=border, sticky="NSEW")

    div_button = Button(num_pad, text="/", command=div, bg=bgside, font=buttonFont)
    div_button.grid(row=4, column=3, pady=border, padx=border, sticky="NSEW")

#Button functionality functions
def addToEquationVariable(x):
    global equationVariable
    equationVariable += str(x)
    refreshEquation()
def refreshEquation():
    equation.config(text=equationVariable)
def calculateAnswer():
    global equationVariable
    global reset
    try:
        result = eval(equationVariable)
        equationVariable += str(' = ') + str(result)
    except:
        equationVariable = str('Error')
    refreshEquation()
    reset = True

#Call a function to create buttons
NumPadButtons()

root.mainloop()