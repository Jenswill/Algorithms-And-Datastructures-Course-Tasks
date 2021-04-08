class MST():
    #predefining lists for quick union algorithm
    def __init__(self) -> None:
        self.N_list = [[]]
        self.M_list = [[]]
        
    #makes list of a nodes
    def makeNlist(self):
        N=int(input())
        self.N_list = [x for x in range(N)]
        
    #defines weight of paths between nodes
    def defineWeights(self):
        M = int(input())
        self.M_list = [[] for x in range(M)]

        for i in range(M):
            weight_input = input().split()
            X = int(weight_input[0])
            Y = int(weight_input[1])
            weight = int(weight_input[2])
            self.M_list[i] = [weight,X,Y]
        self.M_list.sort()

    #Defines Find method for quick union algorithm
    def Find(self, i):
        while i != self.N_list[i]:
            i = self.N_list[i]
        return i  
    #Defines Union Method for quick union algorithm
    def Union(self,i,j):
        r_i = self.Find(i)
        r_j = self.Find(j)
        if r_i != r_j:
            self.N_list[r_i] = r_j
            return True
        else:
            return False
        
    #Defines method for Kruskals algorithm for minimum spanning trees
    def MST(self):
        path = 0
        
        
        for i in self.M_list:
            if self.Union(i[1],i[2]):
                path += i[0]
            
        return path
            
        

def main():
    mst = MST()
    mst.makeNlist()
    mst.defineWeights()
    path = mst.MST() #Defines shortest total path between all nodes
    print(str(path)) #Prints total path length

main()