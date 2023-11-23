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
    
    def parse_by_empty_newline(source_file, splitter=" ", one_per_line=False):
        file = open(source_file, 'r')
        lines = file.readlines()
        result = []
        current = []
        for line in lines:
            if line.strip() == "":
                result.append(current)
                current = []
            else:
                ct = line.strip().split(splitter)
                if one_per_line: ct = ct[0]
                current.append(ct)

        result.append(current)
        return result
            

