from car_info_module import car_info as ci

info = ci('benz', '3000',
                            price = '$30000',
                            color = 'red')
print(info)

new_info = ci('subaru', 'outback',
                                    color = 'blue',
                                    tow_package = True)
print(new_info)
