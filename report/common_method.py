import pickle

class CommonMethod:  
    @staticmethod
    def load_data_from_pickle(file_path):
        try:
            with open(file_path, 'rb') as file:
                data = pickle.load(file)
            return data
        except FileNotFoundError:
            print("파일없음 예외처리")
            return {}

    @staticmethod        
    def count_key(data, target_string):
        return sum(1 for key in data.keys() if target_string in key)
    
    @staticmethod        
    def count_key_and_value(data, target_key, target_value):
        count = sum(1 for key in data if target_key in key and target_value in data[key])
        return count
    
    @staticmethod        
    def make_tag_string(execution):
        tags = ""
        if execution == "ST" or execution == "Smoke":
            tags = ["@pytest.mark.smoke"]
        elif execution == "RT" or execution == "Regression":
            tags = ["@pytest.mark.smoke","@pytest.mark.regression"]
        elif execution == "test" or execution == "Temporary":
            tags = ["@pytest.mark.test"]
        return tags


