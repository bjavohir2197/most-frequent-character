def eng_ko_p_uchraydigan_belgi(matn):
    belgilar = {}
    for belg in matn:
        if belg in belgilar:
            belgilar[belg] += 1
        else:
            belgilar[belg] = 1
    max_belgi = max(belgilar, key=belgilar.get)
    return max_belgi

matn = input("Matnni kiriting: ")
print("Eng ko'p uchraydigan belgi:", eng_ko_p_uchraydigan_belgi(matn))
