y = input("輸入要轉換的單位:")
number = float(input("輸入要轉換的數值:"))
if y=="攝氏":
    x= (number * 9/5) + 32
    print("攝氏",number,"度=華氏",round(x,1),"度")
elif y=="華氏":
    x= (number - 32) * 5/9
    print("華氏",number,"度=攝氏",round(x,1),"度")  
elif y=="公里":
    x= number * 0.6214
    print(number,"公里=",round(x,1),"英里") 
elif y=="英里":
    x= number / 0.6214
    print(number,"英里=",round(x,1),"公里")
elif y=="公斤":
    x= number * 2.20462
    print(number,"公斤=磅",round(x,1),"磅")
elif y=="磅":   
    x= number / 2.20462
    print(number,"磅=公斤",round(x,1),"公斤") 
else:
    print("無效的選項")                         