from copy import copy
from my_exceptions import DestNotFoundException, SourceNotFoundException, PathNotFoundException

class ShortestPath:

    def find(self, net, s, t):
        s = s.upper()
        t = t.upper()

        # sanity check
        if net.has_key(s)==False:
            raise SourceNotFoundException()
        if net.has_key(t)==False:
            raise DestNotFoundException()
        if s == t:
            return [s]

        # create a labels dictionary
        labels={}

        # record whether a label was updated
        order={}

        # populate an initial labels dictionary
        for i in net.keys():
            if i == s: labels[i] = 0 # shortest distance form s to s is 0
            else: labels[i] = float("inf") # initial labels are infinity


        drop1 = copy(labels) # used for looping

        ## begin algorithm
        while len(drop1) > 0:
            # find the key with the lowest label
            # minNode is the node with the smallest label
            minNode = min(drop1, key = drop1.get) 
     
            # update labels for nodes that are connected to minNode
            for i in net[minNode]:
                if labels[i] > (labels[minNode] + net[minNode][i]):
                    labels[i] = labels[minNode] + net[minNode][i]
                    drop1[i] = labels[minNode] + net[minNode][i]
                    order[i] = minNode

            # once a node has been visited, it's excluded from drop1
            del drop1[minNode] 

        ## end algorithm

        temp = copy(t)

        path = []
        while 1:
            path.append(temp)
            if order.has_key(temp): temp = order[temp]
            else: raise PathNotFoundException()
            if temp == s:
                path.append(temp)
                break

        path.reverse()
        return path, labels[t]