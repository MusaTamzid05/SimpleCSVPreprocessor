from lib.simple_preprocessor import SimplePreprocessor

if __name__ == "__main__":
    preprocessor = SimplePreprocessor(csv_path="./adult.csv")
    processed_data = preprocessor.fit()

    train_data, test_data = preprocessor.train_test_split(processed_data=processed_data)

    print(f"total {len(processed_data)}")
    print(f"train {len(train_data)}")
    print(f"test {len(test_data)}")


    list_data = preprocessor.to_list(processed_data=processed_data)




