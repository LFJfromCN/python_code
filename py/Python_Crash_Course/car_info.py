def car_info(maker, model, **info):
    informations = { }
    informations['aotumaker'] = maker.title()
    informations['car_model'] = model
    for key, value in info.items():
        informations[key] = value
    return informations

info = car_info('benz', '3000',
                            price = '$30000',
                            color = 'red')
print(info)

new_info = car_info('subaru', 'outback',
                                    color = 'blue',
                                    tow_package = True)
print(new_info)
