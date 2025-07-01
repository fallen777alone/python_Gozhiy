#{В магазинах имеются следующие товары. Магнит - молоко, соль, сахар.
#Пятерочка - мясо, молоко, сыр. Прекресток - молоко, творог, сыр, сахар. Определить:
#1. полный список всех товаров.
#2. в каких магазинах можно приобрести одновременно молоко и сыр.
#3. в каких магазинах можно приобрести сахар.
Magnit= {'молоко', 'соль', 'сахар'}
Pyaterochka = {'мясо', 'молоко', 'сыр'}
Perekrestok = {'молоко', 'творог','сыр', 'сахар'}
print("1.Полный список товаров: ", Magnit | Pyaterochka | Perekrestok,
      '\nВсего товаров:', str(len(Magnit) + len(Pyaterochka) + len(Perekrestok)))
milk_and_cheese = [store for store in [Magnit, Pyaterochka, Perekrestok] if "молоко" in store and "сыр" in store]
print("Магазины, где можно приобрести одновременно молоко и сыр (Пятерочка и Перекресток):", milk_and_cheese)
sugar = [store for store in [Magnit, Pyaterochka, Perekrestok] if 'сахар' in store]
print('Магазины, где можно приобрести сахар ( Магнит и Перекресток):', sugar)



