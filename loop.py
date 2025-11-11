import random
rolls = [random.randint(1, 6) for _ in range(20)]
print("Dice rolls:", rolls)
count_6 = rolls.count(6)
count_1 = rolls.count(1)
count_double_6 = sum(1 for i in range(len(rolls)-1) if rolls[i] == rolls[i+1] == 6)
print("Number of 6s:", count_6)
print("Number of 1s:", count_1)
print("Number of double 6s in a row:", count_double_6)
total_jacks = 100
done = 0
while done < total_jacks:
    done += 10
    print(f"You completed {done} jumping jacks.")
    if done < total_jacks:
        tired = input("Are you tired?")  
        if tired.lower() in ["yes", "y"]:
            print(f"You completed a total of {done} jumping jacks.")
            break
        else:
            print(f"{total_jacks - done} jumping jacks remaining.")
else:
    print("Congratulations! You completed the workout!")

