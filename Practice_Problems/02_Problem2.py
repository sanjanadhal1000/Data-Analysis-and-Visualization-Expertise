'''
Q2. A bag has 5 red, 3 blue balls. One is drawn and found to be blue.

Find P(next is red).

'''

# Q2: Conditional probability

red = 5
blue = 3

# One blue is drawn
blue -= 1
total = red + blue

P_next_red = red / total
print(f"Probability next is red = {P_next_red:.3f}")
