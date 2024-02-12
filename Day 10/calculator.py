def plus():
    global res
    res = num1 + num2
    
def sub():
    global res
    res = num1 - num2

def mult():
    global res
    res = num1 * num2

def div():
    global res
    res = num1 / num2

def opera():
    if oper == '+':
        plus()
    elif oper == '-':
        sub()
    elif oper == '*':
        mult()
    else:
        div()

num1 = float(input("What's the first number?: "))
oper = input("+\n-\n*\n/\nPick an operator: ")
num2 = float(input("What's the next number?: "))
opera()

while True:
    cont = input(f"Tipe 'y' to continue calculating with {res}, or type 'n' to start a new calculating: ")
    if cont != 'y':
        break
    else:
        num1 = res
        oper = input("Pick an operator: ")
        num2 = float(input("What's the next number?: "))
        opera()
        print(res)
        