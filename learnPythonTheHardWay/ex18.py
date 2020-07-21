def printTwo(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

def printTwoAgain(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

def printOne(arg1):
    print(f"arg1: {arg1}")

def printNone():
    print("I got nothin'.")

printTwo("1", 2)
printTwoAgain("Zed", "Shaw")
printOne("First!")
printNone()