from src.graph.er import ER
from src.graph.pc import PC
from src.vectorize.walk2vecJoe import walk2vecJoe
from src.test.visualize import visualizeDists

n = 200
beta = 0.8
s = 15

def main():
    er = ER(n, 0.5)
    pc = PC(n, beta)
    erj = walk2vecJoe(er, s)
    erj.preprocess()
    pcj = walk2vecJoe(pc, s)
    pcj.preprocess()
    visualizeDists(s, erj, pcj)

if __name__ == '__main__':
    main()
