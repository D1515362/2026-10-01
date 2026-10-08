x = int(input("請輸入0~15的整數:"))
if x < 0 or x > 15:
    print("輸入錯誤")
else:
    t3 = (x // 8) % 2
    t2 = (x // 4) % 2
    t1 = (x // 2) % 2
    t0 = x % 2
    two= f"{t3}{t2}{t1}{t0}"

    e1 = (x // 8) % 8
    e0 = x % 8
    eight= f"{e1}{e0}"
    if x < 10:
        sixteen= str(x)
    elif x == 10:
        sixteen= "A"
    elif x == 11:
        sixteen= "B"
    elif x == 12:
        sixteen= "C"
    elif x == 13:
        sixteen= "D"
    elif x == 14:
        sixteen= "E"
    else: 
        sixteen= "F"
print(f"二進制: {two}")
print(f"八進制: {eight}")
print(f"十六進制: {sixteen}")        