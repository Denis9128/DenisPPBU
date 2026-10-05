color = input("Цвет светофора :")
match color:
    case 'red'|"no":
        print("Стоп")
    case "green":
        print("Go")
    case "yellow":
        print("Ready")
    case _:
        print("Цвет", color)