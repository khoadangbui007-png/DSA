MOD = 1000000007
BASE_ROW = 31
BASE_COL = 37


def hash_row(row):
    h = 0
    for c in row:
        h = (h * BASE_ROW + ord(c)) % MOD
    return h


def hash_matrix(matrix):
    h = 0
    for row in matrix:
        h = (h * BASE_COL + hash_row(row)) % MOD
    return h


matrix = [
    "abcd",
    "efgh",
    "ijkl"
]

pattern = [
    "fg",
    "jk"
]

p_hash = hash_matrix(pattern)

rows = len(pattern)
cols = len(pattern[0])

found = False

for i in range(len(matrix) - rows + 1):
    for j in range(len(matrix[0]) - cols + 1):
        sub = [matrix[i + k][j:j + cols] for k in range(rows)]
        if hash_matrix(sub) == p_hash:
            print("Tim thay tai:", (i, j))
            found = True

if not found:
    print("Khong tim thay")