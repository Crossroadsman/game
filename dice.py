import random

### Random functions
'''
random.randrange(a, b, [step]) return a random value from the range a..<b
random.randint(a, b) return a random value from the range a...b
random.choice(seq) return a random element from seq
random.choices(seq, k=n) return n elements from seq
random.shuffle(seq) shuffle the sequence seq in place
random.sample(population, k) return k unique elements from population
'''

class Dice:

    def roll(self, sides=6) -> int:
        return random.randint(1,sides)

    def rolls(self, n=1, sides=6) -> [int]:
        rolls = []
        while len(rolls) < n:
            rolls.append( self.roll(sides=sides) )
        return rolls

    def sum_rolls(self, n=1, sides=6) -> int:
        sum_so_far = 0
        rolls = self.rolls(n=n, sides=sides)
        for element in rolls:
            sum_so_far += element
        return sum_so_far
    
    def coin_flip(heads="heads", tails="tails"):
        result = random.randint(0, 1)
        if result == 0:
            return heads
        if result == 1:
            return tails
    
    def coin_flips(n, heads="heads", tails="tails"):
        flips = []
        while len(flips) < n:
            flips.append( self.coin_flip(heads=heads, tails=tails) )
        return flips


if __name__ == "__main__":
    print("Tests...")
    print("--------")
    print("creating dice object")
    dice = Dice()

    print("~~~ testing roll() ~~~")
    print("no args: should be between 1 and 6")
    print(dice.roll())

    print("~~~ testing rolls() ~~~")
    print("no args: should be between 1 and 6")
    print(dice.rolls())

    n = 2
    print("specified 'n': {}".format(n))
    print(dice.rolls(n=n))

    sides = 20
    print("specified 'sides': {}".format(sides))
    print(dice.rolls(sides=sides))

    n = 4
    sides = 8
    print("specified n: {}, and sides: {}".format(n, sides))
    print(dice.rolls(n=n, sides=sides))

    print("~~~ testing sum_rolls() ~~~")
    print("no args: should be between 1 and 6")
    print(dice.sum_rolls())
    
    n = 3
    print("specified 'n': {}".format(n))
    print(dice.sum_rolls(n=n))

    sides = 12
    print("specified 'sides': {}".format(sides))
    print(dice.sum_rolls(sides=sides))

    n = 5
    sides = 10
    print("specified 'n': {}, and 'sides': {}".format(n, sides))
    print(dice.sum_rolls(n=n, sides=sides))
