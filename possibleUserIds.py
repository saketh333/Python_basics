# creating all possible user id's with a first two places as a letter and last two places as digits

lowercase = 'abcdefghijklmnopqrstuvwxyz'
digits = '0123456789'

answer = [letter1+letter2+num1+num2 for letter1 in lowercase for letter2 in lowercase for num1 in digits for num2 in digits]
