import csv


with open("products.csv", encoding="utf-8-sig")as file:
    answer = list(csv.reader(file, delimiter=';'))
    answer[0].append('promocode')
    """Добавляем категорию promocode к списку категорий"""
    for s in range(1, len(answer)):
        b = answer[s]
        """b - список по индексу s"""
        prom = b[1][0] + b[1][1].upper() + b[2][:2] + b[1][:-3:-1].upper() + b[2][4] + b[2][3]
        """prom - промокод к товару"""
        answer[s].append(prom)

with open("product_promo.csv", 'w', encoding="utf-8-sig", newline="")as file2:
    writer = csv.writer(file2, delimiter=';')
    writer.writerows(answer)
    """Записываем в новый файл"""
