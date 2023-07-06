# nhập n
n = int(input('nhap n: '))


# convert về str
str_n = str(n).strip()

# lấy độ dài của chuỗi str_n
dai = len(str_n)
print(f'len // 2: {dai // 2}')
for i in range(dai // 2):
    print(f'i la: {i}')
    print(f'i la: {str_n[dai - i - 1]}')

 # vòng lặp
for i in range(dai // 2):
    print(str_n[i])
    print(f'{n} la so doi xung')
    print(str_n[dai - i -1])
    print()
    if str_n[i] != str_n[dai - i -1]:
        print(f'{n} khong phai la so doi xung')
    






# if flag:
#     print(f'{n} la so doi xung')
# else:
#     print(f'{n} khong phai la so doi xung') 
