validation = True
while validation:
    try:
        tickets_count = int(input("Введите количестов билетов "))
        validation = False
    except ValueError:
                print("Некорректный ввод")
total_price = 0
for ticket in range(tickets_count):
    print("это билет ", ticket + 1)
    validation = True
    while validation:
        try:
            age = int(input("Введите ваш возраст "))
            if 0 <= age < 18:
                total_price = total_price + 0
            elif 18 <= age < 25:
                total_price = total_price + 990
            elif age >= 25:
                total_price = total_price + 1390
            else:
                raise ValueError("Тебе не может быть столько лет")
        except ValueError:
            print("Неправильный возраст")
        else:
            validation = False
            print("Поздравляем с покупкой билета!")
if tickets_count >= 3:
    total_price = total_price * 0.9
print(f"Общая стоимость {total_price}")