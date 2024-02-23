import os
import sys
import random

def secure_delete(file_path, passes=3):
    try:
        file_size = os.path.getsize(file_path)
        with open(file_path, 'rb+') as file:
            for _ in range(passes):
                file.seek(0)
                random_data = bytearray(os.urandom(file_size))
                file.write(random_data)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

    try:
        os.remove(file_path)
        print(f"File securely deleted: {file_path}")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python secure_delete.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    secure_delete(file_path)
