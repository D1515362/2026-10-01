account = input("輸入您的帳號: ")
password = input("輸入您的密碼: ")
Balance = 10
if account == "Xiao Ming" and password == "123456":
    print("登入成功")
    print(f"您的帳戶餘額為: {Balance} 元 ")
else:
    print("帳號或密碼錯誤")    