from src.graph.er import ER
from src.graph.sbm import SBM
from src.graph.utils import isConnected
from src.vectorize.walk2vec import walk2vec
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

def generateSBMwalk2vec(times, n, pin, pout, s):
    path = input("Enter filename to save SBM datasets...\n")
    with open(path, 'w') as f:
        try:
            i = 0
            while i < times:
                g = SBM(n, pin, pout)
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
