#saraksta izveidošana
saraksts_ar_skaitliem = [1, 2, 3, 4, 5]
saraksts = ['bread', 'apples', 'milk', 'bananas']

#saraksta elementu izvade
counter = 1
for produkts in saraksts:
    print(f"Produkts {counter}:")
    print(f"{produkts}")
    counter += 1

#vārdnīcas izveidošana
vardnica = {'1234':{'name': 'Anna', 'phone': '2346578'},
            '9874':{'name': 'Mik', 'phone': '99547856'},
            '5555':{'name': 'Jenifer', 'phone': '124569877'}
}

#vārdnicas elementu izvade
print(vardnica['9874']['phone'])

for key in vardnica:
    print("\n---------------------")
    print(f"Personas kods: {key}")
    print(f"Vārds: {vardnica[key]['name']}")
    print(f"Tālrunis: {vardnica[key]['phone']}")