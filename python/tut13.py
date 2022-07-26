# print("agressive point of view , Fulty Calculator")
def main():
    operator=input("Enter operator: ")
    x = int(input("enter your first number: "))
    y = int(input("Enter your second number: "))

    if operator =="+":
        if x == 56 and y == 9:
            print("77")
        else:
            print(x+y)
    if operator == "-":
        if x - y:
            print(x-y)
    if operator == "*":
        if x == 45 and y == 3:
            print("555")
        else:
            print(x * y)
    if operator == "/":
        if x == 56 and y == 6:
            print("4")
        else:
            print(x / y)

    Repeat = input("Would you like to run this calculation again ")
    if Repeat == "yes":
        main()
    else:
        print("Thanks for calculations you do it. ")
        exit()
main()



