import random, sys

JAPANESE_NUMBERS = {1:'ICHI', 2:'NI', 3:'SAN', 4:'SHI', 5: 'GO', 6:'ROKU'}

print("Cho-han")

purse = 5000

while True:
    print('How have', purse, 'mon. How much do you bet? (OR QUIT)')
    while True:
        pot = input('> ')
        if pot.upper() == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        elif not pot.isdecimal():
            print("Please enter a number")
        elif int (pot) > purse:
            print('You do not have enough to make that bet')
        else:
            pot = int (pot)
            break

#Roll the dice
    dice1 = random.randint(1, 6) 
    dice2 = random.randint(1, 6) 

    print('The dealer swirls the cup and slams the cup on the floor. Still covering the dice and asks for your bet.')
    print()
    print('CHO (even) or HAN (odd)?')

    while True:
        bet = input('>').upper()
        if bet != 'CHO' and bet != 'HAN':
            print('Please enter either "CHO" or "HAN".')
            continue
        else:
            break

    print('The dealer lifts the cup to reveal:')
    print(' ', JAPANESE_NUMBERS[dice1], '-', JAPANESE_NUMBERS[dice2])
    print(' ', dice1, '-', dice2)


    rollsEven = (dice1 + dice2) % 2 == 0 
    if rollsEven:
        correctBet = 'CHO'
    else:
        correctBet = 'HAN'

    playerWon  = bet = correctBet

    if playerWon:
        print('You won. You take', pot, 'mon.')
        purse = purse + pot
        print('The house collects', pot // 10, 'mon fee.')
        purse = purse - (pot // 10)
    else:
        print('You lost!')
        purse = purse - pot
    if purse == 0:
        print('You have run out of money')
        print('Thanks for playing!')
        sys.exit()           
           


