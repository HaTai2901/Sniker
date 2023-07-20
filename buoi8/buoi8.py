USER_MENU = '''
a - thêm sách
l - hiển thị sách
s - tìm kiếm sách
x - xóa sách
u - cập nhật thông tin sách
q - thoát
Lựa chọn của bạn:
=> '''
book_file = 'books.csv'

try:
    with open(book_file, 'x') as file:
        file.read()
except:
    print('khong mo duoc file')


def add_book():
    title = input('nhap ten sach: ').strip().title()
    author = input('nhap ten tac gia: ').strip().title()
    release_year = input('nhap nam xuat ban: ').strip()

    with open(book_file, 'a') as file:
        file.write(f'{title},{author},{release_year}\n')

    return title, author, release_year

def show_book(line):
    title, author, release_year = line.strip().split(',')
    print(f'Title: {title} - Author: {author}, Release year: {release_year}')

def get_book():
    with open(book_file, 'r') as file:
        for line in file:
            show_book(line)

def search_book():
    search_title = input('nhap ten sach can tim: ').strip().lower()
    with open(book_file, 'r') as file:
        for line in file:
            title,_,_, = line.strip().split(",")
            if title.lower() in search_title:
                show_book(line)
                break
        else:
            print(f'Không tìm thấy thông tin Book có tên là {search_title}')


def update_book():
    update_title = input('nhap ten sach can thay doi: ').strip().lower()
    found = False
    updated_books = []
    with open(book_file, 'r') as file:
        for line in file:
            title, author, release_year = line.strip().split(",")
            if title.lower() in update_title:
                found = True
            print('Sách cần cập nhật:')
            print(f'Tên sách: {title}')
            print(f'Tác giả: {author}')
            print(f'Năm xuất bản: {release_year}')


            new_title = input('nhap ten sach moi : ').strip()
            new_author = input('nhap tac gia moi : ').strip()
            new_release_year = input('nhap nam xuat ban moi : ').strip()

            if not new_title:
                    new_title = title
            if not new_author:
                    new_author = author
            if not new_release_year:
                    new_release_year = release_year

            updated_books.append(f"{new_title},{new_author},{new_release_year}\n")
        else:
            updated_books.append(line)

    if not found:
        print('khong thay sach can cap nhat')

    with open(book_file, 'w') as file:
        file.writelines(updated_books)

    print('Da cap nhat thanh cong')

n = update_book()