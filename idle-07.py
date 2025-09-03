year = int(input('enter a year:'))

if year%4 == 0:
    if year%100 ==0:
        if year%400 ==0:
            print(f'{year} is a leap yaer')
        else:
            print(f'{year} is not a leap yaer')
    else:
        print(f'{year} is a leap yaer')
else:
    print(f'{year} is not a leap yaer')
