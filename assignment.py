# A progam to check whether a year is a leap year
year = 2000


if (year % 4 == 0) and (year % 1 == 0):
    print("{0} is a leap year".format(year))
else:
    print("{0} is not a leap year".format(year))
# A program to check whether a letter is a consonant or a vowel

def isVowel(ch):
    switcher = {
        'a': "Vowel",
        'e': "Vowel",
        'i': "Vowel",
        'o': "Vowel",
        'u': "Vowel",
        'A': "Vowel",
        'E': "Vowel",
        'I': "Vowel",
        'O': "Vowel",
        'U': "Vowel"
    }
    return switcher.get(ch, "Consonant")


print('a is ' + isVowel('a'))
print('x is ' + isVowel('x'))


