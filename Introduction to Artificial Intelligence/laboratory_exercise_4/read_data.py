def read_train_data(path):
    data = []
    for line in open("./data/" + path):
        data.append(line.strip().split(','))

    features = data[0][:-1]
    target = data[0][-1]

    X = []
    y = []
    for line in data[1:]:
        X.append([float(x) for x in line[:-1]])
        y.append(float(line[-1]))

    return features, target, X, y


def read_test_data(path):
    data = []
    for line in open("./data/" + path):
        data.append(line.strip().split(','))
    X = []
    y = []
    for line in data[1:]:
        X.append([float(x) for x in line[:-1]])
        y.append(float(line[-1]))
    return X, y
