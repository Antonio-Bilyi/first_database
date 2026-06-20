from datetime import date, timedelta
import faker
from random import randint, sample
import sqlite3

NUMBER_GROUPS = 3
NUMBER_STUDENTS = 30
NUMBER_TEACHERS = 5
NUMBER_GRADES = 20
SUBJECTS = ['Математика', 'Історія', 'Фізика', 'Англійська мова', 'Географія']


def generate_fake_data(number_groups, number_teachers, number_students) -> tuple:

    fake_groups = []
    fake_teachers = []
    fake_students = []

    fake_data = faker.Faker('uk_UA')

    for i in range(number_groups):
        fake_groups.append(100 + i + 1)

    for _ in range(number_teachers):
        fake_teachers.append(fake_data.unique.name())
    
    for _ in range(number_students):
        name = fake_data.unique.name()
        email = fake_data.unique.email()
        fake_students.append((name, email))
    

    return fake_groups, fake_teachers, fake_students

def prepare_data(groups, teachers, students, subjects) -> tuple:

    for_groups = []
    for number in groups:
        for_groups.append((number,))
    
    for_teachers = []
    for name in teachers:
        for_teachers.append((name,))
    
    for_subjects = []
    teachers_ids = sample(range(1, len(teachers) + 1), len(subjects))
    for subject, teachers_id in zip(subjects, teachers_ids):
        for_subjects.append((subject, teachers_id))
    
    for_students = []
    for name, email in students:
        for_students.append((name, email, randint(1, len(groups))))
    
    for_grades = []
    start_date = date(2025, 9, 1)
    end_date = date(2026, 6, 1)
    delta_days = (end_date - start_date).days

    for student_id in range(1, len(students) + 1):
        number_of_grades = randint(1, NUMBER_GRADES)
        for _ in range(number_of_grades):
            subject_id = randint(1, len(subjects))
            grade = randint(1, 100)
            grade_date = start_date + timedelta(days=randint(0, delta_days))
            for_grades.append((student_id, subject_id, grade, grade_date.isoformat()))
    

    return for_groups, for_teachers, for_subjects, for_students, for_grades

def insert_data_to_db(groups, teachers, students, subjects, grades):

    with sqlite3.connect('tables.db') as connection:

        current = connection.cursor()

        sql_to_groups = """INSERT INTO groups(number)
                           VALUES (?)"""
        current.executemany(sql_to_groups, groups)

        sql_to_teachers = """INSERT INTO teachers(name)
                            VALUES (?)"""
        current.executemany(sql_to_teachers, teachers)

        sql_to_subjects = """INSERT INTO subjects(name, teacher_id)
                            VALUES (?, ?)"""
        current.executemany(sql_to_subjects, subjects)

        sql_to_students = """INSERT INTO students(name, email, group_id)
                            VALUES (?, ?, ?)"""
        current.executemany(sql_to_students, students)

        sql_to_grades = """INSERT INTO grades(student_id, subject_id, grade, date)
                            VALUES (?, ?, ?, ?)"""
        current.executemany(sql_to_grades, grades)

        connection.commit()


if __name__ == '__main__':

    groups, teachers, students = generate_fake_data(NUMBER_GROUPS, NUMBER_TEACHERS, NUMBER_STUDENTS)

    groups, teachers, subjects, students, grades = prepare_data(groups, teachers, students, SUBJECTS)

    insert_data_to_db(groups, teachers, students, subjects, grades)
        
