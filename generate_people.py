# generate_people.py

import csv
import random

first_names=('Max', 'Ben', 'Alyssa', 'Russ', 'Wendy', 'Summer', 'Katie', 'Hunter', 'Ross', 'Sauni', 'Tevyn', 'Austin', 'Leighonna', 'Ezra', 'Raechel', 'Emma', 'Melanie', 'Mike', 'Evan', 'Justin', 'Jane', 'John', 'Joe', 'Dan', 'Andy', 'Minh', 'Derek', 'Kendall', 'Curtis', 'Ren', 'Bart', 'Ian', 'Homer', 'Peter', 'Caitlin', 'Riley', 'Jim', 'Nathan', 'Sophia', 'Xavier', 'Ryan', 'Dylan', 'Koji', 'Kenji', 'Cieran', 'Olivia', 'Jared', 'Jacob', 'Guy', 'Reid', 'Kamden')
last_names=('Stetter', 'Ponce', 'Jenks', 'Stander', 'Smith', 'Larsen', 'Ross', 'Murray', 'Louis', 'Daly', 'Scott', 'Apples', 'Oranges', 'Kiwi', 'Smithy-Smith', 'McDonald', 'Hennesy', 'Johnson', 'Shoemaker', 'Heinz', 'Turner', 'Jenkins', 'Bui', 'Lee', 'Prentice', 'Troll', 'Dickson', 'Cider', 'Quinn', 'Rassmussen', 'Gubler', 'Grapeton', 'Backpack', 'Moter', 'Anderson', 'Tier', 'Brooks', 'Davenport', 'Naran', 'Schnable', 'Pants', 'Shirt', 'Expo')
genres=('Metal', 'Rock', 'Rap', 'Country', 'EDM', 'Indie', 'Alternative', 'Raggae', 'Pop', 'R&B', 'Punk', 'Disco')
states=('Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming')
platforms=('Spotify', 'Soundcloud', 'Apple-Music', 'Pandora-Premium', 'Youtube-Music', 'Radio')

# Returns a list containing a person's information.
def create_person(platform_id, name, genre, age, state, weight, height):
    return [platform_id, name, genre, age, state, weight, height]

# Returns a list of the population.
def generate_people(iterations):
    population = []
    i = 0
    while i < iterations:
        platform = random.choice(platforms)
        name = random.choice(first_names) + " " + random.choice(last_names)
        genre = random.choice(genres)
        age = str(random.randrange(3,90))
        state = random.choice(states)
        weight = str(random.randrange(80, 220))
        height = str(random.randrange(55, 80))

        population.append(create_person(platform, name, genre, age, state, weight, height))
        #print("Created: " + name + ", Age: " + age)
        i += 1

    return population


# Generate a list of people.
def make_people_csv():
    iterations = input('How many people do you want to generate? \n')
    population = generate_people(int(iterations))

    with open('people.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        field = ["platform_id","name","genre","age","state","weight","height"]

        writer.writerow(field)
        for person in population:
            writer.writerow(person)

    file.close()
