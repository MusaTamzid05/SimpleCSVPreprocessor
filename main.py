from lib.simple_preprocessor import SimplePreprocessor

if __name__ == "__main__":
    preprocessor = SimplePreprocessor(csv_path="./adult.csv")
    processed_data = preprocessor.fit()

    for row in processed_data[:5]:
        print(row)

