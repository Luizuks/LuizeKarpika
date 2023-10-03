amats= str(input('Vai jūs esat skolēns vai personals? [skolens,personals]'))
izdevums= str(input('Vai izdevums ir žurnāls vai grāmata? [gramata,zurnals]'))
pieprasijums= str(input('Vai zurnals,gramata ir pieprasito izdevumu sarakstā?[Ja, Ne]'))
nenodots= str(input('Vai Jums ir kāda nenodota grāmata vai žurnāls? [Ja, Ne]'))
if amats== 'skolens' and izdevums=='gramata' and pieprasijums=='Ne' and nenodots=='Ne' :
    print('Grāmata Jums tiek izsniegta uz 14 dienām. Paldies!')
elif amats== 'personals' and izdevums=='gramata' and pieprasijums=='Ne' and nenodots=='Ne':
    print('Grāmata Jums tiek izsniegta uz 28 dienām! Paldies!')
elif amats=='skolens' and 'personals' and izdevums=='zurnals' and pieprasijums=='Ne' and nenodots=='Ne':
    print('Žurnālu Jums izsniegs uz 7 dienām! Paldies!')
elif nenodots=='Ja':
    print('Jūs nēsat nodevuši kādu no izdevumiem, tāpēc grāmatu vai žurnālu jums neizsniegsim.')
elif pieprasijums=='Ja' and izdevums=='gramata':
    print('Grāmatu Jums izsniegs uz 2 dienām! Paldies!')
elif pieprasijums=='Ja' and izdevums=='zurnals':
    print('Žurnālu Jums izsniegs uz 2 dienām! Paldies!')