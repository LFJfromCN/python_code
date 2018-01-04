def print_models(unprinted_designs, completed_models):
    '''
    模拟打印每个设计，直到没有未打印的设计为止
    打印每个设计后，都将其转移到列表completed_models中
    '''

    while unprinted_designs:
        current_design = unprinted_designs.pop()
        #模拟根据设计制作3D打印模型的过程
        print('Printing model: ' + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    '''显示已经打印好的所有模型'''
    print('\nThe following models have been printed: ')
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['iphone case','robot pendant','dodecahedron','model_car']
completed_models = [ ]

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

##print('\n下面的这种函数调用方式禁止函数修改列表，只给函数传递一个副本')
##print_models(unprinted_designs[ : ],completed_models)
##show_completed_models(completed_models)
##print(unprinted_designs)
