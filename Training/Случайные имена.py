import random
name = ["Маша","Даша","Саша","Глаша","Паша"]
job = ["строитель","курьер","доктор",
       "таксист","грузчик","космонавт"]
rnd = random.randint(0,4)
age = random.randint(5,25)
rnd_job = random.randint(0,5)
print(f'Меня зовут {name[rnd]}, мне {age} лет, я {job[rnd_job]}.')