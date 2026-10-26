class Faculty:
    def __init__(self, id, name, students, university_id):
        self.id = id
        self.name = name
        self.students = students
        self.university_id = university_id


class University:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class FacultyUniversity:
    def __init__(self, faculty_id, university_id):
        self.faculty_id = faculty_id
        self.university_id = university_id


universities = [
    University(1, "Астраханский университет"),
    University(2, "Алтайский университет"),
    University(3, "Московский университет"),
]

faculties = [
    Faculty(1, "Информатики", 800, 1),
    Faculty(2, "Экономики", 1200, 1),
    Faculty(3, "Математики", 950, 2),
    Faculty(4, "Физики", 600, 3),
]

links = [
    FacultyUniversity(1, 1),
    FacultyUniversity(2, 1),
    FacultyUniversity(3, 2),
    FacultyUniversity(4, 3),
    FacultyUniversity(1, 2),
]


def main():
    # Г1. Университеты на букву А и их факультеты.
    print("Г1. Университеты на букву А и их факультеты")
    for u in universities:
        if u.name.startswith("А"):
            names = [f.name for f in faculties if f.university_id == u.id]
            print(u.name)
            print("  " + (", ".join(names) if names else "нет факультетов"))

    # Г2. Максимальное число студентов на факультете каждого университета.
    print("\nГ2. Максимальное число студентов, по возрастанию")
    result = []
    for u in universities:
        numbers = [
            f.students for f in faculties if f.university_id == u.id
        ]
        if numbers:
            result.append((u.name, max(numbers)))

    result = sorted(result, key=lambda x: x[1])
    for name, students in result:
        print(f"{name}: {students}")

    # Г3. Связи многие-ко-многим с сортировкой по университетам.
    print("\nГ3. Факультеты и университеты, по названию университета")
    pairs = [
        (f.name, u.name)
        for link in links
        for f in faculties
        for u in universities
        if f.id == link.faculty_id and u.id == link.university_id
    ]
    pairs = sorted(pairs, key=lambda x: x[1])
    for faculty, university in pairs:
        print(f"{faculty} - {university}")


if __name__ == "__main__":
    main()
