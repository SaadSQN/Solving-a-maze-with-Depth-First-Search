import numpy as np
from copy import copy,deepcopy
depthVariable = 0
visited = []
costVariable = 0
allNodes = []


class Node:
    def __init__(self, state, parent, operator, depth, cost):
        self.state = state
        self.parent = parent
        self.operator = operator
        self.depth = depth
        self.cost = cost

def create_node(state, parent, operator, depth, cost):
    return Node(state, parent, operator, depth, cost)

def move_left(state,row,column):
    global costVariable
    costVariable = costVariable + 1
    
    AnswerRow = 0
    AnswerColumn = 0
    #Checking position of 0
    countX = 0
    countY = 0
    for x in state:
        countX =countX + 1
        countY = 0
        for y in x:
            countY = countY + 1
            if y == 8.0:
                
                AnswerRow = countX
                AnswerColumn = countY
                break

    
    #Boundary conditions
    if AnswerColumn == 1 :
        return None

    
    #Switching places
    AnswerRow = AnswerRow - 1
    AnswerColumn = AnswerColumn - 1
    state[AnswerRow][AnswerColumn-1] = 8
    state[AnswerRow][AnswerColumn]= 1  

    

    return state    

def move_right(state,row,column):
    global costVariable
    costVariable = costVariable + 1
    
    AnswerRow = 0
    AnswerColumn = 0
    #Checking position of 0
    countX = 0
    countY = 0
    for x in state:
        countX =countX + 1
        countY = 0
        for y in x:
            countY = countY + 1
            if y == 8.0:
                
                AnswerRow = countX
                AnswerColumn = countY
                break

    #Boundary conditions
    if AnswerColumn == column :
        return None

    
    #Switching places
    AnswerRow = AnswerRow - 1
    AnswerColumn = AnswerColumn - 1
    state[AnswerRow][AnswerColumn+1] = 8
    state[AnswerRow][AnswerColumn]= 1  

    

    return state    

def move_up(state,row,column):
    global costVariable
    costVariable = costVariable + 1
    
    AnswerRow = 0
    AnswerColumn = 0
    #Checking position of 0
    countX = 0
    countY = 0
    for x in state:
        countX =countX + 1
        countY = 0
        for y in x:
            countY = countY + 1
            if y == 8.0:
                
                AnswerRow = countX
                AnswerColumn = countY
                break

    #Boundary conditions
    if AnswerRow == 1 :
        return None

    
    #Switching places
    AnswerRow = AnswerRow - 1
    AnswerColumn = AnswerColumn - 1
    state[AnswerRow-1][AnswerColumn] = 8
    state[AnswerRow][AnswerColumn]= 1  

    

    return state    

def move_down(state,row,column):
    global costVariable
    costVariable = costVariable + 1
    
    AnswerRow = 0
    AnswerColumn = 0
    #Checking position of 0
    countX = 0
    countY = 0
    for x in state:
        countX =countX + 1
        countY = 0
        for y in x:
            countY = countY + 1
            if y == 8.0:
                
                AnswerRow = countX
                AnswerColumn = countY
                break

    #Boundary conditions
    if AnswerRow == row :
        return None

    
    #Switching places
    AnswerRow = AnswerRow - 1
    AnswerColumn = AnswerColumn - 1
    state[AnswerRow+1][AnswerColumn] = 8
    state[AnswerRow][AnswerColumn]= 1  

    

    return state   

def arrayChecker(s1 , s2,r,c):
    for x in range(0,r):
        for y in range(0,c):

            if s1[x][y] != s2[x][y]:
                return False
    
    return True

def checkVisited(a1,rows,columns):
    found = False
    for x in visited:
        if arrayChecker(a1,x.state,rows,columns) == True:
            found = True
    return found   

def expand_node(node,rows,columns):

    global depthVariable
    depthVariable = depthVariable + 1
    expanded_nodes = []
    # ----- code here
   
    #Checking position of 8
    AnswerRow = 0
    AnswerColumn = 0
    #Checking position of 8
    countX = 0
    countY = 0
    for x in node.state:
        countX =countX + 1
        countY = 0
        for y in x:
            countY = countY + 1
            if y == 8.0:
                
                AnswerRow = countX
                AnswerColumn = countY
                break
    
    AnswerRow = AnswerRow - 1
    AnswerColumn = AnswerColumn - 1
    
    #Check for move up 
    a1 = deepcopy(node.state)
    if AnswerRow != 0 and node.state[AnswerRow-1][AnswerColumn] == 1:
        a1 = move_up(a1,rows,columns)
        #check if its in visited
        if checkVisited(a1,rows,columns) == False:
            sub = create_node(a1,node.state,"up",depthVariable,depthVariable)
            expanded_nodes.append(sub)
            
    #Check for move left
    a4 = deepcopy(node.state)
    if AnswerColumn != 0 and node.state[AnswerRow][AnswerColumn-1] == 1:
        a4 = move_left(a4,rows,columns)
        #check if its in visited
        if checkVisited(a4,rows,columns) == False:
            sub = create_node(a4,node.state,"left",depthVariable,depthVariable)
            expanded_nodes.append(sub)

     #Check for move right
    a3 = deepcopy(node.state)
    if AnswerColumn != 11 and node.state[AnswerRow][AnswerColumn+1] == 1:
        a3 = move_right(a3,rows,columns)
        #check if its in visited
        if checkVisited(a3,rows,columns) == False:
            sub = create_node(a3,node.state,"right",depthVariable,depthVariable)
            expanded_nodes.append(sub)
            
    #Check for move down
    a2 = deepcopy(node.state)
    if AnswerRow != 11 and node.state[AnswerRow+1][AnswerColumn] == 1:
        a2 = move_down(a2,rows,columns)
        #check if its in visited
        if checkVisited(a2,rows,columns) == False:
            sub = create_node(a2,node.state,"down",depthVariable,depthVariable)
            expanded_nodes.append(sub)        

    
    return expanded_nodes

def dfs(start, goal,rows,columns):
     #---- code here -----
   
   #Check whether start is Goal
    one = np.array(start.state)
    two = np.array(goal.state)
    value = one == two

    
    if value.all() == True:
        finalAnswer = start
        return None
    
    queue = []
    queue.append(start)
    answerFound = False
    allNodes.append(start)
    stack = []

    while answerFound == False:
        #check if queue is empty
        if not queue:
            queue.append(stack.pop())

        #check if current Node is Answer
        current = queue.pop(0)
        if (arrayChecker(current.state,goal.state,rows,columns)) == True:
            answerFound = True
            visited.append(current)
            break

        #If current Node is not answer , expand the node and add one to checking queue , the others to stack
        expanded = expand_node(current,rows,columns)
        visited.append(current)
        for i in expanded:
            allNodes.append(i)
        
        if len(expanded) != 0:
            queue.append(expanded[0])
            for i in reversed(expanded):
                    stack.append(i)    
            stack.pop()


    print("Cost of calculation : ")
    counter = 0
    for i in visited:
        counter = counter + 1
    print(counter)

    print("\nPath of Calculation : \n")
    for i in visited:
        print(i.state)
        print("\n")
    print("\n")
    backTrackerVisited(goal,start,rows,columns)

def backTrackerVisited(answerNode , startNode,rows,columns):
    cost = 0
    final = answerNode.state
    toPrint = []
    for x in reversed (visited):
        if(arrayChecker(answerNode.parent,x.state,12,12)):
             cost = cost + 1   
             #print(answerNode.operator)
             toPrint.append(answerNode.operator)
             answerNode = x
             final = answerNode.state
    print("\nCost of Reaching solution : " + str(cost - 1)+"\n")
    toPrint.pop(0)
    print("Path to Solution : \n ")
    for x in reversed (toPrint):
        print(x)            

def main():
    #Program takes input of maze size from user , as well as initial and final state of maze from files

    dim =input("Rows in Maze : ")
    dim2 =input("Columns in Maze : ")
    data = np.genfromtxt("/home/saad/Downloads/Semester6/AI/Assignment01/input.txt")
    data2 = np.genfromtxt("/home/saad/Downloads/Semester6/AI/Assignment01/input2.txt")
    #Node with initial position
    testNode = create_node(data, data , "None",0,0)
    #Node with final position
    testNode2 = create_node(data2, data2 , "None",0,0)
    print("\n")
    #print(arrayChecker(data,data,12,12))
    print("\n******************************\n")
    temp = expand_node(testNode,12,12)
    dfs(testNode , testNode2 , int(dim) , int(dim2))
    
if __name__ == "__main__":
    main()