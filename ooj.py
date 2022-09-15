import sys

"""
dict = {
    'identifikator': 'IDN',
    'kons': 'BROJ',
    '=': 'OP_PRIDRUZI',
    '+': 'OP_PLUS',
    '-': 'OP_MINUS',
    '*': 'OP_PUTA',
    '/': 'OP_DIJELI',
    '(': 'L_ZAGRADA',
    ')': 'D_ZAGRADA',
    'za': 'KR_ZA',
    'od': 'KR_OD',
    'do': 'KR_DO',
    'az': 'KR_AZ',
}
"""


def read_input():
    lines = []
    for line in sys.stdin:
        if len(line) == 0:
            break
        if line == "qu\n":
            break
        lines.append(line)

    return lines


# noinspection PyShadowingNames
class LexicalAnalyzer:

    def __init__(self, lines):
        self.lines = lines
        self.curRead = ""
        self.isIdn = False
        self.isNum = False
        self.component = ""
        self.line = ""
        self.dict = {
            '=': 'OP_PRIDRUZI',
            '+': 'OP_PLUS',
            '-': 'OP_MINUS',
            '*': 'OP_PUTA',
            '/': 'OP_DIJELI',
            '(': 'L_ZAGRADA',
            ')': 'D_ZAGRADA',
            'za': 'KR_ZA',
            'od': 'KR_OD',
            'do': 'KR_DO',
            'az': 'KR_AZ',
            '//': 'KOMENTAR'
        }

    def analyze(self):
        for (i, line) in enumerate(self.lines):
            self.line = line
            self.analyze_line(i + 1)

    def analyze_line(self, line_index):  # k = "10"
        for (row, unit) in enumerate(self.line):

            # if reached space or tab, check if it is idn or num | az or za
            if unit == ' ' or unit == '\t':
                if self.curRead != "":
                    if self.curRead in self.dict:
                        print(self.dict[self.curRead], line_index, self.curRead )
                    else:
                        self.print_idn_num()
                        if self.isIdn:
                            self.component = "IDN"

                        elif self.isNum:
                            self.component = "BROJ"

                        print(self.component, line_index, self.curRead)

                self.reset_values()
                continue

            # if reached new line, check if it is idn or num
            if unit == '\n':
                if self.curRead != "":
                    if self.curRead in self.dict:
                        print(self.dict[self.curRead], line_index, self.curRead)

                    else:
                        if self.isIdn:
                            self.component = "IDN"

                        elif self.isNum:
                            self.component = "BROJ"

                        print(self.component, line_index, self.curRead)

                self.reset_values()

            else:
                # check if its a comment
                if self.line[row] == '/' and self.line[row + 1] == '/':
                    # obrisati sve do zadnja dva znaka
                    self.line = self.line[:-1]
                    # print everything before comment
                    if self.curRead != "":
                        if self.isIdn:
                            self.component = "IDN"
                        elif self.isNum:
                            self.component = "BROJ"
                        print(self.component, line_index, self.curRead)

                    self.reset_values()
                    # go to next line
                    break

                # check if its in a dict
                if unit in self.dict:
                    if self.curRead != "":
                        if self.isIdn:
                            self.component = "IDN"
                        elif self.isNum:
                            self.component = "BROJ"

                        print(self.component, line_index, self.curRead)

                    print(self.dict[unit], line_index, unit)
                    self.reset_values()
                else:
                    self.curRead += unit
                    if 'a' <= unit <= 'z' or 'A' <= unit <= 'Z':
                        if self.isNum:
                            # remove last char
                            self.curRead = self.curRead[:-1]
                            print("BROJ", line_index, self.curRead)
                            self.curRead = unit
                            self.isNum = False
                            self.isIdn = True
                            self.component = ""
                        else:
                            self.isIdn = True
                    elif '0' <= unit <= '9':
                        if self.isIdn:
                            continue
                        else:
                            self.isNum = True


    def print_idn_num(self):
        pass

    def reset_values(self):
        self.curRead = ""
        self.isIdn = False
        self.isNum = False
        self.component = ""


if __name__ == "__main__":
    lines = read_input()
    lexical_analyzer = LexicalAnalyzer(lines)
    lexical_analyzer.analyze()
