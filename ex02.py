y = int(input("請輸入西元年份: "))
if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
    print(f"{y} 年是閏年")
else:
    print(f"{y} 年是平年")