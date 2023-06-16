def printPremise(premise, num):
            print(f"{num + 1}. ", end="")
            for num_literal, literal in enumerate(premise):
                if num_literal == len(premise) - 1:
                    print(f"{literal}")
                else:
                    print(f"{literal} v ", end="")


def outputConclusion(conclusion_str, resolvents, entry_premises, negated_goals, negated_goals_str):
            order = dict()
            last_num = 0
            for premise in resolvents:
                if frozenset(premise[1]) in entry_premises and frozenset(premise[1]) not in order:
                    printPremise(premise[1], last_num)
                    order[frozenset(premise[1])] = last_num + 1
                    last_num += 1
                elif frozenset(premise[2]) in entry_premises and frozenset(premise[2]) not in order:
                    printPremise(premise[2], last_num)
                    order[frozenset(premise[2])] = last_num + 1
                    last_num += 1

            
            for premise in resolvents:
                
                if premise[1] in negated_goals and frozenset(premise[1]) not in order:
                    order[frozenset(premise[1])] = last_num + 1
                    printPremise(premise[1], last_num)
                    last_num += 1
                elif premise[2] in negated_goals and frozenset(premise[2]) not in order:                    
                    order[frozenset(premise[2])] = last_num + 1
                    printPremise(premise[2], last_num)
                    last_num += 1

            
            print("===============")
            
            for premise in resolvents:
                if frozenset(premise[0]) not in order:
                    last_num += 1
                    print(f"{last_num}. ", end="")
                    for num_literal, literal in enumerate(premise[0]):
                        if num_literal == len(premise[0]) - 1:
                            print(f"{literal} ({order[frozenset(premise[1])]}, {order[frozenset(premise[2])]})")
                        else:                            
                            print(f"{literal} v ", end="")
                    order[frozenset(premise[0])] = last_num

            print("===============")
            
            print(f"[CONCLUSION]: {negated_goals_str} is {conclusion_str}")