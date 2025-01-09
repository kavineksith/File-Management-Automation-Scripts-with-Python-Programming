import os
import json
import csv

class UnsupportedFileExtensionError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class FileCreationFailureError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class FileCreator:
    def __init__(self, default_dir=None):
        self.default_dir = default_dir

    def create_file_if_not_exists(self, file_path):
        full_path = os.path.join(self.default_dir or '', file_path)
        _, extension = os.path.splitext(file_path)

        if extension == '.csv':
            self.create_csv(full_path)
        elif extension == '.json':
            self.create_json(full_path)
        elif extension == '.txt':
            self.create_text(full_path)
        else:
            raise UnsupportedFileExtensionError(f"Unsupported file extension: {extension}")

    def create_csv(self, csv_file):
        try:
            if not os.path.isfile(csv_file):
                with open(csv_file, 'w', newline='') as csvfile:
                    pass  # Just create the file
        except IOError as e:
            raise FileCreationFailureError(f"Error creating CSV file: {e}")

    def create_json(self, json_file):
        try:
            if not os.path.isfile(json_file):
                with open(json_file, 'w') as jsonfile:
                    json.dump({}, jsonfile)  # Write an empty JSON object
        except IOError as e:
            raise FileCreationFailureError(f"Error creating JSON file: {e}")

    def create_text(self, txt_file):
        try:
            if not os.path.isfile(txt_file):
                with open(txt_file, 'w') as txtfile:
                    pass  # Just create the file
        except IOError as e:
            raise FileCreationFailureError(f"Error creating text file: {e}")

# Example usage:
if __name__ == "__main__":
    default_directory = '/path/to/default/directory/'
    file_creator = FileCreator(default_dir=default_directory)

    try:
        file_creator.create_file_if_not_exists('data.csv')
        file_creator.create_file_if_not_exists('data.json')
        file_creator.create_file_if_not_exists('data.txt')
        file_creator.create_file_if_not_exists('data.exe')  # Raises UnsupportedFileExtensionError
    except UnsupportedFileExtensionError as e:
        print(f"Unsupported file extension error: {e.message}")
    except FileCreationFailureError as e:
        print(f'File creation failure error: {e.message}')
    except Exception as e:
        print(f"Unexpected error occurred: {e}")
