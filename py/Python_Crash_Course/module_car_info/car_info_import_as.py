import car_info_module as cf

info = cf.car_info('benz', '3000',
                            price = '$30000',
                            color = 'red')
print(info)

new_info = cf.car_info('subaru', 'outback',
                                    color = 'blue',
                                    tow_package = True)
print(new_info)
