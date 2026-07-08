def gan_x_nhat(a, x):
    min_diff = abs(a[0] - x)
    vi_tri = 0

    for i in range(1, len(a)):
        diff = abs(a[i] - x)

        if diff < min_diff:
            min_diff = diff
            vi_tri = i

    return a[vi_tri], vi_tri


a = [10, 22, 28, 29, 40]
x = 26

value, pos = gan_x_nhat(a, x)

print("Gan nhat la:", value)
print("Vi tri:", pos)