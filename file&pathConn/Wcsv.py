import csv


with open("data.csv", "w") as file:  # To open and I write to CSV file
    writer = csv.writer(file)  # This allows you to write into the file
    # This how to write to rows in csv
    writer.writerow(["transaction_id", "transaction_date", "customers_name"])
    writer.writerow([1001, "02-02-2020", "samson"])
    writer.writerow([1001, "02-02-2020", "samson"])
    writer.writerow([1001, "02-02-2020", "samson"])
    writer.writerow([1001, "02-02-2020", "samson"])


with open("data.csv", "r") as file:
    reader = csv.reader(file)
    # print(list(reader)) # You can also print the reader out as list
    for row in reader:  # You can iterate over the reader
        print(row)
