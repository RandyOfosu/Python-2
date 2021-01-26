cijfers ={1: 'Een', 2: 'Twee', 3: 'Drie', 4: 'Vier', 5: 'Vijf', 6: 'Zes', 7: 'Zeven', 8: 'Acht', 9: 'Negen', 10: 'Tien'}

vraag1 = int(input('Voer een getal in tussen 1 en 10: ')[:2])

while vraag1 > 10:
    vraag1 = int(input('Nee, even serieus. Voer een getal in tussen 1 en 10: ')[:2])
else:
    print(cijfers[vraag1])
