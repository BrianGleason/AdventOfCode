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
        for line in lines:
            line = line.strip()
        return lines

