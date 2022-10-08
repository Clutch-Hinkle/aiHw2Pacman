# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

from ast import While
from asyncore import loop
import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    stack = util.Stack()
    solStack = util.Stack()
    from game import Directions
    n = Directions.NORTH
    s = Directions.SOUTH
    e = Directions.EAST
    w = Directions.WEST


    start = problem.getStartState()
    visitedStates = set()
    sol = list()

    stack.push(start)
    solStack.push(sol)

    while True:
        if stack.isEmpty():
            print('no solution was found')
            return

        currentState = stack.pop()
        solution = solStack.pop()

        if problem.isGoalState(currentState):
            break

        if currentState not in visitedStates:
            visitedStates.add(currentState)
            for x in problem.getSuccessors(currentState):
                stack.push(x[0])
                tmpSol = solution.copy()
                tmpSol.append(x[1])
                solStack.push(tmpSol)

        

        

    

    print(solution)
    
    return solution

    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    q = util.Queue()
    from game import Directions
    n = Directions.NORTH
    s = Directions.SOUTH
    e = Directions.EAST
    w = Directions.WEST

    currentState = problem.getStartState()
    start = problem.getStartState()
    visitedStates = {currentState}
    path = {}
    solution = list()

    while not problem.isGoalState(currentState):
        for x in problem.getSuccessors(currentState):
            if x[0] not in visitedStates:
                q.push(x)
                visitedStates.add(x[0])
                path[x[0]] = (currentState,[x[1]])


        if q.isEmpty():
            print("No more moves in the queue")
            break

        successor = q.pop()
        currentState = successor[0]


    while currentState != start:
        solution.append(path[currentState][1][0])
        currentState = path[currentState][0]

    solution.reverse()
    print("Number of moves in solution: ",len(solution))

    
    return solution

    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    # pQ = util.PriorityQueue()

    # start = problem.getStartState()
    # currentState = [problem.getStartState(),0]
    # visitedStates = [currentState]

    # # print('current start',currentState[0])

    # path = {}
    # solution = list()

    # while not problem.isGoalState(currentState[0]):
    #     for x in problem.getSuccessors(currentState[0]):
    #         totalCost = currentState[1] + x[2]
    #         if x[0] not in visitedStates:
    #             y = [x[0],x[1],totalCost]
    #             pQ.update(y,totalCost)
    #             visitedStates.append(x[0])
    #             path[x[0]] = (currentState[0],[x[1]])
                

    #     if pQ.isEmpty():
    #         print("No more moves in the queue")
    #         break
        
    #     successor = pQ.pop()
    #     #print(successor)
    #     currentState = [successor[0], x[2]]

    # print(path)
    # location = currentState[0]
    # while location != start:
    #     solution.append(path[location][1][0])
    #     location = path[location][0]

    # solution.reverse()
    # return solution

    pQ = util.PriorityQueue()
    solStack = util.PriorityQueue()

    start = problem.getStartState()
    visitedStates = list()
    sol = list()

    pQ.push(start,0)
    solStack.push(sol,0)

    while True:
        if pQ.isEmpty():
            print('no solution was found')
            return

        currentState = pQ.pop()
        solution = solStack.pop()
        currentLocation = currentState
        currentCost = problem.getCostOfActions(solution)

        if problem.isGoalState(currentLocation):
            break

        if currentState not in visitedStates:
            visitedStates.append(currentState)
            for x in problem.getSuccessors(currentLocation):
                newCost = currentCost + x[2]
                pQ.push(x[0],newCost)
                tmpSol = solution.copy()
                tmpSol.append(x[1])
                solStack.push(tmpSol,newCost)


    #print(solution)
    
    return solution
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    pQ = util.PriorityQueue()
    solStack = util.PriorityQueue()

    start = problem.getStartState()
    visitedStates = list()
    sol = list()

    pQ.push(start,0)
    solStack.push(sol,0)

    while True:
        if pQ.isEmpty():
            print('no solution was found')
            return

        currentState = pQ.pop()
        solution = solStack.pop()
        currentLocation = currentState
        currentCost = problem.getCostOfActions(solution)

        if problem.isGoalState(currentLocation):
            break

        if currentState not in visitedStates:
            visitedStates.append(currentState)
            for x in problem.getSuccessors(currentLocation):
                newCost = currentCost + x[2] + heuristic(x[0],problem)
                pQ.push(x[0],newCost)
                tmpSol = solution.copy()
                tmpSol.append(x[1])
                solStack.push(tmpSol,newCost)


    #print(solution)
    
    return solution
    util.raiseNotDefined()
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
