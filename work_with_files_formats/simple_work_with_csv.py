import csv

nicknames = ['@boss', '@terminator', '@killer', '@Stepa2007', '@nagibaTOR_007']

with open('test1.csv', 'w', newline='') as csvfile:
    fieldnames = ['nicknames', 'length']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=',')
    writer.writeheader()
    for nickname in nicknames:
        writer.writerow({'nicknames': nickname, 'length': len(nickname)})

with open('test1.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(f'{row['nicknames']}, {row['length']}')

