import os
import shutil
import sys

class FileOrganizerException(Exception):
    """Base class for exceptions in this module."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class FileNotFoundError(FileOrganizerException):
    """Exception raised when a file or directory is not found."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class InvalidUserChoiceError(FileOrganizerException):
    """Exception raised for invalid user choices."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class FileOrganizer:
    def __init__(self, base_directory):
        self.base_directory = base_directory
        self.extensions = {
            ".jpg": "Images",
            ".png": "Images",
            ".gif": "Images",
            ".mp4": "Videos",
            ".mkv": "Videos",
            ".doc": "Documents",
            ".odt": "Documents",
            ".pdf": "Documents",
            ".txt": "Documents",
            ".mp3": "Music",
            ".wav": "Music",
        }

    def get_unique_filename(self, filepath):
        """
        Generate a unique filename by appending a number if a file with the same name already exists.
        """
        base, ext = os.path.splitext(filepath)
        counter = 1
        new_filepath = filepath
        while os.path.exists(new_filepath):
            new_filepath = f"{base}_{counter}{ext}"
            counter += 1
        return new_filepath

    def handle_file_conflict(self, file_path, folder_path):
        """
        Prompt the user to handle file conflicts with three options: rename and save, overwrite, or do not move.
        """
        filename = os.path.basename(file_path)
        destination_path = os.path.join(folder_path, filename)

        if os.path.exists(destination_path):
            while True:
                try:
                    choice = input(f"File '{filename}' already exists in '{folder_path}'. Choose an option:\n"
                                   "1. Rename and save\n"
                                   "2. Overwrite\n"
                                   "3. Do not move\n"
                                   "Enter the number of your choice: ").strip()
                    
                    if choice == '1':
                        new_destination_path = self.get_unique_filename(destination_path)
                        shutil.move(file_path, new_destination_path)
                        print(f"Renamed and moved '{filename}' to '{folder_path}'.")
                        break
                    elif choice == '2':
                        shutil.move(file_path, destination_path)
                        print(f"Overwritten '{filename}' in '{folder_path}'.")
                        break
                    elif choice == '3':
                        print(f"Skipped moving '{filename}'.")
                        break
                    else:
                        raise InvalidUserChoiceError("Invalid choice. Please enter 1, 2, or 3.")
                except KeyboardInterrupt:
                    print("\nOperation interrupted by the user.")
                    raise
        else:
            shutil.move(file_path, destination_path)
            print(f"Moved '{filename}' to '{folder_path}'.")

    def organize_files(self):
        """
        Organize files in the base directory based on file extensions.
        """
        if not os.path.exists(self.base_directory):
            raise FileNotFoundError(f"Directory '{self.base_directory}' does not exist.")

        for file in os.listdir(self.base_directory):
            file_path = os.path.join(self.base_directory, file)

            if os.path.isfile(file_path):
                file_extension = os.path.splitext(file)[1].lower()

                if file_extension in self.extensions:
                    folder_name = self.extensions[file_extension]
                    folder_path = os.path.join(self.base_directory, folder_name)

                    # Create the folder if it does not exist
                    os.makedirs(folder_path, exist_ok=True)

                    # Handle file conflicts
                    try:
                        self.handle_file_conflict(file_path, folder_path)
                    except PermissionError as e:
                        print(f"Permission error: {e}")
                    except FileOrganizerException as e:
                        print(f"Error: {e.message}")
                else:
                    print(f"Skipped '{file}'. Unknown file extension.")
            else:
                print(f"Skipped '{file}'. It's a directory.")

        print("File organization completed.")

# Usage
if __name__ == "__main__":
    try:
        base_directory = os.path.join(os.path.expanduser('~'), 'Downloads')
        organizer = FileOrganizer(base_directory)
        organizer.organize_files()
    except FileNotFoundError as e:
        print(f"File not found: {e}", file=sys.stderr)
    except PermissionError as e:
        print(f"Permission error: {e}", file=sys.stderr)
    except KeyboardInterrupt:
        print("\nProcess interrupted by the user.", file=sys.stderr)
    except FileOrganizerException as e:
        print(f"FileOrganizer error: {e}", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
