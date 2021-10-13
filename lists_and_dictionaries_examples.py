#sarakstā var sakārtoti ielikt dažādus objektus
saraksts = ['apple', 'orange', "banana", 1, 2, 3]

#saraksta elementu indeksācija sākas ar 0 un pēdēja elementa indekss ir saraksta garums - 1
print('\nDaži saraksta elementi:')
print(saraksts[0])
print(saraksts[1])
print(saraksts[5])

#izvadīsim visus saraksta elementus ar cilpi 
print('\nSaraksta elementi:')
for elements in saraksts:    
    print(elements)

#vardnicā var sameklēt cilvēka datus pēc personas koda
vardnica = {'12345':{'name': 'Anna', 
                'surname': 'Abola', 
                'phone': '25469874', 
                'email': 'anna.abola@gmail.com'
                },
        '98745':{'name': 'John', 
                'surname': 'Bright', 
                'phone': '98745632', 
                'email': 'john.bright@gmail.com'
                }
}

#izvadīsim visus elementus vārdnicā izmantojot cipli
saraksts_ar_personas_kodiem = list(vardnica)
print('\nVisi vārnicas elementi:')
for kods in saraksts_ar_personas_kodiem:
    print(f'\nPerson {kods}\n----------------')
    print(vardnica[kods]['name'])
    print(vardnica[kods]['surname'])
    print(vardnica[kods]['phone'])
    print(vardnica[kods]['email'])  