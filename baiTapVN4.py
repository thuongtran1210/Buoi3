# -----Bài 04: Viết hàm
    #     def is_prime(n)
    # để kiểm tra xem số tự nhiên n có phải số nguyên tố hay không, nếu có thì trả lại True, nếu không thì trả lại False
# -------------------------------------------------------------------
print("----KIỂM TRA SỐ NGUYÊN TỐ------")
def is_prime(n):
    if n<=1:
        return False
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True
print("NHẬP SỐ MUỐN KIỂM TRA: ",end="")
n=int(input())
if is_prime(n):
    print(f"{n} TrueTrue")
else:
    print(f"{n} False")