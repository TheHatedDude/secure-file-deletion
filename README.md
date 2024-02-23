# Secure File Deletion Tool

This is a command-line interface (CLI) tool developed in Python for securely deleting files by overwriting them with random data multiple times, making it difficult for the deleted data to be recovered.

## Features

- Securely delete files by overwriting them with random data multiple times.
- Simple CLI interface for easy usage.

## Requirements

- Python 3.x

## Usage

1. Clone or download the repository.
2. Navigate to the directory containing the `secure_delete.py` file.
3. Run the script from the command line and provide the file path as an argument:

    ```
    python secure_delete.py /path/to/file
    ```

    Replace `/path/to/file` with the path to the file you want to securely delete.

## Example


Certainly! Here's a simple README file for the secure file deletion tool:

vbnet
Copy code
# Secure File Deletion Tool

This is a command-line interface (CLI) tool developed in Python for securely deleting files by overwriting them with random data multiple times, making it difficult for the deleted data to be recovered.

## Features

- Securely delete files by overwriting them with random data multiple times.
- Simple CLI interface for easy usage.

## Requirements

- Python 3.x

## Usage

1. Clone or download the repository.
2. Navigate to the directory containing the `secure_delete.py` file.
3. Run the script from the command line and provide the file path as an argument:

    ```
    python secure_delete.py /path/to/file
    ```

    Replace `/path/to/file` with the path to the file you want to securely delete.

## Example

python secure_delete.py /path/to/myfile.txt



## Notes

- This tool overwrites the contents of the file specified with random data multiple times before deleting it, making it more difficult for the deleted data to be recovered.
- Adjust the `passes` parameter in the `secure_delete` function of the script to specify the number of times the file should be overwritten for increased security.

## Disclaimer

- Use this tool responsibly and ensure you have the necessary permissions to delete the files.
- The effectiveness of secure deletion may vary depending on various factors such as storage medium and recovery techniques.

