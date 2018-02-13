print("Enter a number ")
x = int(input("starting"))
sum = 0
if (x > 0):
    print("Hello in our game")
else:
    print("this number should be positive  ")
    print("try again ")
    x = int(input())
if (x > 0):
    print("player 1")
    y = int(input())
    import math
    number = math .sqrt(y)
    if (number * number == y):
        sum = sum + y

    else:
        print("try again ")
        y = int(input())
        import math
        number = math.sqrt(y)
        if (number * number == y):
            sum = sum + y
    remaining = x - y
    print("player 1 subtract ", y, "remaining is ", remaining)
if (remaining == 0):
    print("player 1 wins ")
else:
    print("player 2 ")
    y = int(input())
    import math
    number = math.sqrt(y)
    if (number * number == y):
        sum = sum + y
    else:
        print("try again")
        y = int(input())
        number = math.sqrt(y)
        if (number * number == y):
            sum = sum + y
    remaining = remaining - y
    print("player 2 subtract ", y, "remaining is ", remaining)
    if (remaining == 0):
         print("player 2 wins")

while (remaining > 0):
    print("player 1 ")
    y = int(input())
    import math
    number = math.sqrt(y)
    if (number * number == y):
        sum = sum + y
    else:
        print("try again")
        y = int(input())
        number = math.sqrt(y)
        if (number * number == y):
            sum = sum + y
    remaining = remaining - y
    print("player 1 subtract ", y, "remaining is ", remaining)
    if (remaining == 0):
        print("player 1 wins")
    else:
        print("player 2 ")
        y = int(input())
        import math
        number = math.sqrt(y)
    if (number * number == y):
        sum = sum + y
    else:
        print("try again")
        y = int(input())
        import math
        number = math.sqrt(y)
        if (number * number == y):
            sum = sum + y
    remaining = remaining - y
    print("player 2 subtract ", y, "remaining is ", remaining)
    if (remaining == 0):
        print("player 2 wins")










