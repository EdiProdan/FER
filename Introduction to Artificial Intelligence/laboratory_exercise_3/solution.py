from arguments import args
import read_files
from decisiontree import ID3


def get_class_label_set(D, class_label: str) -> set:
    """
    Iz dataseta vraca set svih mogucih oznaka klase
    """
    class_label_set = set()
    for row in D:
        class_label_set.add(row[class_label])
    return class_label_set


def calculate_accuracy(predictions, actual_class_label, total):
    """
    Racuna preciznost predikcije
    """
    correct = 0
    for i in range(total):
        if predictions[i] == actual_class_label[i]:
            correct += 1

    return correct/total


def calculate_confusion_matrix(predictions, actual_class_label, y, total):
    """
    Racuna matricu konfuzije
    """
    Y = len(y)
    y = sorted(y)
    confusion_matrix = [[0 for i in range(Y)] for j in range(Y)]

    for i in range(total):
        pred = predictions[i]
        true = actual_class_label[i]
        pred_index = y.index(pred)
        true_index = y.index(true)
        confusion_matrix[true_index][pred_index] += 1

    return confusion_matrix


if __name__ == '__main__':
    X, class_label, D = read_files.load_train_data_from_csv(args.train)
    y = get_class_label_set(D, class_label)

    D_test, actual_class_label = read_files.load_test_data_from_csv(args.test)

    max_depth = args.depth

    id3 = ID3()

    # treniranje
    id3.fit(D, X, class_label, y, max_depth)

    # predikcija
    predictions = id3.predict(D_test)

    total = len(predictions)
    accuracy = calculate_accuracy(predictions, actual_class_label, total)
    print(f'[ACCURACY]: {accuracy:.5f}')

    confusion_matrix = calculate_confusion_matrix(
        predictions, actual_class_label, y, total)

    print(f'[CONFUSION_MATRIX]:')
    for i in range(len(confusion_matrix)):
        for j in range(len(confusion_matrix)):
            print(confusion_matrix[i][j], end=' ')
        print()
