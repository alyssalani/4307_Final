# gen_and_pop_platform.py

import csv, sqlite3

# Generate Stuff
def make_platform_csv():
    with open('platforms.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        field = ["platform_id", "name", "cost"]
        writer.writerow(field)
        writer.writerow(["1","Spotify", 10])
        writer.writerow(["2","Soundcloud", 12])
        writer.writerow(["3","Apple-Music", 11])
        writer.writerow(["4","Pandora-Premium", 5])
        writer.writerow(["5","Youtube-Music", 10])
        writer.writerow(["6","Radio", 0])

    file.close()


# Populate Stuff
connection = sqlite3.connect("Music.db")
cursor = connection.cursor()

def populate_table(csv_file, table_name):
    rows = []
    with open(csv_file, 'r') as f:
        csvreader = csv.reader(f)
        header = next(csvreader)
        for i in csvreader:
            rows.append(i)
    for x in rows:
        platform_id = x[0]
        name = x[1]
        cost = x[2]
        cursor.execute("INSERT INTO " + table_name + " (platformID, platform_name, cost) VALUES('{}', '{}', '{}')".format(platform_id, name, cost))
        connection.commit()
        

make_platform_csv()
populate_table("platforms.csv", "Platform")