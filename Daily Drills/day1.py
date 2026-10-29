"""
Recap from me 

    A list is []
    A dictinoary {key: value}

    Accessing items,    list[0][title] 
    from the list, get the 1 row value at index 0 and key title
"""


pokemon_list = [
    {"name": "Charizard VMAX", "set": "Darkness Ablaze", "number": '020/189', "price": 85},
    {"name": "Pikachu V", "set": "Vivid Voltage", "number": '043/185', "price": 12},
    {"name": "Umbreon VMAX", "set": "Evolving Skies", "number": '215/203', "price": 420},
    {"name": "Snorlax", "set": "Base Se", "number": '11/102', "price": 35},
    {"name": "Rayquaza VMAX", "set": "Evolving Skies", "number": '111/203', "price": 60}
]

#print every card name 

for card in pokemon_list: 
    print(card['name'])

#card over 50 

over_50 = [card for card in pokemon_list if card['price'] > 50]
print(over_50)


#build a list of just name using compre

names = [card['name'] for card in pokemon_list]
print(names)
# this one i dont quite rememmber 

#finding the most expensive 

#lets try getting the most expeisive card first

current_max = 0 
max_card_name = ''
for card in pokemon_list: 
    if card['price'] > current_max:
        current_max = card['price']
        max_card_name = card['name']
print(current_max)

print(max_card_name)


def card_over(cards, price): 
    #output card, 
    over_50 = [card for card in cards if card['price'] > price]
    return over_50

expensive_card = card_over(pokemon_list, 50)
print(expensive_card)
