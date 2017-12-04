prompt = '\nPlease enter the name of a city you have visited: '
prompt += "\n(Enter 'q' or 'Q' when you are finished.)"

while True:
    city = input(prompt)

    if city == 'q' or city == 'Q':
        break
    else:
        print("I'd love to go to " + city.title() + ' ! ')
