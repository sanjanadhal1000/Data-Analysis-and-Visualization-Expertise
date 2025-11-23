'''
Basic Terms
Events and Types of Events
Conditional Probability
Permutations & Combinations
Coin Toss Simulation (NumPy Code)
Practice Problems

'''

# Basic Probability Terms

'''
Experiment: An action having certain outcomes. For example, tossing a coin, rolling a dice.

Sample Space (S): All possible outcomes. For example, Coin toss - S = {H,T}. Dice Roll - S = {1,2,3,4,5,6}.

Event (E): A subset of S. For example, while rolling a dice, E = Probability of getting an even number = {2,4,6}.

Probability Formula:

        P(E) = Number of favourable outcomes / Total Outcomes.

'''

# Types of Events

'''

Mutually Exclusive Events: Cannot happen at the same time. 
    Example: getting 2 and getting 5 on the same dice in one throw.

Independent Events: One event doesn't affect the other one.
    Example: Toss Con -> Roll a Dice.

Dependent Events: One event changes the probability of the next.
    Example: Drawing 2 cards from a deck without replacement.

'''

# Conditional Probability:

'''
Used when one event has already happened.

Formula: P(A/B) = P(A intersection B) / P(B).

Example: 

A bag has: 3 red, 2 blue balls. You draw one and it is red.
Find probability next ball is red (without replacement).

If one red ball is drawn, then remaining red balls = 2, and blue balls = 2. Total = 4

Probability(Next Ball Red/One Red Ball Removed) = 2/4 = 0.5

'''

# Permutations & Combinations

'''
-------------
Permutation:
--------------

Order matters. 
    nPr = n! / (n-r)!

Example: Arrange three letters: A,B,C - 6 ways (ABC,ACB,BAC,BCA,CAB,CBA).

-------------
Combination:
-------------

Order doesn't matter.
    nCr = n! / r! (n-r)!

Example: Choose 2 students out of 5. 5C2 = 10.
'''

# Coin Toss Simulation in 01_coin_toss_numpy.py

# Practice Problems in Practice_Problems folder.
