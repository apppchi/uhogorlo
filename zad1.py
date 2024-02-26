import csv


with open("products.csv", encoding="utf-8-sig")as file:
    answer = list(csv.reader(file, delimiter=';'))


with open("products_new.csv", 'w', encoding="utf-8-sig", newline='')as file2:
    writer = csv.writer(file2, delimiter=';')
    answer[0].append('total')
    """Записываем в список категорий категорию total"""
    for i in range(1, len(answer)):
        answer[i].append(float(answer[i][-2]) * float(answer[i][-1]))
    """Записываем числовое значение total в наши столбцы"""
    writer.writerows(answer)
    """Записываем все выше перечисленное в новый файл products_new.csv"""


with open("products_new.csv", encoding="utf-8-sig") as csvfile:
    answer1 = list(csv.reader(csvfile, delimiter=';'))
    """Открываем наш новый файл"""
    summ = 0
    """summ - сумма всех товаров в закусках"""
    for category, product, date, priceperunit, count, total in answer1:
        if category == 'Закуски':
            """Проверяем на нужную нам категорию"""
            summ += float(total)
            """Прибавляем доход закусок к общей сумме"""
    print(summ)
