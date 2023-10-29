

class OneHotEncoder:
    '''
       cat, dog, cow
       cat [1,0,0]
       dog [0,1,0]
       cow [0,0,1]

    '''

    def __init__(self, data_list, string_columns):
        self.data_list = data_list
        self.unique_col_data = {}

        for string_column in string_columns:
            self.unique_col_data[string_column] = []

        self.features = {}


    def fit(self):


        for row in self.data_list:
            for string_column in self.unique_col_data.keys():
                value = row[string_column]

                if value not in self.unique_col_data[string_column]:
                    self.unique_col_data[string_column].append(value)


        for key, value in self.unique_col_data.items():
            self.features[key] = {}

            for index, unique_value in enumerate(value):
                arr = [0 for _ in range(len(value))]
                arr[index] = 1
                self.features[key][unique_value] = arr

        for key, value in self.features.items():
            print("*" * 10)
            print(key)

            for key2, value2 in value.items():
                print(key2, value2)
            print("*" * 10)

    def transform(self,col_name, value):
        return self.features[col_name][value]






