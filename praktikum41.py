a = int(input("Masukkan jumlah maksimal: ")) 

for i in range(a, 0, -1):
    for j in range(i):
        print(i, end="")
    print()

