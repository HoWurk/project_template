import pandas as pd


def input_text_from_console():
    """Function to input text from the console.

    :return: text
    """
    return input("Enter text: ")


def read_from_file_builtin(file_path):
    """Function to read from a file using Python's built-in capabilities.

    :param file_path: path of the file to read from

    :return: text read from file
    """
    with open(file_path, 'r') as file:
        return file.read()


def read_from_file_pandas(file_path):
    """Function to read from a file using the Pandas library.

    :param file_path: path of the file to read from

    :return: text read from file
    """
    # .columns[0] to get text directly from all the info pandas gives
    return pd.read_csv(file_path).columns[0]
