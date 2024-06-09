a=0
b=0
c=0
def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)
print_params()
print_params(8)
print_params(2,'asdads')
print_params(True,'real',str)
value_list = [True, 148, 'a']
value_dict = {'a': True, 'b': 'a', 'c': 148}
print_params(*value_list)
print_params(**value_dict)
value_list2=[False,'a']
print_params(*value_list2,42)
