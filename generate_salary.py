#generate_salary.py

import csv
import random

salaries=('1000', '20000', '25000', '35000', '45000', '50000', '60000', '70000', '80000', '90000', '110000', '130000', '160000', '200000', '500000', '1000000')

# creates a list containing salary information
def create_salary(salary, status):
    return [salary, status]

# Returns a list of the incomes
def generate_incomes(iterations):
    incomes = []
    i = 0
    while i < iterations:
        salary = random.choice(salaries)
        status = 'listener'
        incomes.append(create_salary(salary, status))

        i += 1
    return incomes

# Generate a list of incomes
def make_incomes_csv():
    iterations = input('How many incomes do you want to generate? \n')
    incomes = generate_incomes(int(iterations))

    with open('incomes.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        field = ["salary", "status"]

        writer.writerow(field)
        for income in incomes:
            writer.writerow(income)

    file.close()
