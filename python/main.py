#main.py

print('===========================')
print('|    Python Calculator    |')
print('===========================')
print('+ Tambah x Kali % bagi - Kurang')

command = input('hanya bisa +-%x : ')

#pengurangan

if command == '-':
    kurang1 = input('berapa: ')
    dikurangi = input('- ')
    print(int(kurang1) - int(dikurangi))

#penambahan

if command == '+':
    tambah1 = input('berapa: ')
    ditambah = input('+ ')
    print(int(tambah1) + int(ditambah))

#pembagian

if command == '%':
    bagi = input('berapa: ')
    dibagi = input('% ')
    print(int(bagi) / int(dibagi))

#perkalian

if command == 'x':
    kali = input('berapa: ')
    dikali = input('x ')
    print(int(kali) - int(dikali))