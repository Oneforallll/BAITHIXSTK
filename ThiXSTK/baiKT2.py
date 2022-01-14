#Vũ Công Hoan 1451020093
#câu a
name = input("Nhập tên đệm của bạn:")
print(name)
#câu b
def tongcacchuso(n):
    tong = 0
    while (n > 0):
        tong = tong + n % 10
        n = int(n / 10)
    return tong
a = input("Nhập tên của bạn:")
n=len(a)+len(name)
print("Độ dài tên:",n)
print("Tổng các chữ số của", n, "là", tongcacchuso(n))