cities = ["New York", "London", "Paris", "Tokyo", "Sydney"]

print("The original list of cities:")
for city in cities:
    print(city)

new_city = input("Enter a city name to append to the list: ")
cities.append(new_city)

del_city = input("Enter a city name to delete from the list: ")
try:
    cities.remove(del_city)
except ValueError:
    print(f"{del_city} not found in the list.")
    
print("The list of cities after changes:")
for city in cities:
    print(city)