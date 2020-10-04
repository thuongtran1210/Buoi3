# ----Bài 02: Viết hàm
    #     def reverse_string(str)
    # trả lại chuỗi đảo ngược của chuỗi str
# --------------------------------------------------------------
def reverse_string(str):
    return str[::-1]
str=input("Nhập số nghịch đảo: ")
print(f"Sau khi nghịch đảo: {reverse_string(str)}")