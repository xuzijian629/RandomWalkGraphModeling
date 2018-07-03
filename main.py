from sklearn.ensemble import RandomForestClassifier
import numpy as np
import os, random

def main():
    ER = []
    SBM = []
    path = input("Enter filename of ER datasets...\n")
    with open(path) as f:
        for line in f:
            ER.append((eval(line), -1))
    path = input("Enter filename of SBM datasets...\n")
    with open(path) as f:
        for line in f:
            SBM.append((eval(line), 1))

    train = ER[:len(ER) // 2] + SBM[:len(SBM) // 2]
    random.shuffle(train)

    test = ER[len(ER) // 2:] + SBM[len(SBM) // 2:]
    model = RandomForestClassifier()
    model.fit([*map(lambda x: x[0], train)], [*map(lambda x: x[1], train)])

    predict = model.predict([*map(lambda x: x[0], test)])
    correct = np.sum(predict == np.array([*map(lambda x: x[1], test)]))
    print("correct: {}/{}".format(correct, len(test)))


if __name__ == '__main__':
    main()
