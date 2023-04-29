# generate_everything.py

import generate_people, generate_salary

def generate_everything():
    generate_people.make_people_csv()
    generate_salary.make_incomes_csv()
    print('Generate everything done')

generate_everything()