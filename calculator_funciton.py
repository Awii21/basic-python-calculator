def calculator():
    num1 = int(input("enter num1: "))
    num2 = int(input("enter num2: "))
    add = num1 + num2
    sub = num1 - num2
    multi = num1 * num2
    div = num1/num2
    print("1: Add")
    print("2: Subtract")
    print("3: Multiply")
    print("4: Divide")
    operator = int(input("enter operator: "))
    if operator == 1:
        print(add)
    elif operator == 2:
        print(sub)
    elif operator == 3:
        print(multi)
    elif operator == 4:
        print(div)
    else:
        print("invalid operator value")
calculator()
