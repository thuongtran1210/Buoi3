# ----------------Bài 11: Cho dãy số Tribonacci với công thức truy hồi sau:
#             F(n) = F(n-1) + F(n-2) + F(n-3),    F(1) = 1, F(2) = 1, F(3) = 2
#     Xây dựng 2 hàm để tìm ra số thứ n trong dãy số theo:
#         + Hàm Đệ quy
#         + Hàm Không đệ quy
# -------------------------------------------------------------------------------------
print("TÌM DÃY Fibonacci THEO ĐỆ QUY")
def fibo_dequy(n):
    if n==1 or n==2:
        return 1
    return fibo_dequy(n-1) + fibo_dequy(n-2)
print("TÌM Fibonacci KHÔNG THEO ĐỆ QUY ")
def fibo_thuong(n):
    n1=0
    n2=1
    for i in range(n-1):
        temp=n1+n2
        n1=n2
        n2=temp
    return temp
print("Nhập số fibo: ",end="")
n=int(input())
while n<=0:
    print("Số không hợp lệ\n Nhập lại")
    print("Nhập số fibo: ",end="")
    n=int(input())
print(f"Đệ quy: {fibo_dequy(n)}")
print(f"Không đệ quy: {fibo_thuong(n)}")