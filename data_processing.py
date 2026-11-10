import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))


def filter_items(condition, dict_list):
    result = []
    for item in dict_list:
        if condition(item):
            result.append(item)
    return result


def aggregate(aggregation_key, aggregation_function, dict_list):
    value = []
    for item in dict_list:
        value.append(item[aggregation_key])
    return aggregation_function(value)


for city in cities[:5]:
    print(city)


print("The average temperature of all the cities:")
temps = []
for city in cities:
    temps.append(float(city['temperature']))
print(sum(temps)/len(temps))
print()


print("The average temperature of all the cities:")
print(aggregate("temperature", lambda temp : (sum(map(float, temp))) / len(temp), cities))
print()


print("All cities in Germany:")
Germany = filter_items(lambda x: x["country"] == "Germany", cities)
print(aggregate("city", lambda c: c,Germany))
print()


print("All cities in Spain with a temperature above 12°C")
Spain = filter_items(lambda s: s["country"] == "Spain" and float(s["temperature"]) > 12, cities)
print(aggregate("city", lambda s : s, Spain))
print()


print("Number of unique countries")
unique = []
count = 0
All = aggregate("country", lambda c:c, cities)
for country in All:
    if country not in unique:
        unique.append(country)
for _ in unique:
    count += 1
print(count)
print()


print("The average temperature for all the cities in Germany")
Avg = filter_items(lambda a: a["country"] == "Germany", cities)
print(aggregate("temperature", lambda v: (sum(map(float, v))) / len(v), Avg))
print()


print("The max temperature for all the cities in Italy")
Italy = filter_items(lambda i: i["country"] == "Italy", cities)
print(aggregate("temperature", lambda i: max(map(float, i)), Italy))
print()