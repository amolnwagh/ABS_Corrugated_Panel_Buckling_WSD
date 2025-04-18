import csv


def str_to_int(s: str) -> int|str:
    """
    converts an input string to int if possible, else returns the string as it is
    """
    try:
        output = int(s)
    except ValueError:
        output = s   
    return output


def str_to_float(s: str) -> float|str:
    """
    converts an input string to float if possible, else returns the string as it is
    """
    try:
        output = float(s)
    except ValueError:
        output = s   
    return output


def read_csv_file_without_csv_module(file_name:str) ->list:
    file_data = []
    with open(file_name, 'r') as file:
        for line in file.readlines():
            file_data.append(line.strip().split(","))
    return file_data
        


def read_csv_file(file_name:str) -> list:
    """
    takes a text file at given file path and returns entire data in the file as a list.
    every item on this list is a row in the input text file
    """
    file_data = []
    with open(file_name, 'r') as csv_file:
        csv_data = csv.reader(csv_file)
        for data_line in csv_data:
            file_data.append(data_line)
    return file_data


def write_csv_file_with_header(file_name:str, header:list, data:list[list]) -> None:
    """
    takes a list of lists and writes to a csv file.
    every item in this list is a row in csv file
    """
    with open(file_name, 'w') as csv_file:
        write = csv.writer(csv_file,lineterminator="\n")
        write.writerow(header)
        write.writerows(data)
        
def write_csv_file_no_header(file_name:str, data:list[list]) -> None:
    """
    takes a list of lists and writes to a csv file.
    every item in this list is a row in csv file
    """
    with open(file_name, 'w') as csv_file:
        write = csv.writer(csv_file,lineterminator="\n")
        write.writerows(data)