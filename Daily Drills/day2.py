pokemon_list = [
    {"name": "Charizard VMAX", "set": "Darkness Ablaze", "number": '020/189', "price": 85},
    {"name": "Pikachu V", "set": "Vivid Voltage", "number": '043/185', "price": 12},
    {"name": "Umbreon VMAX", "set": "Evolving Skies", "number": '215/203', "price": 420},
    {"name": "Snorlax", "set": "Base Set", "number": '11/102', "price": 35},
    {"name": "Rayquaza VMAX", "set": "Evolving Skies", "number": '111/203', "price": 60}
]

# return a list of cards above a given price 
def card_over(cards,price): 
    return [card for card in cards if card['price'] > price]

#return a list of just the names 
def card_names(cards):
    return [card['name'] for card in cards]

#return the whle card dict not price
def most_expensive(cards): 
    current_max = 0
    card_expensive = '' 
    for card in cards: 
        if card['price'] > current_max: 
            current_max = card['price']
            card_expensive = card
    return card_expensive 

    

def set_name(cards):
    return {card['set'] for card in cards}

print(card_over(pokemon_list, 50))
print(card_names(pokemon_list))
print(most_expensive(pokemon_list))
print(set_name(pokemon_list))

"""
warm up question: 

No, dont retry. 429 is too many request. If we retry, its gonna be the same error. wait it out for a while, then re-attempt to make a request at a later time. 

2. i am not sure about this 

also github made, but i got stuck at the terminal part 
https://github.com/thitruong1106/pochi_lens
"""

