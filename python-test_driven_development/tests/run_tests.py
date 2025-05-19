# run_tests.py

import doctest
import os

test_file_path = '3-say_my_name'

if not os.path.exists(test_file_path):
    print(f"Error: Test file not found at {test_file_path}")
    exit(1)

# Run the tests from the specified file
# verbose=True gives more detailed output (failures and successes)
# report=True provides a summary at the end
if __name__ == "__main__":
    print(f"Running tests from {test_file_path}...")
    doctest.testfile(test_file_path, verbose=True)
    print("Tests finished.")
