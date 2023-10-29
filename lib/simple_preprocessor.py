import csv
from lib.encoder import OneHotEncoder

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



        self.columns = []
        self.number_columns = []
        self.string_columns = []

        for col_name, value in self.csv_data[0].items():
            try:
                float_value = float(value)
                self.number_columns.append(col_name)
            except ValueError:
                self.string_columns.append(col_name)

            finally:
                self.columns.append(col_name)


        self.encoder = OneHotEncoder(data_list=self.csv_data,string_columns=self.string_columns)






    def fit(self):
        self.encoder.fit()
        processed_data = []

        for row in self.csv_data:
            new_row = {}
            for col_name, col_value in row.items():
                if col_name in self.string_columns:
                    new_row[col_name] = self.encoder.transform(col_name, col_value)
                else:
                    new_row[col_name] = col_value

            processed_data.append(new_row)


        for row in processed_data[:5]:
            print(row)

