produktu_saraksts = []

veikals = int(input('Kādā veikalā jūs iepērkaties? (rimi=1, top=2, maxima=3, vesko=4 un bazars=5): '))

if veikals == 2 or veikals == 3:
    karte = input('Vai jums ir klienta karte? (jā=j, nē=n): ')
elif veikals == 4:
    daudzums_viss = int(input('Cik preces vēlaties pirkt: '))

while True:
    produkts = input('Ievadiet produktu nosaukumu kādu vēlaties iegādāties: ')
    cena = int(input('Ievadiet produkta cenu: '))
    daudzums = int(input('Ievadiet produkta daudzumu: '))
    
 
    if veikals == 1:
        cena_ar_atlaidi = cena * daudzums - 0.3
    elif veikals in [2, 3] and karte == 'j':
        cena_ar_atlaidi = cena * daudzums - 0.4
    elif veikals == 2 and karte == 'n':
        cena_ar_atlaidi = cena * daudzums
    elif veikals == 3 and karte == 'j':
        cena_ar_atlaidi = cena * daudzums - 0.5
    elif veikals == 3 and karte == 'n':
        cena_ar_atlaidi = cena * daudzums - 0.2
    elif veikals == 4 and daudzums_viss >= 3:
        cena_ar_atlaidi = cena * daudzums - 0.3
    elif veikals == 4 and 0 < daudzums_viss < 3:
        cena_ar_atlaidi = cena * daudzums
    elif veikals == 5:
        cena_ar_atlaidi = cena * daudzums - 0.5

    
    produkts = {
        'nosaukums': produkts,
        'cena': cena,
        'daudzums': daudzums,
        'cena_ar_atlaidi': cena_ar_atlaidi
    }
    produktu_saraksts.append(produkts)

    stop = input('Vai ir nopirkts viss kas ir sarakstā: (jā=j, nē=n): ')
    if stop == 'j':
        break

print('\n\t*******Čeks*******')
print('\n\tCenas par produktiem:')
kopeeja_cena = 0

for produkts in produktu_saraksts:
    nosaukums = produkts['nosaukums']
    cena = produkts['cena']
    daudzums = produkts['daudzums']
    cena_ar_atlaidi = produkts['cena_ar_atlaidi']

    if daudzums > 1:
        print('\n\t', nosaukums, cena, 'eiro', '\n\tDaudzums ir', daudzums, '\n\tKopsumma ar atlaidi ir', cena_ar_atlaidi, 'eiro')
        print('\n\t Cena bez atlaides ir ', daudzums*cena, 'eiro')
    elif daudzums == 1:
        print('\n\t', nosaukums, cena, 'eiro', '\n\tKopsumma ar atlaidi ir', cena_ar_atlaidi, 'eiro')
        print('\n\t Cena bez atlaides ir ', cena, 'eiro')
    kopeeja_cena += cena_ar_atlaidi

print('\n\tKopsumma apmaksai:', kopeeja_cena, 'eiro')