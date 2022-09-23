iphone = input('waarde iphone: ')
samsung = input('waarde samsung: ')

if iphone < samsung:
    print("de goedkoopste telefoon is de iphone het kost :  ",iphone," euro")
    print("de duurste telefoon is de samsung.het kost :  ",samsung," euro")
    print('koop de iphone')
elif samsung < iphone:
    print("de goedkoopste telefoon is de samsung. het kost :  ",samsung," euro")
    print("de duurste telefoon is de iphone het kost :  ",iphone," euro")
    print('koop de samsung')

elif samsung == iphone:
    print('de prijs is gelijk. advies: koop de iphone ')

elif samsung < iphone and iphone < samsung + 50:
    print("de goedkoopste telefoon is de samsung het kost",samsung,"euro")
    print('de iphone kost: ',iphone, "euro")
    print('advies: koop de iphone')


