import car_info_module

info = car_info_module.car_info('benz', '3000',
                            price = '$30000',
                            color = 'red')
print(info)

new_info = car_info_module.car_info('subaru', 'outback',
                                    color = 'blue',
                                    tow_package = True)
print(new_info)
