from os import system

def clear():
    _ = system('clear')

# Bill pricing formula

'''   P = F/(1+r(d/365))   '''
A = '$'
F = 1_000_000
d = 90

''' If the price of the bill was 97.45, then 100 - 97.45 = 2.55% per annum. '''

clear()
r = float(input('Enter the price of the bill: '))
r = 100 - r
r = r/100

P = F/(1+r*(d/365))

clear()
print(f'The value of this bill is: {A}{P:,.2f}')