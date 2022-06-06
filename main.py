import keyboard as kb
import random as rd
import math
print("Program started! Press ctrl+c to exit.")
print("Show command: " + "help")

def sin(a):
    return math.sin(round(int(a)))

def cos(a):
     return math.cos(round(int(a)))
 
def tan(a):
    return math.tan(round(int(a)))
 
def asin(a):
     return math.asin(round(int(a)))
 
def acos(a):
     return math.acos(round(int(a)))
 
def atan(a):
     return math.atan(round(int(a)))
 
def add(a, b):
     return int(a) + int(b)
 
def minus(a, b):
     return int(a) - int(b)
 
def mult(a, b):
     return int(a) * int(b)
 

def div(a, b):
    return int(a) / int(b)



def mod(a, b):
    return int(a) % int(b)



def sqrt(a):
    return math.sqrt(int(a))


def exp(a, b):
    return int(a) ** int(b)



def sqr(a):
    return int(a) * 2


def cube(a):
    return int(a) ** 3


def cubeRoot(a):
    return a ** (1 / 3)


def ceil(a):
    return int(a) // 1 + 1


def pi():
    return math.pi


def e():
    return math.e


def rnd(a):
    return int(a) // 1 + 0.5

def degrees(a):
    return math.degrees(int(a))


def radians(a):
    return math.radians(int(a))


def sinh(a):
    return math.sinh(int(a))


def cosh(a):
    return math.cosh(int(a))


def tanh(a):
    return math.tanh(int(a))


def factorial(a):
    return math.factorial(int(a))

def isnan(a):
    return math.isnan(int(a))

def hypot(a, b):
    return math.hypot(int(a), int(b))

def binary(a):
    return bin(int(a))


def octal(a):
    return oct(int(a))


def hexadecimal(a):
    return hex(int(a))

def fibonacci(a):
    if a == 0:
        return 0
    elif a == 1:
        return 1
    else:
        return fibonacci(a - 1) + fibonacci(a - 2)

def isfinite(a):
    return math.isfinite(int(a))


def isinfinite(a):
    return math.isinf(int(a))


def isint(a):
    return int(a) // 1 == int(a)


def log(a, b):
    return int(a) * math.log(int(b))



def fx(a):
    return int(a) * math.e



def inv(a):
    return 1 / int(a)



def root(a, b):
 return int(a) ** (1 / int(b))



def random(a, b):
    return rd.randint(int(a), int(b))

while True:
    cmd = input(">>>  ")
    if cmd == "sin":
     a = input("Enter number: ")
     print(sin(a))
    elif cmd == "cos":
        a = input("Enter number: ")
        print(cos(a))
    elif cmd == "tan":
     a = input("Enter number: ")
     print(tan(a))
    elif cmd == "asin":
     a = input("Enter number: ")
     print(asin(a))
    elif cmd == "acos":
     a = input("Enter number: ")
     print(acos(a))
    elif cmd == "atan":
     a = input("Enter number: ")
     print(atan(a))
    elif cmd == "add":
     a = input("Enter number: ")
     b = input("Enter number: ")
     print(add(a, b))
    elif cmd == "minus":
     a = input("Enter number: ")
     b = input("Enter number: ")
     print(minus(a , b))
    elif cmd == "mult":
     a = input("Enter number: ")
     b = input("Enter number: ")
     print(mult(a, b))
    elif cmd == "div":
     a = input("Enter number: ")
     b = input("Enter number: ")
     print(div(a, b))
    elif cmd == "mod":
     a = input("Enter number: ")
     b = input("Enter number: ")
     print(mod(a, b))
    elif cmd == "sqrt":
     a = input("Enter number: ")
     print(sqrt(a))
    elif cmd == "exp":
     a = input("Enter number: ")
     b = input("Enter number: ")
     print(exp(a, b))
    elif cmd == "sqr":
     a = input("Enter number: ")
     print(sqr(a))
    elif cmd == "ceil":
     a = input("Enter number: ")
     print(ceil(a))
    elif cmd == "rnd":
     a = input("Enter number: ")
     print(rnd(a))
    elif cmd == "log":
     a = input("Enter number: ")
     b = input("Enter number: ")
     print(log(a,b))
    elif cmd == "fx":
     a = input("Enter number: ")
     print(fx(int(a)))
    elif cmd == "inv":
     a = input("Enter number: ")
     print(inv(a))
    elif cmd == "root":
     a = input("Enter number: ")
     b = input("Enter number: ")
     print(root(a,b))
    elif cmd == "cube":
        a = input("Enter number: ")
        print(cube(a))
    elif cmd == "cubeRoot":
        a = input("Enter number: ")
        print(cubeRoot(float(a)))
    elif cmd == "pi":
        print(pi())
    elif cmd == "e":
        print(e())
    elif cmd == "degrees":
        a = input("Enter number: ")
        print(degrees(a))
    elif cmd == "radians":
        a = input("Enter number: ")
        print(radians(a))
    elif cmd == "sinh":
        a = input("Enter number: ")
        print(sinh(a))
    elif cmd == "cosh":
        a = input("Enter number: ")
        print(cosh(a))
    elif cmd == "tanh":
        a = input("Enter number: ")
        print(tanh(a))
    elif cmd == "factorial":
        a = input("Enter number: ")
        print(factorial(a))
    elif cmd == "isnan":
        a = input("Enter number: ")
        print(isnan(a))
    elif cmd == "hypot":
        a = input("Enter number: ")
        b = input("Enter number: ")
        print(hypot(a,b))
    elif cmd == "binary":
        a = input("Enter number: ")
        print(binary(a))
    elif cmd == "octal":
        a = input("Enter number: ")
        print(octal(a))
    elif cmd == "hex":
        a = input("Enter number: ")
        print(hexadecimal(a))
    elif cmd == "fibonacci":
        a = input("Enter number: ")
        print(fibonacci(int(a)))
    elif cmd == "isfinite":
        a = input("Enter number: ")
        print(isfinite(a))
    elif cmd == "isinfinite":
        a = input("Enter number: ")
        print(isinfinite(a))
    elif cmd == "isint":
        a = input("Enter number: ")
        print(isint(a))
    elif cmd == "israndom":
        a = input("the number is between: ")
        b = input("and: ")
        print(random(a,b))
    elif cmd == "help":
        print("sinus: sin")
        print("cosinus: cos")
        print("tangens: tan")
        print("arcsinus: asin")
        print("arccosinus: acos")
        print("arctangens: atan")
        print("addition: add")
        print("subtraction: minus")
        print("multiplication: mult")
        print("division: div")
        print("modulo: mod")
        print("square root: sqrt")
        print("exponent: exp")
        print("square: sqr")
        print("ceiling: ceil")
        print("round: rnd")
        print("logarithm: log")
        print("e: e")
        print("pi: pi")
        print("fibonacci: fibonacci")
        print("factorial: factorial")
        print("isnan: isnan")
        print("hypot: hypot")
        print("binary: binary")
        print("octal: octal")
        print("hex: hex")
        print("degrees: degrees")
        print("radians: radians")
        print("sinh: sinh")
        print("cosh: cosh")
        print("tanh: tanh")
        print("isinfinite: isinfinite")
        print("isfinite: isfinite")
        print("isint: isint")
        print("root: root")
        print("cube: cube")
        print("cubeRoot: cubeRoot")
        print("help: help")
        print("exit: exit")
        print("random: random")
    elif cmd == "exit":
        break
    else:
        print("Unknown command")

