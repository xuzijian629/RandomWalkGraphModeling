from sklearn.ensemble import RandomForestClassifier
import numpy as np
import os, random

def main():
    A = []
    B = []
    path = input("Enter filename of datasets A...\n")
    with open(path) as f:
        for line in f:
            A.append((eval(line), -1))
    path = input("Enter filename of datasets B...\n")
    with open(path) as f:
        for line in f:
            B.append((eval(line), 1))

    train = A[:len(A) // 2] + B[:len(B) // 2]
    random.shuffle(train)

    test = A[len(A) // 2:] + B[len(B) // 2:]
    model = RandomForestClassifier()
    model.fit([*map(lambda x: x[0], train)], [*map(lambda x: x[1], train)])

    predict = model.predict([*map(lambda x: x[0], test)])
    correct = np.sum(predict == np.array([*map(lambda x: x[1], test)]))
    print("correct: {}/{}".format(correct, len(test)))


if __name__ == '__main__':
    main()
