import os

cook_book = {}
with open(r'D:\Netology\Openfile\recipes.txt', encoding='utf-8') as file:
    for _line in file:
            dish = _line.strip() 
            ingredients_quant = int(file.readline().strip())
            dish_dict = [] 
            for item in range(ingredients_quant):
                ingredient_name, quantity, unit = file.readline().strip().split('|')
                dish_dict.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': unit})
            cook_book[dish] = dish_dict
            file.readline() 
# print(cook_book)       

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingridient in cook_book[dish]:
            new_shop_list_item = dict(ingridient)
            new_shop_list_item['quantity'] *= person_count
            if new_shop_list_item['ingredient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingredient_name']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingredient_name']]['quantity'] += new_shop_list_item['quantity']
    return shop_list
        
# print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))


list_file = [elem for elem in os.listdir(path='D:\\Netology\\Openfile\\text') if elem.endswith('txt') and elem[0].isdigit()]

my_dict_len = {}
my_dict_text = {}

for stroke in list_file:
    file_slash = os.path.join('D:\\Netology\\Openfile\\text', stroke)
    with open(file_slash, 'r', encoding='utf-8') as file_in:
        read_file = file_in.read().splitlines()
        my_dict_len[str(stroke)] = len(read_file)
        my_dict_text[str(stroke)] = '\n'.join(read_file)
    
my_dict_len = {key: value for key, value in sorted(my_dict_len.items(), key=lambda x: x[1])}

with open('D:\\Netology\\Openfile\\text\\file_out.txt', 'w', encoding='utf-8') as file_out:
    for stroke in my_dict_len:
        print(f'Имя файла: {stroke}', file=file_out)
        print(f'Количество строк: {my_dict_len[stroke]}', file=file_out)
        print(my_dict_text[stroke], file=file_out)
        print(file=file_out)