# Зашифруйте текст "Блажен, кто верует, тепло ему на свете!" алгоритмом Цезаря с сдвигом вправо на 1010 символов.
# Примечание. Считайте, что русский алфавит состоит из 3232 букв (буква ё отсутствует).
#  1040 ('А') по 1071 ('Я'), 1072 ('а') по 1103 ('я').

s = 'Sgd fqzrr hr zkvzxr fqddmdq nm sgd nsgdq rhcd ne sgd edmbd.'
key = -25
s_caeser = ''

for i in s:
    if i.isalpha() == True:
        if i == i.upper(): # большие буквы
            i = ord(i) + key
            if i < 65:
                i = chr(i + 26)
                s_caeser += i
            else:
                s_caeser += chr(i)

        elif i == i.lower():  # маленькие буквы
            i = ord(i) + key
            if i < 97:
                i = chr(i + 26)
                s_caeser += i
            else:
                s_caeser += chr(i)

    else:
        s_caeser += i

print(s_caeser) #Лхкрпч, фьш мпъэпь, ьпщхш пцэ чк ымпьп!
#Лхкрпч, фьш мпъэпь, ьпщхш пцэ чк ымпьп!

