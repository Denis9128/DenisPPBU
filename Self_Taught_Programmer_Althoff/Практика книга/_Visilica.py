import random


def fil_vis(filename):
    with open(filename, encoding='utf-8') as f:
        file_slov = f.readlines()
        rez = random.choice(file_slov).strip()
        return  rez


def hangman(word):
    wrong = 0
    stages = ["",
               "________   ",
               "|      |   ",
               "|      |   ",
               "|      0   ",
               "|     /|\  ",
               "|     / \  ",
               "|          "
              ]
    rletters = list(word)
    board = ["__"] * len(word)

    win = False
    print("Добро пожаловать на казнь!")

    while wrong < len(stages) - 1:
        print("\n")

        msg = "Введите букву: "
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0: e]))
        if "__" not in board:
            print("Вы выиграли. было загадано слово: ")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0: wrong]))
        print("Вы проиграли. Было загадано слово: {}.".format(word))


hangman(fil_vis('visil.txt'))