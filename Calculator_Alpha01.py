#Calculator_Alpha
#The alpha file for the personal calculator project
#Made by: ChitterCharmer
#Revision History
#Version: 0.1alpha
#Made into beta at:

count = 0

print()
print("Enter a number: ")
count = float(input())
print("Pick a equation symbol: ")
equationSymbol = input()
match equationSymbol:
    case "+":
        print("Enter a number: ")
        count2 = float(input())
        count = count + count2
    case "-":
        print("Enter a number: ")
        count2 = float(input())
        count = count - count2
    case "*":
        print("Enter a number: ")
        count2 = float(input())
        count = count * count2
    case "/":
        print("Enter a number: ")
        count2 = float(input())
        count = count / count2
    case "=":
        count = count
    case _:
        equationSymbol = float(equationSymbol)
        count = equationSymbol
        
print(count)

