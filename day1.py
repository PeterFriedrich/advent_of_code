# advent of code

turn_list = []

# take in input
with open('test_input.txt', 'r') as file:
    
    # add to list, strip, make int
    for line in file:
        temp = line.strip()
        if temp[0] == "L":
            temp = int(temp[1:]) * -1
        else:
            temp = int(temp[1:])
        turn_list.append(temp)

# sanitize numbers with modulus


print(turn_list)
