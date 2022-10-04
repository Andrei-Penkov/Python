import random
k = random.randint(4, 31)
print("Ваша задача оставить в куче 1 камень, чтобы победить, можно брать только 1,2 или 3 камня из кучи")
while k != 1:
    print("В куче ", k, " камней")
    r = int(input("Сколько вы хотите забрать камней 1, 2 или 3 \n"))
    if r <= 0 or r >= 4:
        print("Вы играете не по правилам")
        exit()
    k -= r
    print("В куче осталось ", k, " камней")
    if k <= 0:
        print("Вы проиграли(читайте правила игры)")
        exit()
    if k == 1:
        print("Вы выиграли")
        exit()
    print("Теперь хожу я")
    if k == 4:
        r = 3
    if k == 3:
        r = 2
    if k == 2:
        r = 1
    if k > 4:
        r = random.randint(1, 3)
    k -= r
    if k == 1:
        print("Я выиграл")
        exit()
