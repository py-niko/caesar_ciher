# На вход программе подается строка текста на английском языке, в которой нужно зашифровать все слова. Каждое слово строки следует зашифровать с помощью шифра
# Цезаря (циклического сдвига на длину этого слова). Строчные буквы при этом остаются строчными, а прописные – прописными.
s = input().split()
result = []
for i in s:
    key = len(i)
    result.append(' ')
    for j in range(key):
        if  i[j].isalpha() == True and i[j].isupper() == True:
            if (ord(i[j]) + key) > 90:
                result.append(chr(ord(i[j]) + key - 26))
            else:
                result.append(chr(ord(i[j]) + key))

        if i[j].isalpha() == True and i[j].islower() == True:
            if (ord(i[j]) + key) > 122:
                result.append(chr(ord(i[j]) + key - 26))
            else:
                result.append(chr(ord(i[j]) + key))
del result[0]
print(''.join(result))






