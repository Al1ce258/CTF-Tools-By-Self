sf = "32021119980405" #前14位(区号加生日)
CheckNum = ["1", "0", "X", "9", "8", "7", "6", "5", "4", "3", "2"]
yz = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]


def get_jy(InNum):
    Sum = 0
    for i in range(17):
        Sum += int(InNum[i]) * yz[i]
    T = Sum % 11
    return CheckNum[T]


for i in range(1, 1000):
    sfz_17 = sf + (3 - len(str(i))) * "0" + str(i)
    jy = get_jy(sfz_17)
    sfz = sfz_17 + jy
    with open("sfzs.txt", "a", encoding="utf-8") as f:
        f.write(sfz + "\n")
print("写入完成！")
