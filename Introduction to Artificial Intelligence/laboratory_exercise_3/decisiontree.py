from collections import defaultdict
from typing import Dict, List
import math


class ID3:
    class Leaf:
        def __init__(self, label):
            self.label = label

        def __repr__(self):
            return f"Leaf({self.label})"

    class Node:
        def __init__(self, feature, subtrees, v):
            self.feature = feature
            self.subtrees = subtrees
            self.v = v

        def __repr__(self):
            return f"Node({self.feature}, {self.subtrees})"

    def __init__(self):
        self.tree = None

    def fit(self, D, X, class_label, y, max_depth='inf'):

        def argmax_v(D: List[Dict[str, str]], y: set) -> str:
            """
            Racuna najcescu oznaku primjera (class label) za neki cvor
            """

            class_label_counts = dict.fromkeys(y, 0)

            for row in D:
                class_label_counts[row[class_label]] += 1

            # class_label_counts je rjecnik oblika {'yes': 9, 'no': 5}

            # sortiramo po broju pojavljivanja, a ako je isti broj pojavljivanja, onda po abecedi
            # -x[1] je broj pojavljivanja, x[0] je oznaka
            # [0][0] je oznaka koja se najcesce pojavljuje
            return sorted(class_label_counts.items(), key=lambda x: (-x[1], x[0]))[0][0]

        def subset_class_label(D, v):
            """
            Funkcija koja provjerava je li skup primjera D s pripadnom oznakom klase v podskup skupa D
            To je slucaj ako je svaki primjer u D oznacen s v
            """

            filtered_D = []
            for row in D:
                if row[class_label] == v:
                    filtered_D.append(row)

            return len(filtered_D) == len(D)

        def entropy(D: List[Dict[str, str]]) -> float:
            """
            Racuna entropiju skupa primjera D
            """

            class_label_counts = dict.fromkeys(y, 0)
            for row in D:
                class_label_counts[row[class_label]] += 1

            entropy = 0
            for v in class_label_counts.values():
                if v == 0:
                    entropy += 0
                    continue
                entropy += -v / len(D) * math.log2(v / len(D))

            return entropy

        def information_gain(entropy_D: float, x: Dict[str, Dict[str, float]], total_count: int) -> float:
            """
            Racuna informacijski dobitak za neku znacajku (feature) x
            """
            return entropy_D - sum([v["count"] / total_count * v["entropy"] for v in x.values()])

        def generate_feature_values_dict(D: List[Dict[str, str]]) -> Dict[str, set]:
            """Funkcija kojom svakoj znacajki pridruzujemo skup svih vrijednosti tog atributa za dani dataset
            """
            feature_values_dict = defaultdict(set)

            for row in D:
                for feature, value in row.items():
                    if feature == class_label:
                        continue
                    feature_values_dict[feature].add(value)

            return feature_values_dict

        def print_ig_dict(ig_dict: Dict[str, float]):
            """
            Ispis informacijskog dobitka za svaku znacajku
            """
            for k, v in sorted(ig_dict.items(), key=lambda x: (-x[1], x[0])):
                print(f"IG({k})={v:.4f}", end=" ")
            print()

        def argmax_ig(D: List[Dict[str, str]], X: set):  # most important feature
            """
            Pronalazi znacajku koja ima najveci informacijski dobitak
            """

            entropy_D = entropy(D)

            feature_values_dict: Dict[str,
                                      set] = generate_feature_values_dict(D)  # rjecnik sa svim vrijednostima svake znacajke

            # rjecnik za informacijsku dobit {feature: ig}
            ig_dict: Dict[str, float] = dict.fromkeys(X, 0)

            for k in feature_values_dict.keys():
                # rjecnik za entropiju i broj primjera za svaku vrijednost znacajke
                entropy_count_dict = dict()
                for v in feature_values_dict[k]:
                    filtered_D = []
                    for row in D:
                        if row[k] == v:
                            filtered_D.append(row)
                    entropy_D_v = entropy(filtered_D)
                    entropy_count_dict[v] = {
                        "entropy": entropy_D_v, "count": len(filtered_D)}

                ig_dict[k] = information_gain(
                    entropy_D, entropy_count_dict, len(D))

            print_ig_dict(ig_dict)
            return sorted(ig_dict.items(), key=lambda x: (-x[1], x[0]))[0][0]

        def print_branches(tree, branch):
            """
            Ispisuje stablo u obliku stabla odluke

            Prima stablo i listu koja predstavlja granu. Lista se koristi kako bi se ispisala granu
            """
            if isinstance(tree, ID3.Leaf):
                branch_builder = ''

                for depth, node in enumerate(branch):
                    branch_builder += f"{depth + 1}:{node} "

                print(f"{branch_builder}{tree.label}")
            else:
                for value, subtree in tree.subtrees:
                    branch.append(f"{tree.feature}={value}")
                    print_branches(subtree, branch)
                    branch.pop()

        def id3(D: List[Dict[str, str]], D_parent: List[Dict[str, str]], X: set, y: set, max_depth, current_depth=0):  # initially Dparent = D

            # ako je dosegao maksimalnu dubinu, kao list postavi najcescu oznaku klase
            if current_depth == max_depth:
                v = argmax_v(D, y)
                return ID3.Leaf(v)

            # ako je skup primjera prazan, kao list postavi najcescu oznaku klase u skupu primjera roditelja
            if not D:
                v = argmax_v(D_parent, y)
                return ID3.Leaf(v)

            v = argmax_v(D, y)  # najcesca oznaka klase u skupu primjera D

            # ako vise nema znacajki ili je skup primjera D oznacen s v, kao list postavi v
            if not X or subset_class_label(D, v):
                return ID3.Leaf(v)

            x = argmax_ig(D, X)  # najznacajnija znacajka
            feature_values_dict = generate_feature_values_dict(
                D)  # rjecnik sa svim vrijednostima svake znacajke

            subtrees = []

            # za svaku vrijednost znacajke x, rekurzivno pozovi id3
            for value in feature_values_dict[x]:
                # filtriraj primjere koji imaju vrijednost value za znacajku x i pozovi id3
                filtered_D = []
                for row in D:
                    if row[x] == value:
                        filtered_D.append(row)
                t = id3(filtered_D, D, X - {x}, y,
                        max_depth, current_depth + 1)
                subtrees.append((value, t))

            return ID3.Node(x, subtrees, v)

        # nazovi id3
        self.tree = id3(D, D, X, y, max_depth)

        print('[BRANCHES]:')
        print_branches(self.tree, [])

    def predict(self, X):

        def traverse(node, x):
            """
            Rekurzivna funkcija koja za dani primjer x vraca predikciju

            Ako je node list, vraca njegovu oznaku
            Inace, za svaku vrijednost znacajke node.feature rekurzivno poziva traverse
            Ukoliko ne postoji podstablo za vrijednost znacajke, vraca najcescu oznaku klase u skupu primjera D za taj cvor
            """

            if isinstance(node, ID3.Leaf):
                return node.label

            feature_value = x[node.feature]
            for value, subtree in node.subtrees:
                if value == feature_value:
                    return traverse(subtree, x)

            return node.v

        predictions = []

        for x in X:
            predictions.append(traverse(self.tree, x))

        print('[PREDICTIONS]:', end=' ')
        for p in predictions:
            print(p, end=' ')

        print()
        return predictions
