def book_seat (seats):
    set_name = input(f"Введите место для бронирования (от Б1 до Б9): ").title() # Первый символ с большой буквы
    try:
        i = seats.index([set_name, "Свободно"])
        seats[i] [1]= "Забронировано"
        print(f"Место {set_name}успешно забронировано")
    except ValueError:
        print(f"Место {set_name} забронировано или не существует")
        # Проверка на любую ошибку
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")


seats = [[f"Б{i}","Свободно"] for i in range(1,10)]
print(seats)


while True:
    book_seat(seats)
    booking = input("Хотите забронировать еще одно место? (да/нет): ").lower()
    if booking == "да":
        print("Итоговое состояние мест. ")
        for seat in seats:
            print(f"{seat[0]}: {seat[1]}")
    else:
        break

print("Итоговое состояние мест. ")
for seat in seats:
    print(f"{seat[0]}: {seat[1]}")

