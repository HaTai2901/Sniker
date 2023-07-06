"""
Tính S(n)=1 + 1/2! + 1/3! + ... + 1/n! (n>0)
"""
import math

n = int(input("Nhập vào giá trị n: ")) 
tong = 0  
for i in range(1, n+1):
    giaithua = math.factorial(i) 
print("Giá trị của biểu thức S(n) là:", tong) 