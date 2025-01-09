# File Extension Renamer Script Documentation

## Overview

The File Extension Renamer script is a Python utility designed to recursively search through directories and rename files based on their extensions. It enables users to modify file extensions in bulk, making it easier to manage file formats and streamline file organization. This script provides a user-friendly interface for inputting current extensions to be changed and a new extension to be applied.

## Features

- **Recursive Directory Traversal:** The script processes directories and their subdirectories to ensure all relevant files are handled.
- **File Extension Modification:** Allows users to specify multiple existing file extensions and a new extension to which files will be renamed.
- **Error Handling:** Comprehensive error handling for permissions issues, file not found errors, and interruptions, providing robust feedback and ensuring smooth operation.
- **Interactive User Input:** Prompts users for the list of file extensions to change and the new extension, with validation to ensure correct formats.
- **Result Reporting:** Provides a summary of the number of files modified, unchanged, and the total count processed.

## Dependencies

- **Python 3.x:** The script is designed to run with Python 3. It may not be compatible with Python 2 due to differences in syntax and library functions.
- **Standard Library Modules:** Utilizes built-in Python modules including `os` and `sys` for file and directory operations.

## Usage

1. **Preparation:** Ensure Python 3 is installed on your system. No additional libraries are required beyond the standard library.
2. **Script Execution:** Run the script in a command-line environment. The script will prompt for user input and execute based on provided parameters.

   ```bash
   python file_extension_renamer.py
   ```

3. **Input Prompts:** Follow the interactive prompts to specify:
   - **File Extensions to Change:** Provide a comma-separated list of file extensions you wish to rename.
   - **New File Extension:** Specify the new file extension to apply.

## Interactive Commands

- **File Extensions Input:** Enter a list of file extensions separated by commas (e.g., `.odt, .txt`). The script will process all files matching these extensions.
- **New File Extension Input:** Provide the new file extension (e.g., `.txt`). Ensure it starts with a dot to be valid.

## Special Commands

- **Keyboard Interrupt:** During execution, if you need to stop the script, you can use `Ctrl+C`. The script will handle the interruption gracefully and exit.

## Conclusion

The File Extension Renamer script is a powerful tool for managing file extensions across multiple directories. It simplifies the process of renaming files, providing a clear and interactive way to manage file formats. With its built-in error handling and comprehensive reporting, users can confidently execute bulk file operations while receiving immediate feedback on the script's execution. This tool is ideal for users needing to perform extensive file management tasks efficiently and effectively.