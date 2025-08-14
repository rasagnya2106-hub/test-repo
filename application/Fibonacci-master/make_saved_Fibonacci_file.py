# J. Pocahontas Olson   June 2016
# Function to make a binary file containing the first MAX_NUMBER_OF_SAVED_DIGITS Fibonacci numbers

import fibonacci_module as fb
import os.path
import distutils.util


NUMBER_OF_BYTES = 16384   # 4 bytes = 32 bit, 8 bytes = 64 bit, ... (fib gets big fast)
MAX_NUMBER_OF_SAVED_DIGITS = 1e5  # If want to store more, will have to increase NUMBER_OF_BYTES
filename = 'savedFibonacciNumbers.bin'


def make_saved_fibonacci_file():
    """
    Make a binary file containing the first MAX_NUMBER_OF_SAVED_DIGITS Fibonacci numbers.
    """
    print("Making a binary file with the first", int(MAX_NUMBER_OF_SAVED_DIGITS), "Fibonacci numbers.")
    # See if file exists already, and warn
    if os.path.isfile(filename):
        prompt = "Warning: " + filename + " already exists with " + str(os.path.getsize(filename)/NUMBER_OF_BYTES)
        prompt += " digits.
  Do you wish to overwrite?: (Y/N)"
        ans = input(prompt)
        overwrite = distutils.util.strtobool(ans)
        if not overwrite:
            print("..Exiting without writing over", filename, "..")
            return

    saved_list = fb.fib_list(MAX_NUMBER_OF_SAVED_DIGITS)
    
    # Write binary data to a file
    with open(filename, 'wb') as f:
        for num in saved_list:
            f.write(num.to_bytes(NUMBER_OF_BYTES, byteorder='big', signed=False))


if __name__ == "__main__":
    make_saved_fibonacci_file()
