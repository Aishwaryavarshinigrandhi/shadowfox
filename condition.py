height = float(input("Enter height in meters:"))
weight = float(input("Enter weight in kilograms:"))
bmi = weight / (height ** 2)
if bmi >= 30:
    print("Obesity")
elif bmi >= 25:
    print("Overweight")
elif bmi >= 18.5:
    print("Normal")
else:
    print("Underweight")


Australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

city = input("Enter a city name:")
if city in Australia:
    print(f"{city} is in Australia")
elif city in UAE:
    print(f"{city} is in UAE")
elif city in India:
    print(f"{city} is in India")
else:
    print(f"{city} is not in the list")


city1 = input("enter the first city:")
city2 = input("Enter the second city:")

def find_country(c):
    if c in Australia:
        return "Australia"
    elif c in UAE:
        return "UAE"
    elif c in India:
        return "India"
    else:
        return None

country1 = find_country(city1)
country2 = find_country(city2)

if country1 == country2 and country1 is not None:
    print(f"Both cities are in {country1}")
else:
    print("They don't belong to the same country")

