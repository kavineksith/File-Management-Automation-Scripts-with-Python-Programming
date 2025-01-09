import os
import sys


class FileExtensionRenamer:
    def __init__(self, current_extensions, new_extension):
        self.location_path = os.getcwd()
        self.current_extensions = current_extensions
        self.new_extension = new_extension
        self.total_file_count = 0
        self.total_modified_file_count = 0
        self.total_unmodified_file_count = 0

    def process_directory(self, path):
        try:
            for item in os.listdir(path):
                full_path = os.path.join(path, item)
                if os.path.isdir(full_path):
                    self.process_directory(full_path)  # Recur into subdirectories
                else:
                    self.process_file(full_path)
        except PermissionError as e:
            print(f"Permission error: {e}")
        except FileNotFoundError as e:
            print(f"File or directory not found: {e}")
        except KeyboardInterrupt:
            print("Operation interrupted by the user.")
            sys.exit(1)
        except Exception as e:
            print(f"An unexcepted error occured when processing directory: {e}")

    def process_file(self, file_path):
        try:
            file_name, file_extension = os.path.splitext(file_path)
            if file_extension in self.current_extensions:
                new_file_path = f"{file_name}{self.new_extension}"
                os.rename(file_path, new_file_path)
                self.total_modified_file_count += 1
            else:
                self.total_unmodified_file_count += 1
            self.total_file_count += 1
        except PermissionError as e:
            print(f"Permission error: {e} for file {file_path}")
        except FileNotFoundError as e:
            print(f"File not found: {e} for file {file_path}")
        except Exception as e:
            print(f"Error processing file {file_path}: {e}")

    def file_extension_changer(self):
        try:
            self.process_directory(self.location_path)
        except PermissionError as e:
            print(f"Permission error: {e}")
        except FileNotFoundError as e:
            print(f"File or directory not found: {e}")
        except KeyboardInterrupt:
            print("Operation interrupted by the user.")
            sys.exit(1)
        except Exception as e:
            print(f"An unexcepted error occured in file extension changer method: {e}")
            sys.exit(1)

    def result_display(self):
        print(f"Total file extension changed count: {self.total_modified_file_count}")
        print(f"Total file extension unchanged count: {self.total_unmodified_file_count}")
        print(f"Total file count: {self.total_file_count}")


def get_user_input():
    try:
        # Get list of current extensions
        print("Enter the file extensions to change, separated by commas (e.g., .odt, .txt):")
        extensions_input = input()
        if not extensions_input:
            raise ValueError("No input provided for file extensions.")
        current_extensions = [ext.strip() for ext in extensions_input.split(",")]

        # Validate that extensions start with a dot
        if any(not ext.startswith('.') for ext in current_extensions):
            raise ValueError("Each file extension should start with a dot (e.g., .txt).")

        # Get new file extension
        print("Enter the new file extension (e.g., .txt):")
        new_extension = input().strip()
        if not new_extension.startswith('.'):
            raise ValueError("New file extension should start with a dot (e.g., .txt).")

        return current_extensions, new_extension

    except ValueError as e:
        print(f"Value error: {e}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nOperation interrupted by the user.")
        sys.exit(1)
    except Exception as e:
        print(f"An unexcepted error occured when getting user inputs method: {e}")
        sys.exit(1)


# Main execution
if __name__ == "__main__":
    try:
        current_extensions, new_extension = get_user_input()
        file_extension_wizard = FileExtensionRenamer(current_extensions, new_extension)
        file_extension_wizard.file_extension_changer()
        file_extension_wizard.result_display()
        sys.exit(0)
    except KeyboardInterrupt:
        print("\nOperation interrupted by the user.")
        sys.exit(1)
    except Exception as e:
        print(f"An unexcepted error occured: {e}")
        sys.exit(1)
