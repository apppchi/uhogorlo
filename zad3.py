import csv


with open("products.csv", encoding="utf-8-sig")as file:
    answer = list(csv.reader(file, delimiter=';'))
    mn = set()
    """mn - все категории"""
    for category, product, date, priceperunit, count in answer:
        if category != 'Category':
            mn.add(category)
    mn = list(mn)
    mini = [1000000000] * len(mn)
    prod = [''] * len(mn)
    """
        mini - минимальное количество товара категории списком
        prod - название продукта с минимальным количеством в категории
    """
    for category, product, date, priceperunit, count in answer:
        if category != 'Category':
            ind = mn.index(category)
            if float(count) < mini[ind]:
                mini[ind] = float(count)
                prod[ind] = product
    """Расставляем количество и товар в списках с соответствии с категорией по индексу"""
    al = input()
    while al != "молоко":
        if al in mn:
            indi = mn.index(al)
            print(mn[indi], mini[indi], prod[indi])
        else:
            print("Такой категории не существует в нашей БД")
        al = input()
    """Ввод данных и вывод результата"""
