friends = ["Aishwarya", "Keerthi", "Swathi", "Uma", "Jaswini"]
friends_length = [(name, len(name)) for name in friends]
print("Friends and name lengths:", friends_length)

my_expenses = {"Hotel": 1200, "Food": 800, "Transportation": 500, "Attractions": 300, "Miscellaneous": 200}
partner_expenses = {"Hotel": 1000, "Food": 900, "Transportation": 600, "Attractions": 400, "Miscellaneous": 150}

my_total = sum(my_expenses.values())
partner_total = sum(partner_expenses.values())

print("My total expenses:", my_total)
print("Partner's total expenses:", partner_total)
if my_total > partner_total:
    print("You spent more overall.")
else:
    print("Your partner spent more overall.")

# Find category with max difference
diffs = {k: abs(my_expenses[k] - partner_expenses[k]) for k in my_expenses}
max_diff_category = max(diffs, key=diffs.get)
print(f"Biggest spending difference: {max_diff_category}, Difference = {diffs[max_diff_category]}")
