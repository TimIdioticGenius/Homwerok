def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)
print_params()
print_params(8)
print_params(2,'asdads')
print_params(True,'real',str)
value_list = [True, 148, 'a']
value_dict = {'true': True, '148': 'a', 'a': 148} #функция отказывается принимать словарь по неизвестным мне причинам
#print_params(*value_list, **value_dict)
value_list2=[False,'a']
print_params(*value_list2,42)