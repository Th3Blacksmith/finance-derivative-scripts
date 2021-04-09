from os import system

def clear():
    _ = system('clear')


# Bond pricing formula

'''     P = [(1-1/(1+i)^n)/i]+V/(1+i)^n   '''
A = '$'
C = 3000
n  = 20
V = 100000

''' If the price of the bond was 96.01, then 100 - 96.01 = 3.99% per annum. We need half anual rates, so 3.99/2 gives 1.995% per half year. Therefore i = 1.995 '''

clear()
i = float(input('Enter the price of the bond: '))
i = 100 - i
i = i/2
i = i/100

P = C*((1-(1/(1+i))**n)/i)+V/(1+i)**n

clear()
print(f'The value of this bond is: {A}{P:,.2f}')