def party():
    print(f'Сейчас на вечеринке {len(guests)} человек: {guests}')
    command = input("Гость пришёл или ушёл? ")
    if command == "пришёл":
        if len(guests) < 6:
            guests.append(input("Имя гостя: "))
            print(f'Привет, {guests[-1]}!')
            party()
        else:
            name = input("Имя гостя: ")
            print(f'Прости, {name}, но мест нет.')
            party()
    elif command == "ушёл":
        name = input("Имя гостя: ")
        guests.remove(name)
        print(f'Пока, {name}!')
        party()
    elif command == "Пора спать":
        pass


guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
party()
print('Вечеринка закончилась, все легли спать.')
