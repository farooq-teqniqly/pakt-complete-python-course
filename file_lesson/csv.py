import os.path
from typing import Generator, List


def read_csv(path: str, separator: str = ",", first_row_has_header: bool = True) -> Generator[List[str], None, None]:
    if not os.path.isfile(path):
        raise OSError(f"The file {path} could not be opened.")

    if len(separator.strip()) == 0:
        separator = ","

    with open(path, "r") as reader:
        lines = reader.read().splitlines()

    if first_row_has_header:
        headers = lines[0].split(separator)

    for index, line in enumerate(lines):
        if first_row_has_header and index > 0:
            yield list(zip(headers, line.split(separator)))
        elif not first_row_has_header:
            yield line.split(separator)


if __name__ == "__main__":
    input_csv_path = input("CSV file to read: ")
    input_csv_separator = input("Column delimited (press ENTER for comma): ")
    input_first_row_has_header_str = input("First row contains header? (Y or N, default is Y): ")

    input_first_row_has_header = True

    if input_first_row_has_header_str == "N":
        input_first_row_has_header = False

    csv_lines = read_csv(input_csv_path, separator=input_csv_separator, first_row_has_header=input_first_row_has_header)

    for csv_line in list(csv_lines):
        print(csv_line)
