"""
bài tập: nhập vào 1 năm bất kì, kiểm tra xem năm đó có phải năm nhuận hay không? biết rằng năm nhuận là năm chia hết cho 4 nhưng không chia hết cho 100 hoặc chia hết cho 400

bài tập: nhập vào 1 tháng, kiểm tra xem tháng đó có bao nhiêu ngày. nếu là tháng 2 yêu cầu nhập thêm năm, năm không nhuận có 28 ngày, năm nhuận có 29 ngày

bài tập: giải phương trình bậc 2 
"""
# BAIMOT
# bài tập: nhập vào 1 năm bất kì,
#  kiểm tra xem năm đó có phải năm nhuận hay không? biết rằng năm nhuận là
#  năm chia hết cho 4 nhưng không chia hết cho 100 hoặc chia hết cho 400

# year = int(input("Nhập vào một năm: "))

# flag = False

# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             flag = True
#     else:
#         flag = True

# if flag:
#     print(year, "là một năm nhuận.")
# else:
#     print(year, "không phải là một năm nhuận.")



# BAI 2
# bài tập: nhập vào 1 tháng, kiểm tra xem tháng đó có bao nhiêu ngày. nếu là tháng 2 yêu cầu nhập thêm năm, năm không nhuận có 28 ngày, năm nhuận có 29 ngày

# month = int(input("Nhập vào một tháng : "))

# if month == 2:
#     year = int(input("Nhập vào một năm: "))
#     if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#         days = 29  
#     else:
#         days = 28  
# elif month in [4, 6, 9, 11]:
#     days = 30  
# else:
#     days = 31

# print("Tháng", month, "có", days, "ngày")

# bài tập: giải phương trình bậc 2 

# import math

# a = float(input("Nhập  a: "))
# b = float(input("Nhập  b: "))
# c = float(input("Nhập  c: "))

# delta = b**2 - 4*a*c

# if delta > 0:
#     x1 = (-b + math.sqrt(delta)) / (2*a)
#     x2 = (-b - math.sqrt(delta)) / (2*a)
#     print("Phương trình có hai nghiệm phân biệt:")
#     print("x1 =", x1)
#     print("x2 =", x2)
# elif delta == 0:
#     x = -b / (2*a)
#     print("Phương trình có nghiệm kép:")
#     print("x =", x)
# else:
#     print("Phương trình vô nghiệm.")