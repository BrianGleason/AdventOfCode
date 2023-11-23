import pyperclip

class IOHelpers:
    def __init__():
        pass

    def cp(s):
        pyperclip.copy(s)

    def read_lines(source_file):
        file = open(source_file, 'r')
        lines = file.readlines()
        return lines
    
    def read_lines_stripped(source_file):
        file = open(source_file, 'r')
        lines = file.readlines()
        stripped = []
        for line in lines:
            stripped.append(line.strip())
        return stripped

