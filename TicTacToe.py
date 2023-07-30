lst = [[1, 2, 3, 4, 5, 6, 7, 8, 9]]

for itr in lst:
    print(*itr[:3])
    print(*itr[3:6])
    print(*itr[6:9])
count_ = 0
while count_ != 9:
    a = int(input('Введите число от 1 до 9: '))
    b = str(input('Введите X или O: '))
    for i in lst:
        for j in i:
            if j == a:
                i[j - 1] = b
    for itr in lst:
        print(*itr[:3])
        print(*itr[3:6])
        print(*itr[6:9])
    count_ += 1

print('Конец игры!') # Сделать проверку победы слишком сложно :)
print(win)