def append_line(text, file_path):
    """Append a text line to a file

    :parameter text: The text line to write to the end of the file
    :parameter file_path: Path to the file to write to
    """
    with open(file_path, 'a') as f:
        f.write(text)