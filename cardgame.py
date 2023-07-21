
# Edge Case Container
tests = []

test = {
    'input': {
            'cards': [13, 11, 10, 7, 4, 3, 1, 0],
            'query': 7
    },
    'output': 3
}

tests.append(test)


# query appears in the middle
tests.append({'input': {
                    'cards':[13, 11, 10, 7, 4, 3, 1, 0], 
                    'query': 1
                  }, 
              'output': 6
        })

# query is the first element
tests.append({'input': {
                    'cards':[4, 2, 1, -1], 
                    'query': 4
                  }, 
              'output': 0
        })

#query is the last element
tests.append({'input': {
                    'cards':[3, -1, -9, -127], 
                    'query': -127
                  }, 
              'output': 3
        })

# cards contains just one element
tests.append({'input': {
                    'cards':[6], 
                    'query': 6
                  }, 
              'output': 0
        })   

# cards does not contain query
tests.append({'input': {
                    'cards':[9, 7, 5, 2, -9], 
                    'query': 4
                  }, 
              'output': -1 
        })

# cards is empty
tests.append({'input': {
                    'cards':[], 
                    'query': 7
                  }, 
              'output': -1
        })  

# numbers can repeat in cards
tests.append({'input': {
                    'cards':[8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0], 
                    'query': 3
                  }, 
              'output': 7
        })   

# query occurs multiple times
tests.append({'input': {
                    'cards':[8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0], 
                    'query': 6
                  }, 
              'output': 2
        })

def linear_locate_card(cards, query):
    # Create a variable position with the value 0
    position = 0
    
    # Setup a loop to cycle through our cards list
    # Loop initates as long as the array has values
    while position < len(cards):
        
        # Check if our element at current position matches the query value
        if cards[position] == query:
            
            # Answer found, return the position at which we found it
            return position
        
        # Increment the position
        position += 1

        # Check if we have reached the end of the array
        if position == len(cards):
            
            # Our Query number was not found
            return -1

#print(linear_locate_card(test['input']['cards'], test['input']['query']))

def find_middle_card(cards):
    if len(cards) == 0:
        return "The Array is Empty"
    
    middle_pos = float(len(cards)) / 2

    if middle_pos % 2 != 0:
        return cards[int(middle_pos - .5)]
    else:
        return (cards[int(middle_pos)], cards[int(middle_pos-1)]) 


def binary_locate_card(cards, query):
    
    
    pass

#print(len(test['input']['cards']))
#print(find_middle_card(test['input']['cards']))

print(tests)