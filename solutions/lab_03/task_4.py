def arithmetic_mean(values: list[float]) -> float:
    """Возвращает среднее арифметическое непустого списка."""
    if not values:
        return 0.0
    su = 0.0
    for v in values:
        su += v
    return su / len(values)


def normalize_name(name: str) -> str:
    """Удаляет лишние пробелы и приводит каждую часть имени к нужному регистру."""
    if not name or not name.strip():
        return ""  # ранний return
    parts = name.split()
    return " ".join(p.capitalize() for p in parts)


def build_report(
    student: str,
    results: list[int],
    *,
    precision: int = 2,
    prefix: str = "Результат",
) -> str:
    """Формирует строковый отчет о результатах студента."""
    if not results:
        return f"{prefix}: {student} — нет данных"
    avg = arithmetic_mean(results)
    return f"{prefix}: {student} — средний балл {avg:.{precision}f}"


def collect_tags(*tags: str, lowercase: bool = True) -> tuple[str, ...]:
    """Возвращает очищенные теги без пустых значений и повторов."""
    seen = set()
    result = []
    for tag in tags:
        if not isinstance(tag, str):
            continue
        cleaned = tag.strip()
        if not cleaned:
            continue
        if lowercase:
            cleaned = cleaned.lower()
        if cleaned not in seen:
            seen.add(cleaned)
            result.append(cleaned)
    return tuple(result)

#assert проверки
assert arithmetic_mean([10, 20, 30]) == 20.0
assert arithmetic_mean([5]) == 5.0
assert arithmetic_mean([]) == 0.0

assert normalize_name("  анна   ивановна  ") == "Анна Ивановна"
assert normalize_name("   ") == ""
assert normalize_name("ДАРЬЯ ПЕТРОВА") == "Дарья Петрова"

assert build_report("Анна", [80, 90, 100]) == "Результат: Анна — средний балл 90.00"
assert build_report("Борис", [50], precision=1) == "Результат: Борис — средний балл 50.0"
assert build_report("Дарья", [], prefix="Итог") == "Итог: Дарья — нет данных"

assert collect_tags("Python", "python", "PYTHON") == ("python",)
assert collect_tags("A", "", "  ", "B") == ("a", "b")
assert collect_tags("X", "Y", lowercase=False) == ("X", "Y")

print("Все assert-проверки успешно пройдены")

print("\n--- Демонстрация вызовов функций ---")
print(arithmetic_mean([1, 2, 3, 4, 5]))
print(normalize_name("  илья   петров  "))
print(build_report("Анна", [85, 90, 95]))
print(build_report("Борис", [70, 80], precision=1, prefix="Отчёт"))
print(collect_tags("Python", "Data", "python", "", "LAB"))

print("\n--- Распаковка ---")
scores = [10, 20, 30, 40]
print("Среднее из списка:", arithmetic_mean(scores))

tag_list = ["AI", "ML", "ai", "  "]
print("Теги из списка:", collect_tags(*tag_list))

dicti = {"student": "Дарья", "results": [95, 100, 90], "precision": 3, "prefix": "Итог"}
print("Отчёт из словаря:", build_report(**dicti))

# Исследование LEGB
print("\n--- LEGB ---")

course = "Python"  # global

def outer():
    course = "основы программирования"  # enclosing

    def inner():
        nonlocal course  # ссылаемся на enclosing, НЕ на global
        course = "питон"
        print(f"  inner: course = {course}")

    print(f"  outer до inner: course = {course}")
    inner()
    print(f"  outer после inner: course = {course}")

print(f"global: course = {course}")
outer()
print(f"global после outer: course = {course}")

# Ошибка изменяемого значения по умолчанию
print("\n--- Ошибка изменяемого значения по умолчанию ---")

def add_result(value, results=[]):
    results.append(value)
    return results

def add_result_fixed(value, results=None):
    if results is None:
        results = []  # новый список при каждом вызове
    results.append(value)
    return results
r3 = add_result_fixed(10)
r4 = add_result_fixed(20)
print(f"r3 = {r3}, r4 = {r4}")

# Практическое расширение
print("\n--- Практическое расширение ---")
def apply_to_results(operation, values):
    return [operation(v) for v in values]

def make_threshold_checker(threshold):
    def checker(value):
        return value >= threshold
    return checker

data = [1, 2, 3, 4, 5]
print("Удвоение (lambda):             ", apply_to_results(lambda x: x * 2, data))

check_70 = make_threshold_checker(70)
check_90 = make_threshold_checker(90)

scores = [65, 72, 88, 95]
print(f"Порог 70: {[check_70(s) for s in scores]}")
print(f"Порог 90: {[check_90(s) for s in scores]}")

print(f"check_70.__closure__: {check_70.__closure__[0].cell_contents}")
print(f"check_90.__closure__: {check_90.__closure__[0].cell_contents}")