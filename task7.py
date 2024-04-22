#Работа со списками
my_list = ['apple', 'banana', 'peach', 'orange','coconut', 'kiwi']
print('List: '+ str(my_list))
print('First element: ' + str(my_list[0]))
print('Last element: ' + str(my_list[-1]))
print('Sublist: ' + str(my_list[2:5]))
my_list[2] = 'grape'
print('New list ' + str(my_list))
#Работа со словарем
my_dict = {'apple': 'яблоко', 'banana':'банан', 'peach':'персик', 'orange': 'апельсин'}
print('Dict' + str(my_dict))
my_dict.update({'coconut':'кокос'})
print('New dict' + str(my_dict))