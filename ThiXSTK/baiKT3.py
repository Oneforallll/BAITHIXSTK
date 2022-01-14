#Vũ Công Hoan 1451020093
#câu a
name = input("Nhập tên đầy đủ của bạn:")
print(name)
#câu b
def KTThuanNghich(n):
    str1 = str(n)
    str2 = str1[::-1]
    if (str1 == str2):
        return True
    else:
        return False
a=len(input("Nhập họ của bạn:"))
b=len(input("Nhập tên đệm của bạn:"))
c=len(input("Nhập tên của bạn:"))
n = str(a)+str(b)+str(c)
print("n=",n)
print("Số", n , "là" ,KTThuanNghich(n))

