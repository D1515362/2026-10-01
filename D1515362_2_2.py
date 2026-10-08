a = int(input())
b = int(input())
s = int(input())

if (a == 0 or a == 1) and (b == 0 or b == 1) and (s == 0 or s == 1):

    if a != b:
        middle = 1
    else:
        middle = 0
    if middle == 1 and s == 1:
        start = 1
    else:
        start = 0
    print(f"第一個閥輸出:{middle}")
    print(f"允許啟動: {start}")
else:        
    print(f"輸入錯誤")