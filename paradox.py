import datetime, random

def getBirthdays(numberOfBirthdays):

    birthdays = []
    numberOfBirthdays = int(numberOfBirthdays)

    for i in range(numberOfBirthdays):
        startOfYear = datetime.date(2001, 1, 1)
        randomNumberOfDays = datetime.timedelta(random.randint(0, 394))
        birthday = startOfYear + randomNumberOfDays

        birthdays.append(birthday)
    return birthdays 

def getMatchBirthdays(birthdays):
    if len(birthdays) == len(set(birthdays)):
        return None

    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a + 1 :]):
            if birthdayA == birthdayB:
                return birthdayA
        

#Display intro
print("Birthday Paradox")

MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

while True:
    print('How many birthdays shall I generate (Max 100)')
    response = input('> ')
    if response.isdecimal() and (0 < int(response) <= 100):
        numBDays = response
        break

print()

print('Here are', numBDays, 'birthdays:')
birthdays = getBirthdays(numBDays)
for i, birthday in enumerate(birthdays):
    
    if i != 0:
        print(', ', end='')
        monthName = MONTHS[birthday.month - 1]
        dateText = '{} {}'.format(monthName, birthday.day)
        print(dateText, end='')

print()
print()

match = getMatchBirthdays(birthdays)

print("In this simulation", end='')

if match != None:
    monthName = MONTHS[match.month - 1]
    dateText = '{} {}'.format(monthName, match.day)

    print(' multiple people have a birthday on', dateText)

else:
    print(' there are no matching birthdays.')
print()    



