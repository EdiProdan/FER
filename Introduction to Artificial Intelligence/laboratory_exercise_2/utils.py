def deletion_strategy(premises):
    # while True:
    deleted = True
    while deleted:
        # Uklanjanje redundantnih klauzula:
        for premise_first in premises:
            deleted = False
            for premise_second in premises:
                if premise_first == premise_second:
                    continue
                if premise_first.issubset(premise_second):
                    # returns True if all items in the set exists in the specified set, otherwise it returns False
                    premises.remove(premise_second)
                    deleted = True

    # Uklanjanje nevaznih klauzula:
    for premise in premises:
        for literal in premise:
            if "~" + literal in premise:
                # print(f"Delete premise {premise}")
                premises.remove(premise)

    return premises


def transform_line(line):
    line = line[0:-1]
    for l in line:
        if l == 'v':
            line.remove(l)
    return set(line)


def resolve(premise, sos_clause, literal):
    new_premise = premise.union(sos_clause)
    new_premise.remove(literal)
    new_premise.remove("~" + literal)
    return new_premise

