import math

cards = [7, 5, 4, 4, 3, 2, 1]

def find_card(cards, target, start, end):

    if (start > end):
        return "Value not found"
    
    middle = int(math.floor(start + end) / 2)

    #base case
    if cards[middle] == target:
        return f"Found the target card at {middle}"
    
    if cards[middle] > target:
        find_card(cards, target, start, middle-1)

    if cards[middle] < target:
        find_card(cards, target, start, middle+1)

print(find_card(cards, 1, 0, 6))
    
 
