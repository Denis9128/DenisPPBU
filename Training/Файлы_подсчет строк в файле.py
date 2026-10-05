def analyze_log (filename):
    counter = {"09/17 10:38:40":0, "ERROR":0, "WARNING":0}
    try:
        with open(filename) as file:
            for line in file:
                if "[09/17 10:38:40]" in line:
                    counter["09/17 10:38:40"] += 1
                elif "[ERROR]" in line:
                    counter["ERROR"] += 1
                elif "[WARNING]" in line:
                    counter["WARNING"] += 1
        for k,v in counter.items():
            print(f"{k}: {v}")

    except FileNotFoundError:
        print(f"Фаил {filename} не найден")
    except Exception as e:
        print(f"Неизвестная ошибка {e}")

analyze_log('log.txt')


