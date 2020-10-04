# ----------Bài 08: Viết hàm
#         def body_mass_index(m, h)
#     để tính toán chỉ số BMI của một người với cân nặng m (kg), chiều cao h (m)
#       Viết hàm
#         def bmi_information(m, h)
#     để đưa ra thông tin về chỉ số BMI cũng như phân loại mức độ gầy - béo của người cân nặng m, chiều cao h
# --------------------------------------------------------------
print("----TÍNH TOÁN CHỈ SỐ BMI-------")
def body_mass_index(m,h):
    BMI=m/math.pow(h,2)
    return BMI
def bmi_information(m,h):
    bmi=body_mass_index(m,h)
    if bmi > 30:
        print("Béo phì")
    elif bmi >=25:
        print("Thừa cân")
    elif bmi >=18.5:
        print("Bình thường")
    else:
        print("Gầy")
m=float(input("Nhập cân nặng: "))
h=float(input("Nhập chiều cao: "))
while m<0 or h<0:
    print("Dữ liệu không hợp lệ\n Nhập lại")
    print("Cân nặng là: ",end="")
    m=float(input())
    print("Chiều cao là: ",end="")
    h=float(input())
bmi_information(m,h)