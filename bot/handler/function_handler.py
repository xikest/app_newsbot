from pathlib import Path
import pickle
import gzip
class FunctionHandler:
    # ===============================================
    # pickle 파일
    # ===============================================
    class Pickle:
        @staticmethod
        def save_to_pickle(data, file_name, data_path: Path = Path.cwd()):
            # print(data_path)
            # data_path/f'{file_name}.pickle'
            # print(f"{Path.cwd()}/{file_name}.pickle")
            with gzip.open(f"{data_path}/{file_name}.pickle", 'wb') as f:
                pickle.dump(data, f)

        @staticmethod
        def load_from_pickle(file_name, data_path: Path = Path.cwd()):
            with gzip.open(f"{data_path}/{file_name}.pickle", 'rb') as f:
                return pickle.load(f)