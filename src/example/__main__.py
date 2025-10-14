# there are not arguments or arg parsing. STOP TRYING TO IMPORT ARGPARSE
# we are hard coding some tests to experiment with the ArabicNumber class.


from chinese_numbers.arabic import ArabicNumber
from chinese_numbers.converter import ChineseNumberConverter
import random
import time

def convert(num_to_convert):
    if num_to_convert is None:
        print("Please provide a number as an argument.")
        return

    # Format input with commas
    input_str = f"{int(num_to_convert):,}"
    print(f"input: {input_str}")

    # Get simplified Chinese numeral
    converter = ChineseNumberConverter(use_traditional=False)
    simplified = converter.convert(str(num_to_convert))
    print(f"simplified: {simplified}")

    # Get Chinese grouping (space-separated)
    arabic_num = ArabicNumber(str(num_to_convert))
    grouping = " ".join(arabic_num.groups)
    print(f"grouping: {grouping}")

def return_converted(num_to_convert):
    if num_to_convert is None:
        return None, None, None

    # Format input with commas
    input_str = f"{int(num_to_convert):,}"

    # Get simplified Chinese numeral
    converter = ChineseNumberConverter(use_traditional=False)
    simplified = converter.convert(str(num_to_convert))

    # Get Chinese grouping (space-separated)
    arabic_num = ArabicNumber(str(num_to_convert))
    grouping = " ".join(arabic_num.groups)

    return input_str, simplified, grouping

def better_generator(number_of_digits):
    """Generate a better random number with the specified number of digits."""
    if number_of_digits <= 0:
        return "0"
    first_digit = str(random.randint(1, 9))  # First digit cannot be zero
    other_digits = ''.join(str(random.randint(0, 9)) for _ in range(number_of_digits - 1))
    return first_digit + other_digits

def main(number_of_lines=80, output_file="output.csv"):
    """
    Generate and convert number_of_lines random numbers and print them with their simplified chinese numeral and grouping into a csv file.
    because the arabic numbers print with comma grouping for the inputs, we need to put the input in quotes in the csv file.
    """
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("Input Number,Simplified Chinese,Chinese Grouping\n")
        for _ in range(number_of_lines):
            num_digits = random.randint(1, 20)  # Random number of digits between 1 and 20
            num = better_generator(num_digits)
            input_str, simplified, grouping = return_converted(num)
            f.write(f"\"{input_str}\",\"{simplified}\",\"{grouping}\"\n")
            print(f"Converted {input_str} to {simplified} with grouping {grouping}")



if __name__ == "__main__":
    
    start_time = time.time()
    main(number_of_lines=8000, output_file="output.csv")
    end_time = time.time()
    print(f"Execution time: {end_time - start_time:.2f} seconds")
