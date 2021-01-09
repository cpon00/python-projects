def investment(value, percentage, time):
    for x in range(1, time + 1):
        value = value * percentage
        print('After' + str(x) + 'year(s): ' + str(value))


def broker():
    print('Hello, welcome to the investment calculator!')
    investment_type = input('Which type of investment would you like to make savings/CD/mutual funds/bonds)?')
    value = float(input('How much would you like to invest?'))
    if investment_type == 'savings':
        investment(value, 1.006, 3)
    elif investment_type == 'CD':
        if value >= 2500:
            investment(value, 1.025, 4)
        else:
            investment(value, 1.01, 3)
    elif investment_type == 'mutual funds':
        print('Best Case:')
        investment(value, 1.050, 3)
        print('Worst Case:')
        investment(value, 0.99, 3)
    elif investment_type == 'bonds':
        if value >= 5000:
            investment(value, 1.020, 3)
        else:
            print('ur poor lol')

    else:
        print('invalid type')


broker()
