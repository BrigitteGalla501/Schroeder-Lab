import csv

with open('Csv_example.csv', 'w', newline= '') as file:
    writer = csv.writer(file)
    field = ["name", "age", "country"]

    writer.writerrow(field)
    writer.writerrow(["Jason Todd", "23", "United States"])
    writer.writerow(["Roy Harper", "28", "United States"])
    writer.writerow(["Kory Anders", "26", "Tamaran"])



