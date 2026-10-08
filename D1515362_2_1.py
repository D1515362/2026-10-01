A = int(input("請輸入0或1:")) 
B = int(input("請輸入0或1:"))
if (A == 0 or A == 1) and (B == 0 or B == 1):
    if A == 0 and B == 0:
        print("A OR B = 0")
        print("A AND B = 0")
        print("A XOR B = 0")
    elif A == 0 and B == 1:
        print("A OR B = 1")
        print("A AND B = 0")
        print("A XOR B = 1")
    elif A == 1 and B == 0:
        print("A OR B = 1")
        print("A AND B = 0")
        print("A XOR B = 1")
    elif A == 1 and B == 1:
        print("A OR B = 1")
        print("A AND B = 1")
        print("A XOR B = 0")
else:
    print("輸入錯誤")                    