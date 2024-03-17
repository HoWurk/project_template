import os
from app.io.input import input_text_from_console, read_from_file_builtin, read_from_file_pandas
from app.io.output import write_to_file_builtin, output_text_to_console


def main():
    input_file_path = os.path.join('data', 'input.txt')
    output_file_path = os.path.join('data', 'output.txt')

    # Writes text from console into input file, then reads it with python capabilities,
    # then writes info from input file to output file
    input_text = input_text_from_console()
    write_to_file_builtin(input_text, input_file_path)

    file_content_builtin = read_from_file_builtin(input_file_path)
    output_text_to_console("Content read from file using Python's built-in capabilities:")
    output_text_to_console(file_content_builtin)
    write_to_file_builtin(file_content_builtin, output_file_path)

    # Reads new text using pandas
    write_to_file_builtin("New text to read", input_file_path)
    file_content_pandas = read_from_file_pandas(input_file_path)
    output_text_to_console("Content read from file using Pandas:")
    output_text_to_console(file_content_pandas)


if __name__ == '__main__':
    main()
