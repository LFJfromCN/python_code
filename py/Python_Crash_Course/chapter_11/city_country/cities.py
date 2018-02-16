from city_function import city_country

print("Enter 'q' at any time to quit.")
while True:
    city = input("\nPlease give me a city's name: ")
    if city == 'q':
        break
    country = input("Please give me a country's name which matches the city you just input: ")
    if country == 'q':
        break
    city_c = city_country(city, country)

    print(city_c)
