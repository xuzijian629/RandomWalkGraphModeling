from src.graph.er import ER
from src.graph.sb import SB
from src.graph.pc import PC
from src.graph.hm import HM
from src.graph.utils import isConnected
from src.vectorize.walk2vec import walk2vec
from src.vectorize.walk2vecSC import getMs
from sklearn.decomposition import MiniBatchDictionaryLearning
import numpy as np
import sys, random

def generateERvs(times, n, p, s):
    i = 0
    vs = []
    while i < times:
        g = ER(n, p)
        if isConnected(g):
            vs += getMs(g, s)
            sys.stdout.write("\rGenerating graphs: {}/{} finished".format(i + 1, times))
            i += 1
    assert len(vs) == times * n
    return vs

def generateSBvs(times, n, delta, s):
    i = 0
    vs = []
    while i < times:
        g = SB(n, delta)
        if isConnected(g):
            vs += getMs(g, s)
            sys.stdout.write("\rGenerating graphs: {}/{} finished".format(i + 1, times))
            i += 1
    assert len(vs) == times * n
    return vs

def generatePCvs(times, n, beta, s):
    i = 0
    vs = []
    while i < times:
        g = PC(n, beta)
        if isConnected(g):
            vs += getMs(g, s)
            sys.stdout.write("\rGenerating graphs: {}/{} finished".format(i + 1, times))
            i += 1
    assert len(vs) == times * n
    return vs

def generateHMvs(times, n, s):
    vs = []
    for i in range(times):
        g = HM(n)
        vs += getMs(g, s)
        sys.stdout.write("\rGenerating graphs: {}/{} finished".format(i + 1, times))
    assert len(vs) == times * n
    return vs

def learnDictionary(D, vs1, vs2):
    vs = vs1 + vs2
    random.shuffle(vs)
    D = D.fit(vs)
    print("\rDictionary successfully learned")
    return D, vs1, vs2
