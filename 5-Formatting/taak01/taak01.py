# cijfers ={1: 'Een', 2: 'Twee', 3: 'Drie', 4: 'Vier', 5: 'Vijf', 6: 'Zes', 7: 'Zeven', 8: 'Acht', 9: 'Negen', 10: 'Tien'}
#
# vraag1 = int(input('Voer een getal in tussen 1 en 10: ')[:2])
#
# while vraag1 > 10:
#     vraag1 = int(input('Nee, even serieus. Voer een getal in tussen 1 en 10: ')[:2])
# else:
#     print(cijfers[vraag1])
#
#
# print(vraag1, " is voor diegenen die niet weten hoe ze dat moeten spellen: ", cijfers[vraag1],'.', end='\n' "Is dat niet makkelijk?", sep='')

# namen = ['lies', 'jan', 'kees', 'mireille', 'koen', 'rob']
#
# for index, naam in enumerate(namen):
#     print('Nummer {} in de lijst is: {}'.format(index + 1, naam))
#
# #taak 4
# scores = {'lies': 6231, 'bas': 4322, 'kees': 6218, 'mireille':
# 4821, 'aniek': 6435, 'bert': 184, 'genius':10231}
# #print('Spelers:')
# # Methode 1: Alleen de sleutels worden afgedrukt
# for speler in scores:
#  print(speler)
# print()
# print('Scores:')
# # Methode 2: Alleen de waardes worden afgedrukt
# for score in scores.values():
#  print('Spelers met score')
#  print(score)
# print()
# # Methode 3: Zowel de sleutels als hun waardes worden afgedrukt
# for speler, score in scores.items():
#  print('{}: {}'.format(speler, score))

# scores = {'lies': 6231, 'bas': 4322, 'kees': 6218, 'mireille': 4821, 'aniek': 6435, 'bert': 184, 'genius': 10231}
#
# for speler, score in scores.items():
#     print('{:+^12}'.format(speler), '{:0>6}'.format(score))

# tuple_1 = (('Randy', 'Man', '25', 'Amsterdam')
# tuple_2 = ('Quincy', 'Man', '23', 'Amsterdam')
# tuple_3 = ('Maria', 'Vrouw', '55', 'Overrijsel')
# tuple_4 = ('Deborah', 'Vrouw', '32', 'Rotterdam')
# tuple_5 = ('Bob', 'Man', '14', 'Bunschoten-Spakenburg')
# tuple_6 = ('Laura', 'Vrouw', '28', 'Groningen'))

klas9A = (('Randy', 'Man', 25, 'Amsterdam'),\
          ('Quincy', 'Man', 23, 'Amsterdam'),\
          ('Maria', 'Vrouw', 55, 'Overrijsel'),\
          ('Deborah', 'Vrouw', 32, 'Rotterdam'),\
          ('Bob', 'Man', 14, 'Bunschoten-Spakenburg'),\
          ('Laura', 'Vrouw', 28, 'Groningen'))
for namen, geslacht, leeftijd, woonplaats in klas9A:
    if geslacht == 'Man':
        print('Zijn naam is {}, hij is {} leeftijd en woont in {}.'.format(namen, leeftijd, woonplaats))
    else:
        print('Haar naam is {}, zij is {} leeftijd en woont in {}.'.format(namen, leeftijd, woonplaats))