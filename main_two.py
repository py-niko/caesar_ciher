# Шсъцхр щмчжмщ йшм, нмтзж йшм лхшщзщг.
# #  1040 ('А') по 1071 ('Я'), 1072 ('а') по 1103 ('я').
# s = input()
# k = -1
# while k <= 26:
#     k += 1
#     for i in s:
#         if i.isalpha() is True:
#             print(chr((ord(i) + k) % ord('z')), end='')
#         else:
#             print(i, end='')
#     print()


s = 'Hawnj pk swhg xabkna ukq nqj.'


k = - 1
while k <= 25:
    k += 1
    s_caeser = ''
    for i in s:
        if i.isalpha() == True:
            if i == i.upper(): # большие буквы
                i = ord(i) + k
                if i > 90:
                    i = chr(i - 26)
                    s_caeser += i
                else:
                    s_caeser += chr(i)

            elif i == i.lower():  # маленькие буквы
                i = ord(i) + k
                if i > 122:
                    i = chr(i - 26)
                    s_caeser += i

                else:
                    s_caeser += chr(i)

        else:
            s_caeser += i

    print(s_caeser, sep='\n')
