A = [7, 3, 9, 12, 5, 8, 1]
x = 5

for i in range(len(A)):
    print("Buoc", i + 1, ": A[", i, "] =", A[i])

    if A[i] == x:
        print("Tim thay x tai vi tri", i)
        break
    else:
        print("Chua tim thay, tiep tuc")