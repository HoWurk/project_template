def output_text_to_console(text):
    """Function to output text to the console.

    :param text: Text to read
    """
    print(text)


def write_to_file_builtin(text, file_path):
    """Function to write to a file using Python's built-in capabilities.

    :param text: Text to write
    :param file_path: Path to the file to write
    """
    with open(file_path, 'w') as file:
        file.write(text)
