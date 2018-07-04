from src.graph.er import ER
from src.graph.sb import SB
from src.graph.pc import PC
from src.graph.utils import isConnected
from src.vectorize.walk2vec import walk2vec
from src.vectorize.walk2vecSC import getMs
from sklearn.decomposition import MiniBatchDictionaryLearning, SparseCoder
import numpy as np
import os, sys, traceback

def generateERwalk2vec(times, n, p, s):
    path = input("Enter filename to save ER datasets...\n")
    with open(path, 'w') as f:
        try:
            i = 0
            while i < times:
                g = ER(n, p)
                if isConnected(g):
                    v = walk2vec(g, s)
                    f.write(str(v) + '\n')
                    sys.stdout.write("\r{}/{} finished".format(i + 1, times))
                    i += 1
        except:
            os.remove(path)
            traceback.print_exc()
            exit(1)

    print("\rData successfully generated")

def generateSBwalk2vec(times, n, delta, s):
    path = input("Enter filename to save SB datasets...\n")
    with open(path, 'w') as f:
        try:
            i = 0
            while i < times:
                g = SB(n, delta)
                if isConnected(g):
                    v = walk2vec(g, s)
                    f.write(str(v) + '\n')
                    sys.stdout.write("\r{}/{} finished".format(i + 1, times))
                    i += 1
        except:
            os.remove(path)
            traceback.print_exc()
            exit(1)

    print("\rData successfully generated")

def generatePCwalk2vec(times, n, beta, s):
    path = input("Enter filename to save PC datasets...\n")
    with open(path, 'w') as f:
        try:
            i = 0
            while i < times:
                g = PC(n, beta)
                if isConnected(g):
                    v = walk2vec(g, s)
                    f.write(str(v) + '\n')
                    sys.stdout.write("\r{}/{} finished".format(i + 1, times))
                    i += 1
        except:
            os.remove(path)
            traceback.print_exc()
            exit(1)

    print("\rData successfully generated")

def generateERwalk2vecSC(times, n, p, s, atom=100, l=0.15):
    i = 0
    vs = []
    while i < times:
        g = ER(n, p)
        if isConnected(g):
            vs += getMs(g, s)
            sys.stdout.write("\rGenerating graphs: {}/{} finished".format(i + 1, times))
            i += 1
    assert len(vs) == times * n
    dic = MiniBatchDictionaryLearning(n_components=atom, alpha=l)
    D = dic.fit(vs).components_
    coder = SparseCoder(dictionary=D, transform_alpha=l)
    path = input("\rEnter filename to save ER datasets...\n")
    with open(path, 'w') as f:
        try:
            for i in range(times):
                v = coder.transform(vs[i * n: (i + 1) * n])
                v = np.average(v, axis=0)
                f.write(str(v.tolist()) + '\n')
                sys.stdout.write("\r{}/{} finished".format(i + 1, times))
        except:
            os.remove(path)
            traceback.print_exc()
            exit(1)

    print("\rData successfully generated")

def generateSBwalk2vecSC(times, n, delta, s, atom=100, l=0.15):
    i = 0
    vs = []
    while i < times:
        g = SB(n, delta)
        if isConnected(g):
            vs += getMs(g, s)
            sys.stdout.write("\rGenerating graphs: {}/{} finished".format(i + 1, times))
            i += 1
    assert len(vs) == times * n
    dic = MiniBatchDictionaryLearning(n_components=atom, alpha=l)
    D = dic.fit(vs).components_
    coder = SparseCoder(dictionary=D, transform_alpha=l)
    path = input("\rEnter filename to save SB datasets...\n")
    with open(path, 'w') as f:
        try:
            for i in range(times):
                v = coder.transform(vs[i * n: (i + 1) * n])
                v = np.average(v, axis=0)
                f.write(str(v.tolist()) + '\n')
                sys.stdout.write("\r{}/{} finished".format(i + 1, times))
        except:
            os.remove(path)
            traceback.print_exc()
            exit(1)

    print("\rData successfully generated")

def generatePCwalk2vecSC(times, n, beta, s, atom=100, l=0.15):
    i = 0
    vs = []
    while i < times:
        g = PC(n, beta)
        if isConnected(g):
            vs += getMs(g, s)
            sys.stdout.write("\rGenerating graphs: {}/{} finished".format(i + 1, times))
            i += 1
    assert len(vs) == times * n
    dic = MiniBatchDictionaryLearning(n_components=atom, alpha=l)
    D = dic.fit(vs).components_
    coder = SparseCoder(dictionary=D, transform_alpha=l)
    path = input("\rEnter filename to save PC datasets...\n")
    with open(path, 'w') as f:
        try:
            for i in range(times):
                v = coder.transform(vs[i * n: (i + 1) * n])
                v = np.average(v, axis=0)
                f.write(str(v.tolist()) + '\n')
                sys.stdout.write("\r{}/{} finished".format(i + 1, times))
        except:
            os.remove(path)
            traceback.print_exc()
            exit(1)

    print("\rData successfully generated")
