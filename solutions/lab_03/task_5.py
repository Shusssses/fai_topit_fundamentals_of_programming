def mean(values: list[float]) -> float:
    """Возвращает среднее арифметическое списка. Пустой список → 0.0."""
    if not values:
        return 0.0
    total = 0.0
    for v in values:
        total += v
    return total / len(values)

def minimum(values: list[float]) -> float:
    """Возвращает минимальное значение списка. Пустой список → None."""
    if not values:
        return None
    min_val = values[0]
    for v in values[1:]:
        if v < min_val:
            min_val = v
    return min_val

def maximum(values: list[float]) -> float:
    """Возвращает максимальное значение списка. Пустой список → None."""
    if not values:
        return None
    max_val = values[0]
    for v in values[1:]:
        if v > max_val:
            max_val = v
    return max_val

def classify(score: float) -> str:
    """Возвращает текстовую категорию результата по среднему баллу."""
    if score >= 90:
        return "отличный"
    elif score >= 75:
        return "хороший"
    elif score >= 60:
        return "удовлетворительный"
    else:
        return "недостаточный"

def student_summary(name: str, results: list[int]) -> dict:
    """Возвращает словарь с итогами одного студента.
    Правило для пустого списка: числовые поля = None, категория = 'нет данных'.
    """
    if not results:
        return {
            "name": name,
            "mean": None,
            "min": None,
            "max": None,
            "category": "нет данных",
        }
    return {
        "name": name,
        "mean": mean(results),
        "min": minimum(results),
        "max": maximum(results),
        "category": classify(mean(results)),
    }


def find_top_students(students: dict) -> list[str]:
    """Возвращает список студентов с наибольшим средним результатом.
    Не изменяет исходный словарь. Студенты без результатов игнорируются.
    """
    if not students:
        return []

    # Считаем средние только для студентов с результатами
    student_means = {}
    for name, results in students.items():
        if results:
            student_means[name] = mean(results)

    if not student_means:
        return []

    # Находим максимальное среднее без max()
    max_mean = None
    for v in student_means.values():
        if max_mean is None or v > max_mean:
            max_mean = v

    # Собираем всех лидеров (может быть несколько с одинаковым средним)
    return [name for name, avg in student_means.items() if avg == max_mean]


def group_summary(students: dict) -> dict:
    """Возвращает общую статистику группы.
    Средний по группе считается как среднее арифметическое средних баллов студентов.
    """
    if not students:
        return {
            "total_students": 0,
            "group_mean": None,
            "category_counts": {
                "отличный": 0,
                "хороший": 0,
                "удовлетворительный": 0,
                "недостаточный": 0,
            },
            "top_students": [],
        }
    # Средние баллы по студентам (только у кого есть результаты)
    student_means = {}
    for name, results in students.items():
        if results:
            student_means[name] = mean(results)
    group_mean = mean(list(student_means.values())) if student_means else None   # Средний по группе

    category_counts = {
        "отличный": 0,
        "хороший": 0,
        "удовлетворительный": 0,
        "недостаточный": 0,
    }
    for avg in student_means.values():
        cat = classify(avg)
        category_counts[cat] += 1

    # Топ-студенты
    top_students = find_top_students(students)

    return {
        "total_students": len(students),
        "group_mean": group_mean,
        "category_counts": category_counts,
        "top_students": top_students,
    }


def format_report(student_data: list[dict], group_data: dict) -> str:
    """Формирует итоговый текстовый отчёт."""
    lines = []
    lines.append("ОТЧЁТ ПО УЧЕБНЫМ РЕЗУЛЬТАТАМ")
    lines.append("\n--- Индивидуальные результаты ---")
    for s in student_data:
        if s["mean"] is not None:
            lines.append(
                f"  {s['name']:<10} | средний: {s['mean']:7.2f} "
                f"| мин: {s['min']:5} | макс: {s['max']:5} "
                f"| {s['category']}"
            )
        else:
            lines.append(f"  {s['name']:<10} | нет данных")

    lines.append("\n--- Сводка по группе ---")
    lines.append(f"  Всего студентов: {group_data['total_students']}")
    if group_data["group_mean"] is not None:
        lines.append(f"  Средний по группе: {group_data['group_mean']:.2f}")
    else:
        lines.append("  Средний по группе: нет данных")

    lines.append("\n  Распределение по категориям:")
    for cat, count in group_data["category_counts"].items():
        lines.append(f"    {cat:<20}: {count}")

    top = group_data["top_students"]
    lines.append(f"\n  Лидеры: {', '.join(top) if top else 'нет'}")
    return "\n".join(lines)

def run_scenario(name, students_dict):
    print(f"\n{'-'*55}")
    print(f"СЦЕНАРИЙ: {name}")
    print(f"Входные данные: {students_dict}")
    student_data = []
    for name_s, results in students_dict.items():
        student_data.append(student_summary(name_s, results))
    group_data = group_summary(students_dict)
    print(format_report(student_data, group_data))

students = {
    "Анна": [78, 91, 84, 88],
    "Борис": [60, 72, 68],
    "Дарья": [95, 93, 97, 90],
    "Илья": [55, 61],
}

run_scenario("Обычный набор данных", students)

run_scenario("Один студент", {"Анна": [85, 90, 95]})

run_scenario("Несколько лидеров", {
    "Анна": [90, 90, 90],   # среднее 90
    "Борис": [80, 100, 90],  # среднее 90
    "Дарья": [70, 70, 70],   # среднее 70
})

run_scenario("Пустая группа", {})

run_scenario("Студент без результатов", {
    "Анна": [80, 90],
    "Борис": [],             # пустой список
    "Дарья": [95, 100],
})

run_scenario("Граничные значения категорий", {
    "Отличник": [90],         # ровно 90 -> отличный
    "Хорошист": [75],         # ровно 75 -> хороший
    "Удовл": [60],            # ровно 60 -> удовлетворительный
    "Неуд": [59],             # ровно 59 -> недостаточный
    "Макс": [100],            # максимум
    "Мин": [0],               # минимум
})