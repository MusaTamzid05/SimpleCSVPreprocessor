import statistics

class StandardScaler:
    def __init__(self, preprocessor):
        self.preprocessor = preprocessor
        self.data_info = {}

    def fit(self):
        number_columns = self.preprocessor.number_columns

        for col in number_columns:
            col_data = self.preprocessor.get_col_data_of(col)
            col_data = [float(value) for value in col_data]
            mean = statistics.mean(col_data)
            stdev = statistics.stdev(col_data)

            col_info = {"mean": mean, "stdev": stdev}
            self.data_info[col] = col_info

    def transform(self, col_name, col_value):
        # z = (x - u) / s
        # x = row data
        # u = mean
        # s = stdev

        mean = self.data_info[col_name]["mean"]
        stdev = self.data_info[col_name]["stdev"]

        return (col_value - mean) / stdev





