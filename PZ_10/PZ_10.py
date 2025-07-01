# Туристические агентства предлагают следующие туры. Вояж – Мексика,Канада,Израиль,
# Италия,США. РейнаТур – Англия,Япония,Канада,ЮАР. Радуга – США,Испания,Швеция,
# Австралия. | & -
# Определить в каких турагенствах можно приобрести туры в Канаду, а в каких в США

Voij = {'Мексика', 'Канада', 'Израиль', 'Италия', 'США'}
ReinaTur = {'Англия', 'Япония', 'Канада', 'ЮАР'}
Raduga = {'США', 'Испания', 'Швеция', 'Австралия'}

canada_agencies = []
if {"Канада"} & Voij:
    canada_agencies.append("Вояж")
if {"Канада"} & ReinaTur:
    canada_agencies.append("РейнаТур")
if {"Канада"} & Raduga:
    canada_agencies.append("Радуга")

all_agencies = {
    "Вояж": Voij,
    "РейнаТур": ReinaTur,
    "Радуга": Raduga,
}

usa_agencies = [name for name, countries in all_agencies.items() if {"США"} | countries == countries]

print("Туры в Канаду можно приобрести в:", ", ".join(canada_agencies))
print("Туры в США можно приобрести в:", ", ".join(usa_agencies))

