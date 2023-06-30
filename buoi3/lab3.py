"""
1. cho 2 set
art_student = {'john', 'anne', 'max', 'bob', 'obito'}
math_student = {'max', 'maery', 'david', 'anne', 'john'}
- tìm những sinh viên học cả 2 môn
- tìm những người học vẽ nhưng không học toán
- tìm những người học toán nhưng không học vẽ
- tìm những người bạn học vẽ hay toán không phải cả 2
- tìm tất cả những người

"""

# bai1
# art_student = {'john', 'anne', 'max', 'bob', 'obito'}
# math_student = {'max', 'maery', 'david', 'anne', 'john'}

# # tìm những sinh viên học cả 2 môn
# sv_chung = art_student.intersection(math_student)
# print(sv_chung)

# tìm những người học vẽ nhưng không học toán
# ArtnoMath = art_student.difference(math_student)
# print(ArtnoMath)

# tìm những người học toán nhưng không học vẽ
# MathnoArt = math_student.difference(art_student)
# print(MathnoArt)

# tìm những người bạn học vẽ hay toán không phải cả 2
# Not4all = art_student.symmetric_difference(math_student)
# print(Not4all)

# tìm tất cả những người
# All = art_student.union(math_student)
# print(All)


"""
2. tạo ra 1 album nhạc:
- lấy ra giá trị của các key sau: album_name, release_year bằng 2 cách
- thay đổi giá trị của key release_year từ 1971 thành 1973
- xóa phàn tử với keey là track_list
- thêm 1 key mới là amount = 2000 bằng 2 cách
- làm trống dict album_info
"""

# album
import json
dict = {
    'album_name': "Con rain cross by",
    'release_year': '2016'
}
# lấy ra giá trị của các key sau: album_name, release_year bằng 2 cách
print(dict)
print(json.dumps(dict, indent=4))

# [2 cach]
n = dict.keys()
print(n)

value1 = dict.get("album_name")

# thay đổi giá trị của key release_year từ 2016 thành 1973
dict['release_year'] = '1973'
print(json.dumps(dict, indent=4))

# xóa phàn tử với keey là track_list
"them key track_list"
dict['track_list'] = '001'
print(json.dumps(dict, indent=4))
"xoa track_list"
n = dict.pop('track_list')
print(json.dumps(dict, indent=4))

# thêm 1 key mới là amount = 2000 bằng 2 cách
dict['amount'] = '2000'
print(json.dumps(dict, indent=4))

"cach 2"
dict.update(amount = '2000')
print(json.dumps(dict, indent=4))

# làm trống dict album_info
"them key"
dict['album_info'] = 'Dam Vinh Hung - tpHCM'
print(json.dumps(dict, indent=4))
"xoa key"
dict.pop('album_info')
print(json.dumps(dict, indent=4))