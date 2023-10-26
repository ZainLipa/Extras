# Program of the Day: Dice Roller
import random

def roll_dice(num_dice, num_sides):
    rolls = [random.randint(1, num_sides) for _ in range(num_dice)]
    return rolls

# Example usage: Roll two six-sided dice
num_dice = 2
num_sides = 6

dice_rolls = roll_dice(num_dice, num_sides)
print(f"Rolling {num_dice} {num_sides}-sided dice:")
print("Result:", dice_rolls)
print("Total:", sum(dice_rolls))
