
pareiza_parole = '54321'                 #izveidoti 4 mainīgie
pareizs_lietotajvards = 'vasara'
meginajumu_skaits = 5
pas_meginajumi = 0

while pas_meginajumi < meginajumu_skaits:  #Programma lietotājam jautā ievadīt lietotājvārdu un paroli kamēr nav pareizi
    ievaditais_lietotajvards = input('Lūdzu ievadiet savu lietotājvārdu:')
    if ievaditais_lietotajvards == 'stop': #Ja lietotājs vēlas pārtraukt un ieraksta stop, programma beidzas
      print('Programmas beigas!')
      break
    ievadita_parole = input('Lūdzu ievadiet savu paroli:')

    if ievaditais_lietotajvards == 'stop' or ievadita_parole == 'stop': #Ja lietotājs vēlas pārtraukt un ieraksta stop, programma beidzas
        print('Programmas beigas!')
        break
    if len(ievadita_parole)<5:
      print('Parole ir par īsu, jābut 5 rakstzimju garai!')
     
    elif len(ievadita_parole)>5:
      print('Parole ir par garu, jābut 5 rakstzimju garai!')

    if ievaditais_lietotajvards == pareizs_lietotajvards and ievadita_parole == pareiza_parole: #Pēc tam kad ir ievadīti pareizi dati, sākas 2. uzdevums kurā lietotājs ievada 1. un 2. skaitli
        print('Pieslēgšanās veiksmīga')
        pirmais_ves_sk = input('Ievadiet 1. veselo skaitli:')
        if pirmais_ves_sk=='stop': #Ja lietotājs vēlas pārtraukt un ieraksta stop, programma beidzas
          print('Programmas beigas!')
          break
        otrais_ves_sk = input('Ievadiet 2. veselo skaitli:')
        if otrais_ves_sk=='stop': #Ja lietotājs vēlas pārtraukt un ieraksta stop, programma beidzas
         print('Programmas beigas!')
         break
        pirmais_ves_sk2= int(pirmais_ves_sk)
        otrais_ves_sk2= int(otrais_ves_sk)
        if pirmais_ves_sk2 < 0 or otrais_ves_sk2 < 0: #Pārbauda vai ievadītie skaitļi nav negatīvi
            print('Skaitļi nevar būt negatīvi')
        elif otrais_ves_sk < pirmais_ves_sk: #Pārbauda vai ievadītie skaitļi, otrais nav mazāks par pirmo
            print('0')
        else:
            summa = 0
            for i in range(pirmais_ves_sk2, otrais_ves_sk2 + 1): #Skaitļu kopa pēc ievadītajiem skaitļiem, un apreķina to summu
                summa += i
            print('Summa:', summa)

        break
    else:
        pas_meginajumi += 1
        if pas_meginajumi == meginajumu_skaits:
            print('Beidzies mēģinājumu skaits!')
        else:
            atlikusie_meginajumi = meginajumu_skaits - pas_meginajumi
            print('Ir atlikuši vēl', atlikusie_meginajumi, 'mēģinājumi!')