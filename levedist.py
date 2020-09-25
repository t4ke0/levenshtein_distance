import sys
from pprint import pprint

class Levenshtein:
    def __init__(self,w1,w2):
        self.matrix = []
        if len(w1) > len(w2):
            self.B = w1
            self.S = w2
        else:
            self.B = w2
            self.S = w1

    def _setup_Matrix(self):
        row = [i for i in range(len(self.S)+1)]
        self.matrix.append(row)
        col = []
        for i in range(len(self.B)+1):
            if i != 0:
                col.append(i)
                self.matrix.append(col)
                col = []

    def distance(self) -> int:
        self._setup_Matrix()
        for i,x in enumerate(self.B):
            for j,y  in enumerate(self.S):
                if x != y:
                    self.matrix[i+1].append(min(self.matrix[i][j],self.matrix[i][j+1],self.matrix[i+1][j])+1)
                else:
                    self.matrix[i+1].append(self.matrix[i][j]) 
        return self.matrix[-1][-1] 

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(
                """
                USAGE: python3 levdist.py <word1> <word2>
                """
                )
        sys.exit(1)

    w1 = sys.argv[1]
    w2 = sys.argv[2]
    l = Levenshtein(w1,w2)
    print("distance :",l.distance())
    pprint(l.matrix)
