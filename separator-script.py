import csv

with open('data1.csv', newline='') as source:
    dialect = csv.Sniffer().sniff(source.readline())
    source.seek(0)
    reader = csv.reader(source, dialect)
    number_of_columns = len(next(reader))
    source.seek(0)
    with open("goalkeepers.csv", "w") as goalkeepers_file:
        gk_writer = csv.writer(goalkeepers_file)
        with open("players.csv", "w") as players_file:
            pl_writer = csv.writer(players_file)

            position_column = -1
            for r in reader:
                for i in range(number_of_columns):
                    if r[i] == "Position":
                        position_column = i

            source.seek(0)
            for r in reader:
                if r[position_column] == "GK":
                    gk_writer.writerow(r)
                else:
                    pl_writer.writerow(r)
