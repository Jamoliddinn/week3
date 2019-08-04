word = input ('Enter the pharse: ')
# # return the vowels used in the pharse
vowels = ['e', 'u', 'i', 'o', 'a']

# result = []

# for letter in word:
#     if letter in vowels:
#         result.append(letter)

# print(result)
# print(''.join(result))

#solution using dictionary 
# # # result2 = {'e':0, 'u':0, 'i':0, 'o':0, 'a':0}
# # # for letter in word:
# # #     if letter in vowels:
# # #         result2[letter] += 1
# # # print(result2)

# # # for key, value in result2.items():
# # #     print(f'{key} was found {value} times')


# # result2 = {'e':0, 'u':0, 'i':0, 'o':0, 'a':0}
# # for letter in word:
# #     if letter in vowels:
# #         result2.setdefault(letter, 0)
# #         result2[letter] += 1
# # print(result2)

# # for key, value in result2.items():
# #     print(f'{key} was found {value} times')

pharse = input('Print message: ')
phrase = len(pharse)
print(pharse)
print(f'you have {len(pharse)} characters. ')

# count the consonanat in the phrase
result2 = {}
for letter in word:
    if letter not in vowels:
        result2.setdefault(letter, 0)
        result2[letter] += 1
print(result2)

for key, value in result2.items():
    print(f'{key} was found {value} times')