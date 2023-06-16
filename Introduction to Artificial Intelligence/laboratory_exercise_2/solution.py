from arguments import args
import utils
import output


def resolution(entry_premises, negated_goals):
    premises = entry_premises.copy()

    set_of_support = []
    set_of_support.extend(negated_goals)
    premises.extend(set_of_support)
    premises = utils.deletion_strategy(premises)

    runAgain = True
    new = []
    while runAgain:
        runAgain = False
        # for each (c1, c2) in selectClauses(clauses) do
        for sos_clause in set_of_support:

            for literal in sos_clause:

                for premise in premises:
                    if literal.startswith("~"):
                        if literal[1:] in premise:
                            # resolvents ← plResolve(c1, c2)
                            resolvent = utils.resolve(
                                premise, sos_clause, literal[1:])

                            # if NIL ∈ resolvents then return true

                            if len(resolvent) == 0 and len(sos_clause) == 1:
                                resolvents.append(
                                    ({"NIL"}, premise, sos_clause))
                                premises.append({"NIL"})

                                return True

                            resolvents.append(
                                (resolvent, premise, sos_clause))
                            # new ← new ∪ resolvents
                            new.append(resolvent)
                            break

                    else:
                        if "~" + literal in premise:
                            # resolvents ← plResolve(c1, c2)
                            resolvent = utils.resolve(
                                premise, sos_clause, literal)

                            # if NIL ∈ resolvents then return true

                            if len(resolvent) == 0 and len(sos_clause) == 1:
                                resolvents.append(
                                    ({"NIL"}, premise, sos_clause))
                                premises.append({"NIL"})

                                return True

                            resolvents.append(
                                (resolvent, premise, sos_clause))

                            # new ← new ∪ resolvents
                            new.append(resolvent)

                            break

        if new:
            is_subset = True
            # usporedujemo element iz new sa svim premisama
            for new_premise in new:
                # ako se element iz new ne nalazi u premisama, onda je to novi element
                # tj., nije subset
                if new_premise not in premises:
                    is_subset = False

                    if is_subset:
                        runAgain = False
                        break
                    else:

                        premises.extend(new)
                        set_of_support.extend(new)

                        set_of_support = utils.deletion_strategy(
                            set_of_support)
                        premises = utils.deletion_strategy(premises)

                        runAgain = True
                        break
                else:
                    continue

    return False


if __name__ == "__main__":

    if args.command == 'resolution':

        entry_premises = []
        set_of_support = []
        data = []
        for line in open("./data/" + args.path_to_clauses, "r"):

            if line.startswith("#"):
                continue
            data.append(line)
            premise = set()
            line = line.lower().strip().split(" v ")
            for l_ in line:
                premise.add(l_.strip())
            entry_premises.append(premise)

        negated_goals_str = data[-1].lower().strip()

        negated_goals = entry_premises[-1].copy()
        entry_premises.remove(entry_premises[-1])

        for literal in negated_goals:
            if literal.startswith("~"):

                set_of_support.append({literal[1:]})
            else:
                set_of_support.append({"~" + literal})

        premises = entry_premises.copy()
        negated_goals = set_of_support.copy()

        premises.extend(set_of_support)

        premises = utils.deletion_strategy(premises)

        resolvents = []

        if resolution(entry_premises, negated_goals):
            output.outputConclusion(
                "true", resolvents, entry_premises, negated_goals, negated_goals_str)
        else:
            output.outputConclusion(
                "unknown", resolvents, entry_premises, negated_goals, negated_goals_str)

    elif args.command == 'cooking':

        entry_premises = []
        for line in open("./data/" + args.path_to_clauses, "r"):

            if line.startswith("#"):
                continue

            premise = set()
            line = line.lower().strip().split(" v ")
            for l_ in line:
                premise.add(l_.strip())
            entry_premises.append(premise)

        for line in open("./data/" + args.path_to_user_commands, "r"):

            if line.startswith("#"):
                continue

            line = line.lower().strip().split(" ")

            if line[-1] == '?':
                negated_goals = []
                if line[0].startswith("~"):
                    negated_goals.append({line[0][1:]})
                else:
                    negated_goals.append({"~" + line[0]})

                negated_goals_str = line[0]

                resolvents = []

                if resolution(entry_premises, negated_goals):
                    output.outputConclusion(
                        "true", resolvents, entry_premises, negated_goals, negated_goals_str)
                else:
                    output.outputConclusion(
                        "unknown", resolvents, entry_premises, negated_goals, negated_goals_str)

            elif line[-1] == '-':
                line = utils.transform_line(line)
                entry_premises.remove(line)

            elif line[-1] == '+':
                line = utils.transform_line(line)
                if line not in entry_premises:
                    entry_premises.append(line)
