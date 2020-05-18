import random


def dice_roller(die_value, side_value):
    minimum_dice_value = 1
    minimum_side_value = 3
    if die_value < minimum_dice_value or side_value < minimum_dice_value:
        return "Invalid arguments."
    else:
        results = []
        for x in range(die_value):
            results.append(random.randint(1, side_value))
        return results


print(dice_roller(int(input("Enter a die value: \n")), int(input("Enter a side value: "))))
