import csv

with open('data1.csv', newline='') as source:
    dialect = csv.Sniffer().sniff(source.readline())
    source.seek(0)
    reader = csv.reader(source, dialect)
    number_of_columns = len(next(reader))
    source.seek(0)
    with open("data/goalkeepers.csv", "w") as goalkeepers_file:
        gk_writer = csv.writer(goalkeepers_file)
        with open("data/players.csv", "w") as players_file:
            pl_writer = csv.writer(players_file)
            gk_index = 0
            pl_index = 0

            position_column = -1
            for r in reader:
                for i in range(number_of_columns):
                    if r[i] == "Position":
                        position_column = i

            source.seek(0)
            header = next(reader)
            gk_writer.writerow(header)
            pl_writer.writerow(header)
            for r in reader:
                if r[position_column] == "GK":
                    r[0] = gk_index
                    gk_writer.writerow(r)
                    gk_index += 1
                else:
                    r[0] = pl_index
                    pl_writer.writerow(r)
                    pl_index += 1

