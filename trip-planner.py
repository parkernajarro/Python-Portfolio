prices = 0
amount = 0
hotel = 0
hotel_prices = 0
total_no_hotel = 0
prices = int(prices)
amount = int(amount)
total_no_hotel = str(total_no_hotel)
hotel_options = 'weston, marriot, or sheraton'


# Asks for City and stores values to city
def ticket_cost():                               
    global prices
    city = input('What city are you looking for? (Choose from Los Angeles, Chicago, or New York) ').lower()
    if city == 'los angeles':
        prices = 55
    elif city == 'chicago':
        prices = 45
    elif city == 'new york':
        prices = 55
    else:
        print("No tickets are available in the inputted city")
        prices == 0

# Asks for ticket quantity
def quantity():                               
    global amount
    amount = int(input('How many tickets are you looking for? (Enter a number between 1 and 6) '))
    if amount in range(1,7):
        print('You have selected {} tickets '.format(amount))
    elif amount == (0):
        print('You have selected 0 tickets')
    else:
        print('Please choose an amount between 1-6')

# Asks user if they wish to book a hotel
def hotel_stay():                               
    hotel = input('Will you be needing a hotel? Y/N: ').lower()
    if hotel == ('y'):
        print('Here are your options: {}'.format(hotel_options))
    else:
        print('Your total is ${}'.format(total_no_hotel))
        input("press any key to exit")

# Prompts user to select hotel and stores price to each hotel
def hotel_choice():
    global hotel_prices                               
    hotel_selection = input('Which hotel would you like to stay at? ').lower()
    if hotel_selection == 'weston':
        hotel_prices = 125
    elif hotel_selection == 'marriot':
        hotel_prices = 130
    elif hotel_selection == 'sheraton':
        hotel_prices = 135
    else:
        print('Please choose from the shown options')
        hotel_prices = 0

ticket_cost()
quantity()
hotel_stay()
hotel_choice()

# Calculates prices for respective hotel costs
hotel_prices = int(hotel_prices)
total_no_hotel = prices * amount

# Calculate total cost
total = (prices * amount) + hotel_prices
total = str(total)

if amount in range(1,7):
    print('Your total is $'+total)
else:
    print('Sorry, try again')
