import csv
from typing import List, Dict, Tuple, Set


def load_train_data_from_csv(train_filename: str) -> Tuple[Set[str], str, List[Dict[str, str]]]:
    """
    Ucitava podatke za treniranje iz csv datoteke i vraca ih u obliku liste rjecnika
    """
    train_data: List[Dict[str, str]] = []

    with open("datasets/" + train_filename, 'r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)

        for row in csv_reader:
            row_dict = dict()
            for i, feature in enumerate(header):
                row_dict[header[i]] = row[i]
            train_data.append(row_dict)

        class_label = header[-1]
        header = set(header[:-1])

    return header, class_label, train_data


def load_test_data_from_csv(test_filename: str) -> Tuple[List[Dict[str, str]], List[str]]:
    """
    Ucitava podatke za testiranje iz csv datoteke i vraca ih u obliku liste rjecnika
    """
    test_data: List[Dict[str, str]] = []

    with open("datasets/" + test_filename, 'r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)
        class_label = header[-1]
        actual_class_label = []
        for row in csv_reader:
            row_dict = dict()
            for i, feature in enumerate(header):
                if feature == class_label:
                    actual_class_label.append(row[i])
                else:
                    row_dict[feature] = row[i]
            test_data.append(row_dict)

    return test_data, actual_class_label
