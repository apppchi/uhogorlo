import csv


with open("products.csv", encoding="utf-8-sig") as file:
    a = list(csv.reader(file, delimiter=';'))
    for f in range(2, len(a)):
        while a[f][3] > a[f-1][3] and f > 1:
            a[f], a[f-1] = a[f-1], a[f]
            f -= 1
    """Расставляем методом вставок список по цене за единицу товара"""
    for i in range(2, len(a)):
        while a[i][0] < a[i-1][0] and i > 1:
            a[i], a[i-1] = a[i-1], a[i]
            i -= 1
    """Расставляем методом вставок список по алфавиту категорий"""
    print('"В категории:', a[1][0], "самый дорогой товар:", a[1][1], "его цена за единицу товара составляет", a[1][3] + '"')
