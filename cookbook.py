from pprint import pprint

def welcome():
  with open('welcome.txt') as welcome_file:
    print(welcome_file.read())
    read_file()

def read_file():
  with open("recipes.txt") as recipes_book:
      list_of_dishes = list(recipes_book.read().split("\n\n"))
      cook_book = {}
      for dish_lines in list_of_dishes:
          dish_name = dish_lines.split("\n")[0]
          ingredients_list = dish_lines.split("\n")[2:]
          ingredients_list = list(map(lambda x: {'ingredient_name': x.split(" | ")[0],
          'quantity': int(x.split(" | ")[1]),
          'measure': x.split(" | ")[2]},
          ingredients_list))
          cook_book[dish_name] = ingredients_list
  main(cook_book)

def menu(cook_book, what):
  print('У нас есть:')
  for dishes in cook_book:
    print(f'-{dishes}')
  main(cook_book)
  
def i_want(cook_book, what, persons):
  buy = {}
  for name in what:
    ingredients = cook_book.get(name)
    for each in ingredients:
      if each['ingredient_name'] not in buy:
        buy[each['ingredient_name']] = dict(zip(['quantity', 'measure'],
        (int(each.get('quantity')) * persons, each.get('measure'))))
      else:
        buy[each['ingredient_name']]['quantity'] += int(each['quantity']) * persons
  print('Вам необходимы следующие продукты:')
  for dish, ingr in buy.items():
    print(f"- {dish} {ingr['quantity']} {ingr['measure']}.")
  print('\n Приятного аппетита!')
  # pprint(buy)

def check_dish(what, cook_book):
  for name in what: 
    if name == 'Меню':
      menu(cook_book, what)
      return False
    elif name not in cook_book.keys():
      print(f'Блюда "{name}" нет в списке')
      menu(cook_book, what)
      return False

def check_persons():
    persons = input("Введите количество персон: ")
    try:
        int(persons)
        return persons
    except ValueError:
        print("Количество персон введено неверно. Введите число.")
        persons = check_persons()
        return persons

def main(cook_book):
  what = list(map(lambda i: i.capitalize(), input("Что вы хотите приготовить? (Введите названия блюд через запятую, \
либо введите 'Меню' для просмотра доступных рецептов): ").split(', ')))
  if check_dish(what, cook_book) != False:
    persons = int(check_persons())
    i_want(cook_book, what, persons)

if __name__ == "__main__":
  welcome()