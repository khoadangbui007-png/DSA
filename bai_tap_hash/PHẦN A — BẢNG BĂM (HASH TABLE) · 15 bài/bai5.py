def group_by_first_letter(words):
    groups = {}
    for word in words:
        if word:
            key = word[0]
            if key not in groups:
                groups[key] = []
            groups[key].append(word)
    return groups

if __name__ == "__main__":
    words = ["apple", "banana", "apricot", "cherry"]
    print("Bài 5 - Nhóm từ:", group_by_first_letter(words))