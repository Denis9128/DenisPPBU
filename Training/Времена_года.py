s = input("Введите время года: ")
s = s.lower() # Перевод в нижний регистр
if s=="лето":
    print(f"{s.capitalize()} - жара")
elif s=="осень":
    print(f"{s.capitalize()} - дожди")
elif s=="зима":
    print(f"{s.capitalize()} - дубак")
elif s=="весна":
    print(f"{s.capitalize()} - слякоть")
else:
    print(f'{s} - не время года')