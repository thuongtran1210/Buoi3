#---------------- Bài 09: Viết hàm
#         def change_upper_lower(str)
#     chuyển toàn bộ các ký tự in hoa sang in thường và in thường thành in hoa trong str
# ---------------------------------------------------------------------
print("Chuyển chữ hoa thành chữ thường và ngược lại")
def change_upper_lower(str):
    str=str.swapcase()
    print(f"Chuỗi sau khi chuyển: {str}")
str=input("Nhập chuỗi muốn chuyển: ")
change_upper_lower(str)