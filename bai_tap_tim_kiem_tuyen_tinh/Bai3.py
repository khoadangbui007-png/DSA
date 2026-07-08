def linear_search_count(A, x):
    count = 0

    for i in range(len(A)):
        count += 1
        if A[i] == x:
            return i, count

    return -1, count


A = [7, 3, 9, 12, 5, 8, 1]

# a) x = 7
vi_tri, so_sanh = linear_search_count(A, 7)
print("a) x = 7")
print("Vi tri:", vi_tri)
print("So phep so sanh:", so_sanh)

# b) x = 1
vi_tri, so_sanh = linear_search_count(A, 1)
print("\nb) x = 1")
print("Vi tri:", vi_tri)
print("So phep so sanh:", so_sanh)

# c) x = 100
vi_tri, so_sanh = linear_search_count(A, 100)
print("\nc) x = 100")
print("Vi tri:", vi_tri)
print("So phep so sanh:", so_sanh)