import math

def minimax(currDepth, nodeIndex, maxTurn, scores, targetDepth):
    if (currDepth == targetDepth):
        return scores[nodeIndex]
    if(maxTurn):
        return max(
            minimax(currDepth+1,nodeIndex*2,False, scores, targetDepth),
            minimax(currDepth+1, nodeIndex*2+1, False, scores, targetDepth))

    else:
        return min(
             minimax(currDepth+1,nodeIndex*2,True, scores, targetDepth),
            minimax(currDepth+1, nodeIndex*2+1, True, scores, targetDepth))

scores = [3, -25, 2, -17, -19, 5, 23, 21]
targetDepth = math.ceil(math.log2(len(scores)))
print("The value of minimax on root node = ",minimax(0,0,True,scores,targetDepth))