shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300], ['педаль', 100],
        ['седло', 1500], ['рама', 12000], ['обод', 2000], ['шатун', 200],
        ['седло', 2700]]
materials = input('Название детали: ')
materials = materials.lower()
print()
cost = 0
count = 0
for i_shop in shop:
    if i_shop[0] == materials:
        cost += i_shop[1]
        count += 1
if count == 0:
    print("Товар не найден")
else:
    print(f'Количество деталей: {count}')
    print(f'Общая стоимость: {cost}')
