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

tests.append({'input': {
                    'cards':[9, 7, 5, 2, -9], 
                    'query': 4
                  }, 
              'output': -1
        })     



def locate_card(cards, query):
    pass

print(locate_card(**test['input']) == test['output'])

