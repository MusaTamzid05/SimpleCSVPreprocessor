from lib.simple_preprocessor import SimplePreprocessor

if __name__ == "__main__":
    preprocessor = SimplePreprocessor(csv_path="./adult.csv")
    processed_data = preprocessor.fit()

    print(processed_data[0])

    list_data = preprocessor.to_list(processed_data=processed_data)

    print(list_data[0])



