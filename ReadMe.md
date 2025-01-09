# File Management Scripts Documentation

## Overview
This collection of Python scripts offers various functionalities for managing files and directories. Each script addresses a specific task, such as removing files, copying files, renaming files, filtering content, and more. These scripts are designed to automate and simplify file management tasks, handling common operations and exceptions to ensure smooth execution.

## Scripts Overview

### 1. ItemRemover
- Removes items (files or directories) recursively from a specified location.
- Handles exceptions such as file not found, permission errors, and unexpected errors during item removal.

### 2. FileCopier
- Copies files from a source directory to a destination directory.
- Provides statistics on the number of copied and uncopied files, and the total number of folders processed.
- Handles exceptions such as file not found, permission errors, and unexpected errors during file copying.

### 3. FileMover
- Moves files from a source directory to a destination directory.
- Provides statistics on the number of moved and unmoved files, and the total number of folders processed.
- Handles exceptions such as file not found, permission errors, and unexpected errors during file moving.

### 4. DirectoryDetails
- Retrieves and prints details of files and folders within a specified directory.
- Displays file names, paths, sizes, and timestamps for each file.
- Handles exceptions such as directory not found and permission errors.

### 5. ExtensionRenamer
- Renames file extensions for a specified file.
- Handles exceptions such as file not found, permission errors, and unexpected errors during extension renaming.

### 6. FileCopyer
- Copies a single file from a source directory to a destination directory.
- Handles exceptions such as file not found, permission errors, and unexpected errors during file copying.

### 7. FileManager
- Organizes files from a source directory into specific destination directories based on file extensions.
- Provides logging functionality for errors and operations.
- Handles exceptions such as source directory not found, permission errors, and unexpected errors during file organization.

### 8. FileMover (Second Implementation)
- Moves a single file from a source directory to a destination directory.
- Handles exceptions such as file not found, permission errors, and unexpected errors during file moving.

### 9. FileRemover
- Removes a single file specified by its location.
- Handles exceptions such as file not found, permission errors, and unexpected errors during file removal.

### 10. FileNameRenamer
- Renames a single file specified by its current filename and a new filename.
- Handles exceptions such as file not found, permission errors, and unexpected errors during file renaming.

### 11. ContentFilter (First Implementation)
- Scans a directory recursively to identify files and subdirectories.
- Prints information about each item, including its type (file or directory).
- Handles exceptions such as directory not found, permission errors, and unexpected errors during content filtering.

### 12. FolderRemover
- Removes a single folder specified by its location.
- Handles exceptions such as folder not found, permission errors, and unexpected errors during folder removal.

### 13. ContentFilter (Second Implementation)
- Recursively scans a directory to count the number of files and folders.
- Prints the total count of files and folders within the specified directory.
- Handles exceptions such as directory not found, permission errors, and unexpected errors during content filtering.

### 14. FileCreator
- Creates files with specific extensions (`.csv`, `.json`, `.txt`) if they do not already exist in the specified directory.
- Handles unsupported file extensions and file creation errors.

## Dependencies
- Python 3.x
- Standard libraries: os, sys, shutil, pathlib, json, csv
- Third-party libraries: None

## Usage
1. Execute each script using Python 3.x.
2. Follow the provided usage instructions for each script to perform specific file management tasks.
3. Review the output or log files generated by the scripts for information about the performed operations and any encountered errors.

## Conclusion
These Python scripts provide a diverse set of tools for managing files and directories efficiently. Users can utilize these scripts to automate tasks such as file removal, copying, moving, renaming, and organizing files based on their extensions. With error handling and logging capabilities, these scripts ensure robustness and reliability in file management operations.

As the curtain falls on this digital odyssey, let us reiterate: this project stands as a beacon of education, not a vessel for commercial endeavors. While its potential is boundless, its purpose remains rooted in the realm of learning. Thus, we absolve ourselves of any responsibility for its usage beyond the confines of educational exploration. Let knowledge be your guide, and may Python light the path to new discoveries.

*Tailor each script with surgical precision, sculpting bespoke solutions to cater to the unique needs of every user. Embrace the spirit of continuous improvement, as upgrades and customization stand as testament to Python's adaptability and resilience.*

## **License**
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

### **Disclaimer:**
Kindly note that this project is developed solely for educational purposes, not intended for industrial use, as its sole intention lies within the realm of education. We emphatically underscore that this endeavor is not sanctioned for industrial application. It is imperative to bear in mind that any utilization of this project for commercial endeavors falls outside the intended scope and responsibility of its creators. Thus, we explicitly disclaim any liability or accountability for such usage.