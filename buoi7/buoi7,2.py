

# def trung_binh_cong(day_so):
#     tong = a + b+ c
#     trungbinh = tong / 3
#     return trungbinh

# a = 1
# b = 2
# c = 3

# kq = trung_binh_cong(a, b, c)
# print("trung binh cong la:", kq )

# def so_nguyen_to(n): #viết tên hàm
#         dem  = 1
#         for i in range(2, n+1):
#             if n % i == 0:
#                 dem += 1
#         if dem == 2:
#             return f'{n} la so nguyen to'
#         else:
#             return f'{n} khong phai so nguyen to'

# # truyền tham số vào hàm (n)
# so = 1
# # in ra  kết quả
# print(so_nguyen_to(so))


# cho một danh sách ngẫu nhiên viết hàm sắp xếp tăng dần

# def sap_xep(_list):
#     return sorted(_list)

# _list = input("nhap vao mot day so: ")
# dayso = list(map(eval, _list.split()))
# da_sap_xep = sap_xep(dayso)
# print("da sap xep tang dan:", da_sap_xep)