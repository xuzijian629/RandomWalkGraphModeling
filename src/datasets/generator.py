from src.graph.er import ER
from src.graph.sb import SB
from src.graph.pc import PC
from src.graph.hm import HM
from src.graph.der import DER
from src.graph.dsb import DSB
from src.graph.dhm import DHM
from src.graph.utils import isConnected
from src.vectorize.walk2vec import walk2vec
from src.vectorize.walk2vecSC import getMs
from sklearn.decomposition import SparseCoder
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

def generateDERwalk2vec(times, n, p, s):
    path = input("Enter filename to save DER datasets...\n")
    with open(path, 'w') as f:
        try:
            i = 0
            while i < times:
                g = DER(n, p)
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

def generateDSBwalk2vec(times, n, delta, s):
    path = input("Enter filename to save DSB datasets...\n")
    with open(path, 'w') as f:
        try:
            i = 0
            while i < times:
                g = DSB(n, delta)
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

def generateHMwalk2vec(times, n, s):
    path = input("Enter filename to save HM datasets...\n")
    with open(path, 'w') as f:
        try:
            for i in range(times):
                g = HM(n)
                v = walk2vec(g, s)
                f.write(str(v) + '\n')
                sys.stdout.write("\r{}/{} finished".format(i + 1, times))

        except:
            os.remove(path)
            traceback.print_exc()
            exit(1)

    print("\rData successfully generated")

def generateDHMwalk2vec(times, n, s):
    path = input("Enter filename to save DHM datasets...\n")
    with open(path, 'w') as f:
        try:
            for i in range(times):
                g = DHM(n)
                v = walk2vec(g, s)
                f.write(str(v) + '\n')
                sys.stdout.write("\r{}/{} finished".format(i + 1, times))

        except:
            os.remove(path)
            traceback.print_exc()
            exit(1)

    print("\rData successfully generated")

def generateWalk2vecSC(D, times, n, vs, l):
    coder = SparseCoder(dictionary=D.components_, transform_alpha=l)
    path = input("Enter filename to save datasets...\n")
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
