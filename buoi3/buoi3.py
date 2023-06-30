'''
- set{} không chứa phần tử giống nhau
- tuple()
'''
tup = 'a', 'c', 'b'
tup2 = 'd', 'e', 'f'
print(type(tup))
print(tup)

num = 1, 2, 3, 4, 5, 6, 7
total = tup + tup2
print(total.index('e'))

set = set()
print(set)

# set: chỉ chứa các phần tử không trùng lặp với nhau
# thêm phần tử vào set
set.add(1)
set.add(1)
set.add(1)
set.add(1)
print(set)
set.update(range(1, 100))
print(set)
pop = set.pop()
print(pop)
print(set)

set.clear()
print(set)

'''
 - dictionnary

'''

# dict = {'key' : value}
import json
dict = {'name': 'nam',
        'age': 25,
        'class': 'dth'}
print(dict)
print(json.dumps(dict, indent=4))
n = dict.keys()
print(n)

v = dict.values()
print(v)

# nếu in một key không nằm trong dict thì sẽ báo lỗi
value = dict['id']
print(value)

# ngược lại, nếu sử dụng phương thức get để lấy value của key, nếu key không nằm trong dict thì sẽ trả về None
vaue1 = dict.get('nid')
print(vaue1)

import json
dict = {'name': 'nam',
        'age': 25,
        'class': 'dth'}

# thêm key và value vào dictionary
dict['id'] = '001'
print(json.dumps(dict, indent=4))

# nếu thêm 1 key và value trùng với key, value đã tồn tại trước đó, nó sẽ update thay vì chèn
dict['name'] = 'tu'
print(json.dumps(dict, indent=4))

# update(): chèn thêm đc nhiều key, value khác nhau
dict.update(gender = 'female', gay = 'yes')
print(json.dumps(dict, indent=4))

# remove, pop, del, popitem
n = dict.pop('gay')
print(n)
print(json.dumps(dict, indent=4))

# popitem(): xóa đi cặp key, value nằm cuối cùng của dict, kết quả trả về là 1 tuple
pop = dict.popitem()
print(pop)
print(json.dumps(dict, indent=4))

keys = list[dict.keys()]
print(keys)

'''
    set nâng cao
'''

set1 = {1, 2, 3, 4 , 5, 6}
set2 = {1, 2, 4, 7 , 9, 16}

# tìm phần tử chung của 2 set
set3 = set1.intersection(set2)
print(set1 & set2)
print(set3)

# tìm phần tử khác nhau, có trong set 1 nhưng không có trong set 2
set4 = set1.difference(set2)
print(set1 - set2)
print(set4)

# lấy ra phần tử có trong 2 set
set5 = set1.union(set2)
print(set1 | set2)
print(set5)

# lấy tất cả nhưng trừ đi phần chung
set6 = set1.symmetric_difference(set2)
print(set1 ^ set2)
print(set6)

# điều kiện sử dụng: phải là 2 mảng dữ liệu giống nhau
lst = [[1, 2, 3, 4], [5, 6, 7, 8]]
s = sum(lst, ['nam'])
print(s)

# join(): dùng để chèn, với điều kiện phần tử phải là chuỗi
# map(): dùng để convert một biến nào đó thành kiểu dữ liệu mong muốn
lst1 = [1, 2, 3, 4] #[1 - 4 - 9 - 16]

x = '-'.join(map(str, lst1))
print(x)

def binh_phuong(y):
    return y ** 2

double = binh_phuong(2)
print (double)


print(tuple(map (binh_phuong, lst1)))

# eval(): hàm này dùng để tính toán mà không quan tâm đến kiểu dữ liệu của biển
x = 5
y = 1.5
print (5+2j+7)
print (eval ('5+2j'))