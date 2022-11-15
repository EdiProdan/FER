import sys


def read_input():
    lines = []
    for line in sys.stdin:
        if len(line) == 0: break
        if line == "qu\n": break
        lines.append(line)
    return lines


class LexicalAnalyzer:
    def __init__(self, lines):
        self.lines, self.curRead, self.isIdn, self.isNum, self.component = lines, "", False, False, ""
        self.dict = {'=': 'OP_PRIDRUZI', '+': 'OP_PLUS', '-': 'OP_MINUS', '*': 'OP_PUTA', '/': 'OP_DIJELI',
                     '(': 'L_ZAGRADA', ')': 'D_ZAGRADA', 'za': 'KR_ZA', 'od': 'KR_OD', 'do': 'KR_DO', 'az': 'KR_AZ'}

    def analyze(self):
        for (i, line) in enumerate(self.lines): self.analyze_line(i + 1, line)

    def analyze_line(self, line_index, line):
        for (column, unit) in enumerate(line):
            if unit == ' ' or unit == '\t':
                self.print_current_unit(line_index)
                continue

            if unit == '\n':
                self.print_current_unit(line_index)
                continue

            if line[column] == '/' and line[column + 1] == '/':
                self.print_idn_num(line_index)
                self.reset_values()
                break

            if unit in self.dict:
                self.print_idn_num(line_index)
                print(self.dict[unit], line_index, unit)
                self.reset_values()
            else:
                self.analyze_idn_num(unit, line_index)

    def print_idn_num(self, line_index):
        if self.curRead != "":
            if self.isIdn:
                self.component = "IDN"
            elif self.isNum:
                self.component = "BROJ"
            print(self.component, line_index, self.curRead)

    def reset_values(self):
        self.curRead, self.isIdn, self.isNum, self.component = "", False, False, ""

    def analyze_idn_num(self, unit, line_index):
        self.curRead += unit
        if 'a' <= unit <= 'z' or 'A' <= unit <= 'Z':
            if self.isNum:
                self.curRead = self.curRead[:-1]
                print("BROJ", line_index, self.curRead)
                self.curRead, self.isNum, self.isIdn, self.component = unit, False, True, "IDN"
            else:
                self.isIdn = True
        elif '0' <= unit <= '9':
            if not self.isIdn: self.isNum = True

    def print_current_unit(self, line_index):
        if self.curRead in self.dict and self.curRead != "":
            print(self.dict[self.curRead], line_index, self.curRead)
        else:
            self.print_idn_num(line_index)
        self.reset_values()


if __name__ == "__main__":
    lines = read_input()
    lexical_analyzer = LexicalAnalyzer(lines)
    lexical_analyzer.analyze()
