def degreeFinder(listOfWords):
    dictOfDegree={}
    for i in copyListOfDiploma :
        for j in listOfWords:
            if j in i.upper(): 
                dictOfDegree[list(dictOfDiploma.keys())[list(dictOfDiploma.values()).index(i)]] = i
                break
    copyListOfDiploma[:]=[x for x in copyListOfDiploma if x not in list(dictOfDegree.values())]
    return dictOfDegree
  
#return a dict of (node1,node2) : W
def findCC(inputDict):
    cCDict={}
    lower=list(inputDict.keys())
    for i in inputDict:
        lookInList=[]
        lower.remove(i)
        if len(lower) ==0:
            break
        for m in lower: 
            lookInList.extend(inputDict[m])
        for k in inputDict[i]:
            for l in R.neighbors(k):
                if l in lookInList:
                    cCDict[(k,l)]=R[k][l]['w']
    return cCDict
  
  
  def findDomainOfDiplom(G,dip):
    preWords=[i for i in G.successors(dip)]
    marque=[]
    result=[]
    for sommet in preWords:
        f=[]
        f.insert(0,sommet)
        marque.append(sommet)
        while (len(f)!=0):
            sommet=f.pop()
            if sommet not in result:
                result.append(sommet)
            L=list(G.successors(sommet))
            for t in L:
                if t not in marque:
                    f.insert(0,t)
                    marque.append(t)
    finalresult=[]
    for i in result:
        if WR2.nodes[i]["kind"]=="ref_domain":
            finalresult.append(i)
    return finalresult
  
  
  
