def car_info(maker, model, **info):
    informations = { }
    informations['aotumaker'] = maker.title()
    informations['car_model'] = model
    for key, value in info.items():
        informations[key] = value
    return informations
