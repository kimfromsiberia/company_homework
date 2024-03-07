"""
В этот раз у нас есть компания, в ней отделы, в отделах люди. У людей есть имя, должность и зарплата.

Ваши задачи такие:
1. Вывести названия всех отделов
2. Вывести имена всех сотрудников компании.
3. Вывести имена всех сотрудников компании с указанием отдела, в котором они работают.
4. Вывести имена всех сотрудников компании, которые получают больше 100к.
5. Вывести позиции, на которых люди получают меньше 80к (можно с повторениями).
6. Посчитать, сколько денег в месяц уходит на каждый отдел – и вывести вместе с названием отдела

Второй уровень:
7. Вывести названия отделов с указанием минимальной зарплаты в нём.
8. Вывести названия отделов с указанием минимальной, средней и максимальной зарплаты в нём.
9. Вывести среднюю зарплату по всей компании.
10. Вывести названия должностей, которые получают больше 90к без повторений.
11. Посчитать среднюю зарплату по каждому отделу среди девушек (их зовут Мишель, Николь, Кристина и Кейтлин).
12. Вывести без повторений имена людей, чьи фамилии заканчиваются на гласную букву.

Третий уровень:
Теперь вам пригодится ещё список taxes, в котором хранится информация о налогах на сотрудников из разных департаметов.
Если department None, значит, этот налог применяется ко всем сотрудникам компании.
Иначе он применяется только к сотрудникам департмента, название которого совпадает с тем, что записано по ключу department.
К одному сотруднику может применяться несколько налогов.

13. Вывести список отделов со средним налогом на сотрудников этого отдела.
14. Вывести список всех сотредников с указанием зарплаты "на руки" и зарплаты с учётом налогов.
15. Вывести список отделов, отсортированный по месячной налоговой нагрузки.
16. Вывести всех сотрудников, за которых компания платит больше 100к налогов в год.
17. Вывести имя и фамилию сотрудника, за которого компания платит меньше всего налогов.
"""

departments = [
    {
        "title": "HR department",
        "employers": [
            {"first_name": "Daniel", "last_name": "Berger", "position": "Junior HR", "salary_rub": 50000},
            {"first_name": "Michelle", "last_name": "Frey", "position": "Middle HR", "salary_rub": 75000},
            {"first_name": "Kevin", "last_name": "Jimenez", "position": "Middle HR", "salary_rub": 70000},
            {"first_name": "Nicole", "last_name": "Riley", "position": "HRD", "salary_rub": 120000},
        ]
    },
    {
        "title": "IT department",
        "employers": [
            {"first_name": "Christina", "last_name": "Walker", "position": "Python dev", "salary_rub": 80000},
            {"first_name": "Michelle", "last_name": "Gilbert", "position": "JS dev", "salary_rub": 85000},
            {"first_name": "Caitlin", "last_name": "Bradley", "position": "Teamlead", "salary_rub": 950000},
            {"first_name": "Brian", "last_name": "Hartman", "position": "CTO", "salary_rub": 130000},
        ]
    },
]

taxes = [
    {"department": None, "name": "vat", "value_percents": 13},
    {"department": "IT Department", "name": "hiring", "value_percents": 6},
    {"department": "BizDev Department", "name": "sales", "value_percents": 20},
]

# 1. Вывести названия всех отделов

def print_department_name(departments):
    for department in departments:
        print(department['title'])

print_department_name(departments)

# 2. Вывести имена всех сотрудников компании.

def print_employee_names(departments):
    for department in departments:
        for employee in department['employers']:
            print(employee['first_name'])

print_employee_names(departments)

# 3. Вывести имена всех сотрудников компании с указанием отдела, в котором они работают.

def print_emp_and_dep_names(departments):
    for department in departments:
        for employee in department['employers']:
            print(f"{employee['first_name']} {department['title']}")

print_emp_and_dep_names(departments)

# 4. Вывести имена всех сотрудников компании, которые получают больше 100к.

def print_rich_employers(departments):
    for department in departments:
        for employee in department['employers']:
            if employee['salary_rub'] > 100000:
                print(f"{employee['first_name']}")

print_rich_employers(departments)

# 5. Вывести позиции, на которых люди получают меньше 80к (можно с повторениями).

def print_low_paid_position(departments):
    for department in departments:
        for employee in department['employers']:
            if employee['salary_rub'] < 80000:
                print(f"{employee['position']}")

print_low_paid_position(departments)

#6. Посчитать, сколько денег в месяц уходит на каждый отдел – и вывести вместе с названием отдела

def print_department_salary(departments):
    for department in departments:
        department_salary = 0
        for employee in department['employers']:
            department_salary += employee['salary_rub']
        print(f"{department_salary} {department['title']}")

print_department_salary(departments)

# 7. Вывести названия отделов с указанием минимальной зарплаты в нём.

def print_min_salary(departments):
    for department in departments:
        min_salary = sorted([salary['salary_rub'] for salary in department['employers']])[0]
        print(f"{department['title']} {min_salary}")

print_min_salary(departments)

# 8. Вывести названия отделов с указанием минимальной, средней и максимальной зарплаты в нём.

def print_salary_statistics(departments):
    for department in departments:
        salary = [salary['salary_rub'] for salary in department['employers']]
        print(f"{department['title']}. Min salary: {min(salary)}, average salary: {sum(salary) / len(salary)}, max salary: {max(salary)}")

print_salary_statistics(departments)

# Вывести среднюю зарплату по всей компании.

def print_average_salary(departments):
    company_salary = []
    for department in departments:
        company_salary += [salary['salary_rub'] for salary in department['employers']]
    print(sum(company_salary) / len(company_salary))

print_average_salary(departments)

# 10. Вывести названия должностей, которые получают больше 90к без повторений.

def print_high_paid_position(departments):
    high_paid_position = []
    for department in departments:
        for employee in department['employers']:
            if employee['salary_rub'] > 90000 and employee['position'] not in high_paid_position:
                high_paid_position.append(employee['position'])
    print(high_paid_position)

print_high_paid_position(departments)

# 11. Посчитать среднюю зарплату по каждому отделу среди девушек (их зовут Мишель, Николь, Кристина и Кейтлин).

def print_average_female_salary(departments):
    female = ['Michelle', 'Nicole', 'Christina', 'Caitlin']
    for department in departments:
        female_salary = [salary['salary_rub'] for salary in department['employers'] if salary['first_name'] in female]
        print(f"{department['title']} {sum(female_salary) / len(female_salary)}")

print_average_female_salary(departments)

# 12. Вывести без повторений имена людей, чьи фамилии заканчиваются на гласную букву.

def vowel_end_last_name(departments):
    vowel = ['a', 'e', 'i', 'o', 'u', 'y']
    names = []
    for department in departments:
        for employee in department['employers']:
            if employee['last_name'][-1] in vowel and employee['first_name'] not in names:
                names.append(employee['first_name'])
    print(names)

vowel_end_last_name(departments)

# 13. Вывести список отделов со средним налогом на сотрудников этого отдела.

def department_percents_tax(departments, taxes):
    department_tax = {}
    for department in departments:
        department_tax[department['title']] = 0
        for tax in taxes:
            if tax['department'] == None or tax['department'].lower() == department['title'].lower():
                department_tax[department['title']] += tax['value_percents']
    return department_tax

print(department_percents_tax(departments, taxes))

# 14. Вывести список всех сотредников с указанием зарплаты "на руки" и зарплаты с учётом налогов.
    
def employee_tax(departments):
    for department in departments:
        percent_tax = department_percents_tax(departments, taxes)[department['title']]
        for employee in department['employers']:
            print(f"{employee['first_name']}. На руки: {employee['salary_rub'] - employee['salary_rub'] * percent_tax / 100}. До вычета: {employee['salary_rub']}.")

employee_tax(departments)

# 15. Вывести список отделов, отсортированный по месячной налоговой нагрузки.

def calculate_department_tax(departments):
    department_tax = {}
    for department in departments:
        salary_sum = sum([salary['salary_rub'] for salary in department['employers']])
        department_tax[department['title']] = salary_sum * department_percents_tax(departments, taxes)[department['title']] / 100
    return sorted(department_tax.items(), key=lambda item: item[1])


print(calculate_department_tax(departments))

# 16. Вывести всех сотрудников, за которых компания платит больше 100к налогов в год.

def high_annual_tax(departments):
    for department in departments:
        percent_tax = department_percents_tax(departments, taxes)[department['title']]
        for employee in department['employers']:
            if employee['salary_rub'] * percent_tax / 100 *12 > 100000:
                print(employee['first_name'])

high_annual_tax(departments)

# 17. Вывести имя и фамилию сотрудника, за которого компания платит меньше всего налогов.

def min_employee_tax(departments):
    employers_tax = []
    for department in departments:
        percent_tax = department_percents_tax(departments, taxes)[department['title']]
        for employee in department['employers']:
            employers_tax.append((str(employee['first_name'] + ' ' + employee['last_name']), employee['salary_rub'] * percent_tax / 100))
    print(sorted(employers_tax, key=lambda item: item[1])[0][0])
min_employee_tax(departments)

'''
departments = [
    {
        "title": "HR department",
        "employers": [
            {"first_name": "Daniel", "last_name": "Berger", "position": "Junior HR", "salary_rub": 50000},
            {"first_name": "Michelle", "last_name": "Frey", "position": "Middle HR", "salary_rub": 75000},
            {"first_name": "Kevin", "last_name": "Jimenez", "position": "Middle HR", "salary_rub": 70000},
            {"first_name": "Nicole", "last_name": "Riley", "position": "HRD", "salary_rub": 120000},
        ]
    },
    {
        "title": "IT department",
        "employers": [
            {"first_name": "Christina", "last_name": "Walker", "position": "Python dev", "salary_rub": 80000},
            {"first_name": "Michelle", "last_name": "Gilbert", "position": "JS dev", "salary_rub": 85000},
            {"first_name": "Caitlin", "last_name": "Bradley", "position": "Teamlead", "salary_rub": 950000},
            {"first_name": "Brian", "last_name": "Hartman", "position": "CTO", "salary_rub": 130000},
        ]
    },
]

taxes = [
    {"department": None, "name": "vat", "value_percents": 13},
    {"department": "IT Department", "name": "hiring", "value_percents": 6},
    {"department": "BizDev Department", "name": "sales", "value_percents": 20},
]'''
