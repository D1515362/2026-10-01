x = int(input("請輸入0或1:")) 
y = int(input("請輸入0或1:"))
if (x == 0 or x == 1) and (y == 0 or y == 1):
    if x == 0 and y == 0:
        print("x OR y = 0")
        print("x AND y = 0")
        print("x XOR y = 0")
    elif x == 0 and y == 1:
        print("x OR y = 1")
        print("x AND y = 0")
        print("x XOR y = 1")
    elif x == 1 and y == 0:
        print("x OR y = 1")
        print("x AND y = 0")
        print("x XOR y = 1")
    elif x == 1 and y == 1:
        print("x OR y = 1")
        print("x AND y = 1")
        print("x XOR y = 0")
else:
    print("輸入錯誤")                    