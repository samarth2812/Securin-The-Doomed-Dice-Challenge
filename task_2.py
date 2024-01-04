Die_A = [1, 2, 3, 4, 5, 6]
Die_B = [1, 2, 3, 4, 5, 6]

print(f"Original Dice A = {Die_A}")
print(f"Original Dice B = {Die_B}")

total_combinations = len(Die_A) * len(Die_B)

original_sums = {}
for i in range(len(Die_A)):
    for j in range(len(Die_B)):
        temp = Die_A[i] + Die_B[j]
        val = original_sums.get(temp, 0) + 1
        original_sums[temp] = val

original_probabilities = {key: val / total_combinations for key, val in original_sums.items()}

print("\nOriginal Probabilities:")
for key, val in original_probabilities.items():
    print(f"P(Sum = {key})  Occurrence = {original_sums[key]}  Probability = {val}")
print("\n")

diceA, diceB = [], []

def find_dice_possibility(number, temp, dice_list, limit):
    if number > limit:
        return
    if len(temp) > 6:
        return

    if len(temp) == 6:
        if temp not in dice_list:
            dice_list.append(temp)
        return

    for i in range(number, limit + 1):
        find_dice_possibility(i, temp.copy() + [i], dice_list, limit)

def undoom_dice():

    diceA, diceB = [], []

    for i in range(1, 5):
        find_dice_possibility(i, [i], diceA, 5)
    for j in range(1, 11):
        find_dice_possibility(j, [j], diceB, 12)

    print("After Undooming Dice A and Dice B")

    for i in diceA:
        for j in diceB:
            temp_dict = {}
            for k in range(len(i)):
                for l in range(len(j)):
                    summation = i[k] + j[l]
                    val = temp_dict.get(summation, 0) + 1
                    temp_dict[summation] = val

            match_count = sum(1 for key, val in temp_dict.items() if val == original_sums.get(key, -1))
            if match_count == 11:
                return i, j, temp_dict

New_Die_A, New_Die_B, tdic = undoom_dice()
print(f"New Dice A -> {New_Die_A}")
print(f"New Dice B -> {New_Die_B}")

print("\nProbability of Dice After Transforming:")
for key, val in tdic.items():
    print(f"P(Sum = {key}) Occurrence ={val}  Probability = {val / total_combinations}")