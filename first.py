yarancaq = ""

# İlk faylı oxuyuruq və ilk sətiri böyük hərflərə çeviririk
with open("newfile.txt", mode="r", encoding="utf-8") as data:
    data = data.readline()
    yaranacaq = data.upper()
    print(yaranacaq)  # Test üçün çap edirik

# Böyük hərflərə çevrilmiş sətiri yeni fayla yazırıq
with open("newfile2.txt", mode="w", encoding="utf-8") as yeni:
    yeni.write(yaranacaq)
