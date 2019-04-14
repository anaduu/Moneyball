import csv
import sys
import random

# ako zelite veci/manji validation set, promijeniti ovu varijablu
percentage = 0.20 #posto

def inList(value, randomlist):
    for x in randomlist:
        if x == value:
            return True
    return False

with open("data/" + sys.argv[1], newline='') as read_file:
    dialect = csv.Sniffer().sniff(read_file.readline())
    read_file.seek(0)
    reader = csv.reader(read_file, dialect)
    for count, line in enumerate(read_file):
        pass
    # broj redaka bez headera
    number_of_data = count
    rndlist = random.sample(range(0, number_of_data), int(number_of_data * percentage))

    main_index = 0
    end_index = 0
    read_file.seek(0)
    with open("data/main_" + sys.argv[1], "w") as main_write:
        with open("data/end_" + sys.argv[1], "w") as end_write:
            main_writer = csv.writer(main_write)        
            end_writer = csv.writer(end_write)
            header = next(reader)
            main_writer.writerow(header)
            end_writer.writerow(header)

            for i, r in enumerate(reader):
                if inList(i, rndlist):
                    r[0] = end_index
                    end_writer.writerow(r)
                    end_index += 1
                else:
                    r[0] = main_index
                    main_writer.writerow(r)
                    main_index += 1

