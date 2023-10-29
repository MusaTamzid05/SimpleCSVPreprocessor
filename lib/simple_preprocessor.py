import csv

class SimplePreprocessor:
    def __init__(self, csv_path):
        self.csv_data = []

        with open(csv_path) as f:
            reader = csv.DictReader(f)

            for row in reader:
                new_row = {}

                for key, value in row.items():
                    new_row[key.strip()] = value.strip()

                self.csv_data.append(new_row)


        print(self.csv_data[0])


    def fit(self):
        print("fit")
