import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))


for city in cities[:5]:
    print(city)


print("The average temperature of all the cities:")
temps = []
for city in cities:
    temps.append(float(city['temperature']))
print(sum(temps)/len(temps))
print()


print("The average temperature of all the cities:")
temps = [float(city['temperature']) for city in cities]
print(sum(temps)/len(temps))
print()


print("All cities in Germany:")
All = []
Germany = filter(lambda city: city["country"] == "Germany", cities)
for city in Germany:
    All.append(city["city"])
print(All)
print()


print("All cities in Spain with a temperature above 12°C")
All = []
Spain = filter(lambda city: city["country"] == "Spain" and float(city["temperature"]) > 12, cities)
for city in Spain:
    All.append(city["city"])
print(All)
print()


print("Number of unique countries")
unique = []
count = 0
All = list(map(lambda city: city["country"], cities))
for country in All:
    if country not in unique:
        unique.append(country)
for _ in unique:
    count += 1
print(count)
print()


print("The average temperature for all the cities in Germany")
Avg = list(filter(lambda city: city["country"] == "Germany", cities))
total = 0
count = 0 
for city in Avg:
    total += float(city["temperature"])
    count += 1
average = total / count
print(average)
print()


print("The max temperature for all the cities in Italy")
Italy = filter(lambda city: city["country"] == "Italy", cities)
max_temp = max(Italy, key = lambda city: float(city["temperature"]))
print(float(max_temp["temperature"]))
print()