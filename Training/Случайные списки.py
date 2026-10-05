import random
name = []
job = []
names = int(input("Сколько имён введете ?"))
jobs= int(input("Сколько профессий введете? "))

for i in range(names):
    name.append(input("Введите имя ")) # Добавляем в список name
for i in range(jobs):
    job.append(input("Введите профессию ")) # Добавляем в список job

# print(names)
# print(jobs)

rnd = random.randint(0,names-1)
age = random.randint(5,25)
rnd_job = random.randint(0, jobs-1)
print(f'Меня зовут {name[rnd]}, мне {age} лет, я {job[rnd_job]}.')