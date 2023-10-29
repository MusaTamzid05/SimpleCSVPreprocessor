from lib.simple_preprocessor import SimplePreprocessor

if __name__ == "__main__":
    preprocessor = SimplePreprocessor(csv_path="./adult.csv")
    preprocessor.fit()
