justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]

print("Members in Justice League:", len(justice_league))

justice_league.extend(["Batgirl", "Nightwing"])
print("After adding new members:", justice_league)

justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print("After moving Wonder Woman to front:", justice_league)

justice_league.remove("Superman")
justice_league.insert(justice_league.index("Flash"), "Superman")
print("After separating Aquaman and Flash:", justice_league)

justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print("New Justice League team:", justice_league)

justice_league.sort()
print("Sorted Justice League:", justice_league)
print("New leader:", justice_league[0])  # BONUS
