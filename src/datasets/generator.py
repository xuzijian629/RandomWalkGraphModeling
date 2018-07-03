from src.graph.er import ER
from src.graph.sbm import SBM
from src.vectorize.walk2vec import walk2vec
import os, sys, traceback

def generateERwalk2vec(times, n, p, s):
    path = input("Enter filename to save data...\n")
    with open(path, 'w') as f:
        try:
            for i in range(times):
                g = ER(n, p)
                v = walk2vec(g, s)
                f.write(' '.join([*map(str,v)]) + '\n')
                sys.stdout.write("\r{}/{} finished".format(i + 1, times))
        except:
            os.remove(path)
            traceback.print_exc()
            exit(1)

    print("\rData successfully generated")

def generateSBMwalk2vec(times, n, pin, pout, s):
    path = input("Enter filename to save data...\n")
    with open(path, 'w') as f:
        try:
            for i in range(times):
                g = SBM(n, pin, pout)
                v = walk2vec(g, s)
                f.write(' '.join([*map(str,v)]) + '\n')
                sys.stdout.write("\r{}/{} finished".format(i + 1, times))
        except:
            os.remove(path)
            traceback.print_exc()
            exit(1)

    print("\rData successfully generated")
