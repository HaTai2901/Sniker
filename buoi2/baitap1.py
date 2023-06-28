'''
bài tập:
tạo 1 movie list chứa các bộ phim đã xem
sử dụng hàm input để nhập vào 1 bộ phim khác không có trong list trên
thêm bộ phim vừa nhập vào cuối danh sách list
in ra bộ phim ở đầu tiên, ở giữa và ở cuối danh sách
tính tổng bộ phim có trong list
xóa bộ phim đầu và cuối trong list
lấy ra và xóa bộ phim cuối trong list
chèn 1 bộ phim bất kì vào đầu danh sách
đếm số bộ phim có tiêu đề là "naruto"
tìm vị trí của bộ phim có tiêu đề là naruto
thêm một danh sách các bộ phim khác vào cuối danh sách movies ban đầu
xóa list
'''



# tạo 1 movie list chứa các bộ phim đã xem
movie_list  = ['naruto', 'cha_naruto', 'luffy', 'monalisa', 'picasio',  'im_coming_home', 'ae_la_dan_Binh_Phuoc']


# sử dụng hàm input để nhập vào 1 bộ phim khác không có trong list trên
# thêm bộ phim vừa nhập vào cuối danh sách list
new_movie = input('nhap ten moi: ')
movie_list.append(new_movie)
print(movie_list)

# in ra bộ phim ở đầu tiên, ở giữa và ở cuối danh sách
first_movie = movie_list[0]
# ở giữa
phim_o_giua =  len(movie_list) // 2
mid_movie = movie_list[phim_o_giua]
# ở cuối
last_movie  = movie_list[-1]

# tính tổng bộ phim có trong list
sum_movie = sum(movie_list)
print(sum_movie)

# xóa bộ phim đầu và cuối trong list
del movie_list[0]
del movie_list[-1]
print(movie_list)

# lấy ra và xóa bộ phim cuối trong list
pop = movie_list.pop()
print(pop)
print(movie_list)

# chèn 1 bộ phim bất kì vào đầu danh sách
movie_list.insert(0 ,new_movie)

# đếm số bộ phim có tiêu đề là "naruto"
amount  =  movie_list.count('naruto')
print(f'thg naruto xuat hien {amount} lan trong New Movie ')

# tìm vị trí của bộ phim có tiêu đề là naruto
location = movie_list.index('naruto')

# thêm một danh sách các bộ phim khác vào cuối danh sách movies ban đầu
dif_movie = ['Chap nhan', 'Thuc Tinh', 'Ao Giac',  'Phim Sẽ gầy tháng 7']
movie_list.extend(dif_movie)
print(movie_list)

# xóa list
movie_list.clear()
print(movie_list)

