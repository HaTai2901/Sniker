# '''
# if - elif - else
# '''
# # Cú pháp:
# # if điều_kiện:
#     # câu_lệnh
# """ thoi_tiet = 'nang'
# if thoi_tiet == 'nang':
#     print('oke')
# else:
#     print('noo')

# num = int(input('nhap n: '))

# if num >0:
#     print('so duong')
# elif num == 0:
#     print('so 0')
# else:
#     print('so am')

# print('n chia het cho 2' if num % 2 == 0 else 'nn khong chia het cho 2') """

# # hàm nhập nâng cao
# # khi nhập bằng input() giá trị sẽ là 1 chuỗi, hàm split() sẽ tách chuỗi ra thành các phần tử (mặc định không)
# # truyền tham số sẽ cắt theo " ", sau đó hàm map() sẽ convert chuỗi thành int
# """ s = 'a b c'
# print(s.split())
# list1 = input().split()
# print(list1)
# print(list(map(int, list1))) """

# # nhập nhiều dãy số trên cũng 1 hàng
# """ a, b = map(int, input().split())
# print(a if a <b else b) """

# # hàm eval() dùng để đánh giá biểu thức bên trong chuỗi
# """ print(eval('1+2'))
# lst = list(map(eval, input().split()))
# print(lst) """

# # in ra trên cùng 1 hàng cách ra bởi dấu cách
# """ lst = [1, 2, 3, 4]
# print(*lst, sep = "%") """

# # format
# # x = 2.4567
# # print(format(x, '.2f'))

# # hàm round(): làm tròn
# # hàm pow() tính lũy thừa
# # hàm sorted() dùng để sắp xếp và trả về 1 list mới
# # ord() trả về mã ascii
# # divmod() phép chia trả về số nguyên và số dư

# # ================================================================================================================================

# '''
# for
# while
# vòng lặp lồng nhau
# break: thoat vong lap
# countinue: bỏ qua các câu lệnh bên dưới nó và chuyển sang một vòng lặp mới
# '''

# # for _ in range(5):
# #     print('hello world')

# # for i in range(21):
# #     if i % 2 == 0:
# #         print(i, end=' ')

# # s = input('> ')
# # while s != 'q':
# #     print('hello')

# # vòng lặp for lặp số lần lặp xác định, while lặp số lần không xác định

# for i in range(5):
#     for j in range(3):
#         print(i, j, sep=' - ')

# for i in range(1, 21):
#     if i % 2 == 0:
#          continue #bỏ qua fong print
#     print(i, end = ' ')

# ví dụ vẽ chữ N
# n = int(input('nhap chieu cao'))

# for i in range(n):
# 	for j in range(n):
# 		if j==0 or i == j or j==n-1:
# 			print('*', end = ' ')
# 		else:
# 			print(" ", end = ' ')
# 	print()

# ví dụ vẽ tam giác:
# n = int(input('nhap chieu cao'))

# for i in range(n):
# 	for j in range(n):
# 		if j==0 or i == j or i==n-1:
# 			print('*', end = ' ')
# 		else:
# 			print(" ", end = ' ')
# 	print()