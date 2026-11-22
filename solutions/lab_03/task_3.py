submissions = [
    ("anna", "lab_01", 5),
    ("boris", "lab_01", 4),
    ("anna", "lab_02", 5),
    ("daria", "lab_01", 3),
    ("boris", "lab_02", 5),
    ("anna", "lab_01", 4),
]

students = {x[0] for x in submissions}
print('Множество всех студентов:', students)

labs = {x[1] for x in submissions}
print('Множество всех сданных работ:', labs)

stud_attempts = {}
for name, lab, score in submissions:
    if name not in stud_attempts:
        stud_attempts[name] = []
    stud_attempts[name].append((lab, score))
print("Попытки студентов:")
for name in sorted(stud_attempts):
    print(f"  {name:<8} {stud_attempts[name]}")

best_res = {}
for name, lab, score in submissions:
    key = (name, lab)
    if (key not in best_res) or (score > best_res[key]):
        best_res[key] =  score
print('Лучшие результаты:')
for key in sorted(best_res):
    print(f'{key} {best_res[key]}')

num_attempts = {}
for name, lab, score in submissions:
    key = (name, lab)
    num_attempts[key] = num_attempts.get(key, 0) + 1
print('Количество попыток:')
for key in sorted(num_attempts):
    print(f'{key} {num_attempts[key]}')

lab1 = {name for name, lab, score in submissions if lab == 'lab_01'}
lab2 = {name for name, lab, score in submissions if lab == 'lab_02'}
both = lab1 and lab2
print('Обе работы сдавали:', both)

print('----------------------------------------------')
print("Добавляем новую запись: ('daria', 'lab_02', 4)")
new_record = ("daria", "lab_02", 4)
name, lab, score = new_record

students.add(name)
labs.add(lab)
stud_attempts.setdefault(name, []).append((lab, score))
key = (name, lab)

if key not in best_res or score > best_res[key]:
    best_res[key] = score
num_attempts[key] = num_attempts.get(key, 0) + 1

print("Обновлённые попытки daria:", stud_attempts["daria"])
print("Лучший результат daria/lab_02:", best_res[("daria", "lab_02")])
print("Попыток daria/lab_02:", num_attempts[("daria", "lab_02")])

#==================ПРАКТИЧЕСКОЕ РАСШИРЕНИЕ==================
print('\n=============ПРАКТИЧЕСКОЕ РАСШИРЕНИЕ================')
demo_commands = [
    "student anna",
    "best anna lab_01",
    "attempts boris lab_02",
    "completed lab_01",
    "student ivan",          # неизвестный студент
    "best anna lab_67",      # несуществующая лабораторная
    "unknown command",       # неизвестная команда
    "student",               # недостаточно аргументов
]
for cmd in demo_commands:
    print(cmd)
    parts = cmd.split()

    match parts:
        case ["student", name]:
            if name in stud_attempts:
                print(f"  Попытки {name}: {stud_attempts[name]}")
            else:
                print(f"  Студент '{name}' не найден")

        case ["best", name, lab]:
            key = (name, lab)
            if key in best_res:
                print(f"  Лучший результат {name}/{lab}: {best_res[key]}")
            else:
                print(f"  Нет данных для {name}/{lab}")

        case ["attempts", name, lab]:
            key = (name, lab)
            if key in num_attempts:
                print(f"  Попыток {name}/{lab}: {num_attempts[key]}")
            else:
                print(f"  Нет данных для {name}/{lab}")

        case ["completed", lab]:
            who = sorted({name for name, l, _ in submissions if l == lab})
            if who:
                print(f"  Сдавали {lab}: {who}")
            else:
                print(f"  Лабораторную {lab} никто не сдавал")

        case _:
            print("  Неизвестная команда или неверный формат")